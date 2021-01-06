from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from .forms import CreatePollForm
from .models import Poll
from .models import Poll_Trigger
from django.contrib.auth.models import User


def home(request):
    polls = Poll.objects.all()
    users = User.objects.all()
    # select * from polls_poll;
    polls_triggers = Poll_Trigger.objects.all().last()
    context = {
        'polls': polls,
        'users': users,
        'polls_triggers': polls_triggers,
    }
    return render(request, 'polls/home_poll.html', context)


def dictfetchall(cursor):
    # Return all rows from a cursor as a dict
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def user_questions(request):
    cursor = connection.cursor()
    cursor.execute("select username, count(question) as count from auth_user, polls_poll where polls_poll.username_id "
                   "= "
                   "auth_user.id group by username having count(question) > 0")
    # cursor.execute("select content from blog_post") cursor.execute("select title from blog_post, polls_poll,
    # auth_user where blog_post.author_id = auth_user.id and auth_user.username = 'Nimesh'")
    row3 = dictfetchall(cursor)
    return render(request, 'polls/user_questions.html', {'data3': row3})


def create(request, self=None):
    cursor = connection.cursor()
    if request.method == 'POST':
        form = CreatePollForm(request.POST)

        if form.is_valid():
            form.save()
            cursor.execute("drop trigger my_trigger")
            cursor.execute("create trigger my_trigger after insert on polls_poll when new.category = 'Science' begin "
                           "insert into polls_poll_trigger(message) values('added science category'); "
                           "end;")
            cursor.execute("drop trigger my_trigger1")
            cursor.execute("create trigger my_trigger1 after insert on polls_poll when new.category = 'Random' begin "
                           "insert into polls_poll_trigger(message) values('added random category'); "
                           "end;")
            cursor.execute("drop trigger my_trigger2")
            cursor.execute("create trigger my_trigger2 after insert on polls_poll when new.category = 'Comic' begin "
                           "insert into polls_poll_trigger(message) values('added comic category'); "
                           "end;")
            return redirect('poll_home')
    else:
        form = CreatePollForm()

    context = {'form': form}
    return render(request, 'polls/create_poll.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    # 'select id from polls_poll where id == %s', [poll_id]
    context = {
        'poll': poll,
    }
    return render(request, 'polls/results.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    # Poll.objects.raw("select id from polls_poll where id = %s", [poll_id])

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
            # poll.raw("update polls_poll set 'option_one_count' = 'option_one_count' + 1")
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form option')

        poll.save()

        return redirect('poll_results', poll.id)

    context = {
        'poll': poll
    }
    return render(request, 'polls/vote_poll.html', context)
