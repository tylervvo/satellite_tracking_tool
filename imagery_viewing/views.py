from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, View, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView

from .models import Analysis
from .forms import AnalysisCreateForm
from django.views.generic import ListView, DetailView, FormView, View

# import pyrebase

# firebaseConfig = {
#   'apiKey': "AIzaSyCbNY_L1OzSB5wPB981J64qxFKTqM3K9RU",
#   'authDomain': "satellite-mapping-standalone.firebaseapp.com",
#   'databaseURL': "https://satellite-mapping-standalone.firebaseio.com",
#   'projectId': "satellite-mapping-standalone",
#   'storageBucket': "satellite-mapping-standalone.appspot.com",
#   'messagingSenderId': "470637696129",
#   'appId': "1:470637696129:web:24555fc15cd9a087"
# }

# firebase = pyrebase.initialize_app(firebaseConfig)
# storage = firebase.storage()

class AnalysisList(ListView):
	model = Analysis


class AnalysisCreate(CreateView):
    model = Analysis
    template_name = 'imagery_viewing/new_analysis.html'
    form_class = AnalysisCreateForm

    def get(self, request, *args, **kwargs):
        context = {'form': AnalysisCreateForm()}
        return render(request, 'imagery_viewing/new_analysis.html', context)

    def form_valid(self, form):
	    self.object = form.save()
	    return HttpResponseRedirect('/')

 # display_images(View):
	# ref = storage.child('images/AC.png')
	# def get(self,request):
	# 	return render(request, 'main.html', {'image': ref.getDownloadURL()})



