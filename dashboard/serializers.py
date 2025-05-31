from rest_framework import serializers
from campaigns.models import Campaigns

class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = ('name' , 'start_date' , 'budget')