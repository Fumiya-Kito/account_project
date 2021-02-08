from django.shortcuts import render, redirect
from .forms import AccountCreateForm, UserCreateForm
from .models import Account
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request,'account/index.html')

def register_user(request):
    user_form = UserCreateForm(request.POST or None)
    account_form = AccountCreateForm(request.POST or None)

    if request.method == "POST" and user_form.is_valid() and account_form.is_valid:
        #Userモデル
        user = user_form.save(commit=False)
        user.is_activate = True
        user.save()

        # Accountモデル ↑紐付けよう
        account = account_form.save(commit=False)
        # ログインしている状態なら、 = request.user
        account.user = user
        # account.image = request.FILES.get('image', None)
        account.save()
        # add manytomanyフィールドで使うcommit=Falseのとき必要
        # account_form.save_m2m()
        
        return redirect('login')


    context = {
        'user_form':user_form,
        'profile_form':account_form,
    }
    return render(request,'account/user_create.html', context)

def loginfunc(request):
    if request.method == 'POST':
        username1= request.POST['username']
        password1 = request.POST['password']
        user = authenticate(request, username=username1, password=password1)
        

        # ? ユーザーがいる場合
        if user is not None:
            login(request, user)
            return redirect('account_detail', pk=user.pk)
        else:
            return render(request, 'account/login.html',{'error':'ログインに失敗しました'})
    return render(request,'account/login.html')

@login_required
def listfunc(request):
    object_list = Account.objects.all()
    return render(request,'account/list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = Account.objects.get(pk=pk)
    return render(request, 'account/account_detail.html', {'object':object})