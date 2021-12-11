from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import notes
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def index(request):
    context={}
    return render(request, 'login.html', context)


def home(request):
    user_log = request.user
    note_list = notes.objects.filter(user=user_log)
    context = {'note': note_list}
    
    return render(request, 'index.html', context)


def add_note(request):
    if request.method == "POST":
        title = request.POST['title']
        des = request.POST['desc']
        user = request.user
        ins = notes(title=title, description = des, user=user )
        ins.save()
        messages.add_message(request, messages.SUCCESS, "Add A Note Successfully")
        return redirect('home')
    
    return render(request, 'index.html')


def delete(request, id):
        note_list = notes.objects.get(pk=id)
        note_list.delete()
        messages.add_message(request, messages.SUCCESS, "Delete Successful")

        return redirect('home')


def edit_note(request, id):
    data = notes.objects.get(id=id)
    item_list = notes.objects.all()

    context = {
        'data':data,
        'item_list':item_list
    }
    
    return render(request, 'index.html',context)  



def update_data(request, id):
    item= notes.objects.get(id=id)
    item.title=request.POST['title']
    item.description=request.POST['desc']
    item.save()
    messages.success(request, "Note Updated")
    return redirect('home')

    

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                messages.success(request, "New User Creation Successful")
                return redirect('login')
        else:
            return render (request,'signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            messages.add_message(request, messages.SUCCESS, "Welcome To Keep Note")
            return redirect('home')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')

def logout(request):
        auth.logout(request)
        return redirect('login')

def search(request):
    search = request.GET['search']
    query = notes.objects.filter(title__icontains=search)
    
    return render(request, 'search.html', {'query':query})
    



   
        