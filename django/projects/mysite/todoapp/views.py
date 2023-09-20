from django.shortcuts import render, redirect
from todoapp.forms import LoginForm, RegisterForm, ListForm
from todoapp.models import User, TodoList
import hashlib
from datetime import datetime


def custom_login(request, nickname):
    request.session['nickname'] = nickname


def custom_logout(request):
    request.session.pop('nickname', "")


def get_nickname(request):
    return request.session.get('nickname', "")


def sha256_encode(text):
    return hashlib.sha256(text.encode()).hexdigest()


def home(request):
    return render(request, 'home.html', {'nickname': get_nickname(request)})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # 비번 일치
            if form.clean_password1() == form.clean_password2():
                # 닉네임 중복
                if not User.objects.filter(nickname=form.clean_nickname()).exists():
                    q = User(nickname=form.clean_nickname(), password=sha256_encode(form.clean_password1()))
                    q.save()
                    custom_login(request, form.clean_nickname())
                    return redirect('home')
                else:
                    error = '이미 존재하는 닉네임입니다.'
            else:
                error = '비밀번호가 일치하지 않습니다.'
        else:
            error = '입력된 값이 없습니다.'
    else:
        form = RegisterForm()
        error = ''

    return render(request, 'register.html', {'form': form, 'error': error, 'nickname': get_nickname(request)})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # 닉네임 확인
            if User.objects.filter(nickname=form.clean_nickname()).exists():
                encoded_password = User.objects.get(nickname=form.clean_nickname()).password
                if encoded_password == sha256_encode(form.clean_password()):
                    custom_login(request, form.clean_nickname())
                    return redirect('home')
                else:
                    error = '비밀번호가 일치하지 않습니다.'
            else:
                error = '존재하지 않는 닉네임입니다.'
        else:
            error = '입력된 값이 없습니다.'
    else:
        form = LoginForm()
        error = ''

    return render(request, 'login.html', {'form': form, 'error': error, 'nickname': get_nickname(request)})


def logout(request):
    custom_logout(request)
    return redirect('home')


def lists(request):
    nickname = get_nickname(request)

    if nickname == "":
        return redirect("error")
    else:
        user_id = User.objects.get(nickname=nickname).id

        if request.method == 'POST':
            form = ListForm(request.POST)
            if form.is_valid():
                error = ''
                q = TodoList(subject=form.clean_subject(),
                             contents=form.clean_contents(),
                             create_date=datetime.now(),
                             is_completed=False,
                             user_id = user_id)
                q.save()
            else:
                error = '입력된 값이 없습니다.'
        else:
            form = ListForm()
            error = ''

        lists = TodoList.objects.filter(user_id=user_id)

        return render(request, 'lists.html', {'nickname': get_nickname(request), 'error': error, 'lists': lists})


def error(request):
    nickname = get_nickname(request)

    if nickname == "":
        error_message = "로그인이 필요합니다."
    else:
        error_message = "알 수 없는 오류가 발생했습니다."

    return render(request, 'error.html', {'error': error_message, 'nickname': nickname})
