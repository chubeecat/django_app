from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Friend, Message
from .forms import HelloForm, FriendForm, FindForm, CheckForm, MessageForm


def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 3)
    params = {
        'title': 'Hello',
        'message': '',
        'data': page.get_page(num),
    }
    # params = {
    #     'title':'Hello',
    #     'message':'all friends.',
    #     'form':[],
    #     'data':[],
    # }
    # if request.method == 'POST':
    #     num = request.POST['id']
    #     params['data'] = [Friend.objects.get(id=num)]
    #     params['form'] = HelloForm(request.POST)
    # else:
    #     params['data'] = Friend.objects.all().order_by('age').reverse()
    #     params['form'] = HelloForm()
    return render(request, 'hello/index.html', params)


def create(request):
    params = {
        'title':'Hello',
        'message':'Please create data.',
        'form':FriendForm(),
    }
    if request.method == 'POST':
        friend = FriendForm(request.POST, instance=Friend())
        if friend.is_valid():
            params['message'] = 'OK. Please create next data. '
            friend.save()
            return redirect(to='/hello/create')
        else:
            params['message'] = 'no good.'
    return render(request, 'hello/create.html', params)


def edit(request, num):
    obj = Friend.objects.get(id=num)
    if request.method == 'POST':
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id':num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)


def delete(request, num):
    obj = Friend.objects.get(id=num)
    if request.method == 'POST':
        obj.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id':num,
        'obj': obj,
    }
    return render(request, 'hello/delete.html', params)


def find(request):
    if request.method == 'POST':
        str = request.POST['find']
        list = str.split()
        msg = 'search result:'
        form = FindForm(request.POST)
        data = Friend.objects.filter(name__in=list)
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message':msg,
        'form': form,
        'data':data,
    }
    return render(request, 'hello/find.html', params)


def check(request):
    params = {
        'title':'Hello',
        'message':'check validation',
        'form':FriendForm()
    }
    if request.method == 'POST':
        # form = CheckForm(request.POST)
        form = FriendForm(request.POST, instance=Friend())
        params['form'] = form
        if form.is_valid():
            params['message'] = 'OK'
        else:
            params['message'] = 'no good.'
    return render(request, 'hello/check.html', params)


def message(request, page=1):
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=Message())
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 3)
    params = {
        'title': 'Message',
        'form': MessageForm(),
        'data': paginator.get_page(page),
    }
    return render(request, 'hello/message.html', params)