from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('dashboard:show_campaigns')