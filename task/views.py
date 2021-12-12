from django.http.response import HttpResponseNotFound, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.conf import settings

from .forms import TaskForm
from .models import Check, Task
from .generic import TaskListView

import secrets, pytz

SERVER_TZ = pytz.timezone(settings.TIME_ZONE)

# Create your views here.
@login_required
def index(request):
    view = TaskListView.as_view()
    return view(request)

@login_required
def create(request):

    timezone.activate(SERVER_TZ)

    if request.method == 'GET':
        
        new_task = Task()
        now = timezone.now()
        new_task.date_opening = now.astimezone(SERVER_TZ).date()
        new_task.start_time   = now.astimezone(SERVER_TZ).time().replace(second=0)
        new_task.end_time     = now.astimezone(SERVER_TZ).time().replace(second=0)

        form = TaskForm(instance=new_task)
        context = {
            'title': 'Task - Create',
            'task_active': 'active',
            'form': form,
        }

        return render(request, 'task/create.html', context)
    
    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():

            request.user.task_set.create(
                name         = form.cleaned_data['name'],
                key          = secrets.token_urlsafe(16),
                password     = form.cleaned_data['password'],
                date_opening = form.cleaned_data['date_opening'],
                start_time   = form.cleaned_data['start_time'],
                end_time     = form.cleaned_data['end_time']
            )

            return redirect('task')

        context = {
            'title': 'Task - Create',
            'task_active': 'active',
            'form': form,
        }
        return render(request, 'task/create.html', context)

def join(request):

    if request.method == 'POST':
        key = request.POST.get('key')
        item = Task.objects.filter(key=key).first()
        if item:
            response_data = {
                'link' : f'/task/detail/{item.id}',
                'owner': item.owner.email,
                'name' : item.name,
                'date_opening': item.date_opening,
                'start_time'  : item.start_time.strftime("%H:%M"),
                'end_time'    : item.end_time.strftime("%H:%M")
            }
            return JsonResponse(response_data)
        else:
            return HttpResponseNotFound("No result.")
    
    context = {
        'title': 'Join',
        'join_active': 'active',
    }

    return render(request, 'task/join.html', context)

def detail(request, id):

    context = {
        'title': 'TaskDetail',
    }

    if request.method == "POST":
        pwd = request.POST.get('password')
        request.session[f'task_{id}_password'] = pwd
        return redirect('task_detail', id=id)

    if 'quit' in request.GET:
        request.session[f'task_{id}_password'] = None
        return redirect('task_join')

    task = get_object_or_404(Task, id=id)
    if task.owner.id != request.user.id:
        pwd = request.session.get(f'task_{id}_password')
        if pwd is None:
            return enter_password(request, context)

        if task.password != pwd:
            context['error'] = 'Incorrect password.'
            request.session[f'task_{id}_password'] = None
            return enter_password(request, context)

    context['item'] = task
    context['is_enrolled'] = task.check_set.filter(user__pk=request.user.id)

    return render(request, 'task/detail.html', context)


def enter_password(request, context):
    return render(request, 'task/password.html', context)


def check(request, task_id):

    user = request.user
    task = get_object_or_404(Task, id=task_id)

    if user.id == task.owner.id:
        return HttpResponse("You cannot self-enroll in your task.", status=405)

    if task.check_set.filter(user__pk=request.user.id):
        return HttpResponse("You have already joined.")

    pwd = request.session.get(f'task_{task_id}_password')
    if pwd != task.password:
        return redirect('task_detail', id=task_id)

    if timezone.now().astimezone(SERVER_TZ).date() != task.date_opening \
    or not task.start_time <= timezone.now().astimezone(SERVER_TZ).time() <= task.end_time:

        return HttpResponse("Time out.", status=405)
    
    Check.objects.create(task=task, user=user)

    return HttpResponse("Enroll successfully.")