from django.shortcuts import render
from campaigns.models import Campaigns
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404 ,redirect
from django.contrib import messages
from django.contrib.auth.models import User


from .serializers import CampaignsSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated #加入授權功能

from django.core.mail import send_mail
from django.conf import settings


def show_campaigns(request):    #直接在dashboard中顯示 不需要點擊進入細節
    campaign = Campaigns.objects.all()
    return render(request , 'dashboard.html' , {'campaigns':campaign})

@login_required
def edit_campaigns(request , id):
    campaign = get_object_or_404(Campaigns , pk=id)

    if campaign.poster == request.user: #判斷操作者是否為上傳活動者
        if request.method == 'POST':
            new_name = request.POST['name']
            new_start_date = request.POST['start_date']
            new_budget = request.POST['budget']

            campaign.name = new_name
            campaign.start_date = new_start_date
            campaign.budget = new_budget

            campaign.save()
            messages.success(request , '編輯成功')

            return redirect('dashboard:show_campaigns')
    else:
        messages.warning(request, '無權限編輯此活動')
        return redirect('dashboard:show_campaigns')

    return render(request, 'campaign_form.html', {'campaign': campaign})

@login_required
def campaign_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        start_date = request.POST.get('start_date')
        budget = request.POST.get('budget')
        poster = request.user

        new_campaign = Campaigns(name=name , start_date=start_date , budget=budget , poster=poster)
        new_campaign.save()

        return redirect('dashboard:show_campaigns')

    return render(request , 'campaign_form.html')

@login_required
def campaign_delete (request , id):
    campaign = get_object_or_404(Campaigns , pk=id)

    if campaign.poster == request.user:
        if request.method == 'POST':
            campaign.delete()
            messages.success(request , '成功刪除')
            return redirect('dashboard:show_campaigns')
    else :
        messages.warning(request , '無權限刪除此活動')
        return redirect('dashboard:show_campaigns')
    
    return render(request , 'campaign_delete.html' , {'campaign':campaign})

@login_required
def campaign_click (request , id):
    campaign = get_object_or_404(Campaigns , pk=id)
    campaign.click += 1
    campaign.save()
    
    user = campaign.poster
    if campaign.click>50 and (campaign.click % 50 == 0):
        send_mail(
                subject='活動通知',
                message = f'您好，您的活動目前已經突破 {campaign.click} 人參加',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,           
                )          

    return redirect('dashboard:show_campaigns')

def postercampaigns(request , poster):
    user = get_object_or_404(User , username=poster)
    campaigns = Campaigns.objects.filter(poster=user)
    return render(request , 'poster_campaigns.html' , {
        'campaigns':campaigns,
        'poster': user
    })


class campaign_viewsets(viewsets.ModelViewSet):
    queryset = Campaigns.objects.all()
    serializer_class = CampaignsSerializer
    permission_classes = (IsAuthenticated,)


