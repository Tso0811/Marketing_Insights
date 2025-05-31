from django.shortcuts import render
from campaigns.models import Campaigns
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404 ,redirect

from .serializers import CampaignsSerializer
from rest_framework import viewsets
# Create your views here.

def show_campaigns(request):    #直接在dashboard中顯示 不需要點擊進入細節
    campaign = Campaigns.objects.all()
    return render(request , 'dashboard.html' , {'campaigns':campaign})

@login_required
def edit_campaigns(request , id):
    campaign = get_object_or_404(Campaigns , pk=id)
    if request.method == 'POST':
        new_name = request.POST['name']
        new_start_date = request.POST['start_date']
        new_budget = request.POST['budget']

        campaign.name = new_name
        campaign.start_date = new_start_date
        campaign.budget = new_budget

        campaign.save()

        return redirect('dashboard:show_campaigns')

    return render(request, 'campaign_form.html', {'campaign': campaign})

@login_required
def campaign_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        start_date = request.POST.get('start_date')
        budget = request.POST.get('budget')

        new_campaign = Campaigns(name=name , start_date=start_date , budget=budget)
        new_campaign.save()

        return redirect('dashboard:show_campaigns')

    return render(request , 'campaign_form.html')

@login_required
def campaign_delete (request , id):
    campaign = get_object_or_404(Campaigns , pk=id)
    if request.method == 'POST':
        campaign.delete()
        return redirect('dashboard:show_campaigns')
    return render(request , 'campaign_delete.html' , {'campaign':campaign})

@login_required
def campaign_click (request , id):
    campaign = get_object_or_404(Campaigns , pk = id)
    campaign.click += 1
    campaign.save()
    return redirect('dashboard:show_campaigns')

class campaign_viewsets(viewsets.ModelViewSet):
    queryset = Campaigns.objects.all()
    serializer_class = CampaignsSerializer