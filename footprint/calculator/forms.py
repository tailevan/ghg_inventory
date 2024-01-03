from django.forms import ModelForm
from .models import OfficeOperationForm

class OfficeOperationForm(ModelForm):
    class Meta:
        model = OfficeOperationForm
        fields = ["year","electricity", "water", "paper", "garbage", "commute"]
        labels = {
            "year" : "Year of report",
            "electricity" : "Amount of purchased electricity (kWh) per year",
            "water" : "Amount of purchased water (m3) per year",
            "paper" : "Amount of purchased paper (reams) per year",
            "garbage" : "Number of garbage bags per week",
            "commute" : "Total distance of commute (km) per year"
        }