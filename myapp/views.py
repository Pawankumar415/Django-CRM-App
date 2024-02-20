from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm,AddRecordForm
from .models import Record


def home_page(request):
    records = Record.objects.all()
    # check to if loging in
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'you have been logged in {username}')
            return redirect('myapp:home_page')
        else:
            messages.error(request, 'There was an error logging in!!!')
            return redirect('myapp:home_page')
    else:

        return render(request, 'home.html', {'records': records})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "you have been logged out!!!")
        return redirect("myapp:home_page")
    else:
        return render(request, 'home.html')


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "you have successfully Register!")
            return redirect('myapp:home_page')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def record_detail(request, pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Record, id=pk)
        return render(request, 'detail.html', {'record': record})
    else:
        messages.success(request,"you must login for view this page!")
        return redirect('myapp:home_page')


def delete_record(request, pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Record, id=pk)
        record.delete()
        messages.success(request,'record deleted successfully')
        return redirect('myapp:home_page')
    else:
        messages.success(request, "you must login for delete records!!!")
        return redirect('myapp:home_page')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request,"Record Added Successfully!!!")
                return redirect('myapp:home_page')

        return render(request, 'add_record.html',{'form':form})
    messages.success(request, "you must be login for Add records!!!")
    return redirect('myapp:home_page')


def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = get_object_or_404(Record, id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Updated Successfully!!!')
            return redirect('myapp:home_page')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request, 'you must be login to update the record!')
        return redirect("myapp:home_page")