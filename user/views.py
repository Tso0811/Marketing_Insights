from django.contrib.auth import logout , authenticate , login
from django.shortcuts import redirect , render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('dashboard:show_campaigns')

def login_view(request):
    errors={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username :
            errors['username'] = '請輸入使用者名稱'
        if not password :
            errors['password'] = '請輸入密碼'    

        if not errors:  #當errors字典為空進入判斷
            user = authenticate(request , username=username , password=password)
            if user :
                login(request , user)
                return redirect('dashboard:show_campaigns')
            else:
                return redirect('user:login_view')
    return render(request , 'login.html')

def register_view(request):
    errors={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        email = request.POST.get('email')
        if password != password_confirm :
            errors['password_confirm'] = '兩次密碼輸入不一樣'

        if User.objects.filter(username=username):
            errors['username'] = '使用者名稱已存在'
        
        if not errors:
            user = User.objects.create_user(username=username , password=password , email=email)
            
            send_mail(
            subject='註冊成功',
            message='您好，感謝您註冊成為我們的會員！',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,           
            )
            
            login(request , user)
            return redirect('dashboard:show_campaigns')
    return render(request , 'register.html' , {'errors':errors})