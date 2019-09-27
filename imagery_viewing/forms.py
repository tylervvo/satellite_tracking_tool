from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Analysis

class AnalysisCreateForm(forms.ModelForm):

    class Meta:
        model = Analysis
        fields = (
	        'north_east_long',
			'north_east_lat',
			'south_west_long',
			'south_west_lat',
			'start_date',
			'end_date',
			'frequency',
			'type_analysis',
		)
