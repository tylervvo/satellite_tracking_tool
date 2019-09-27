from django.urls import path

from . import views

urlpatterns = [
    path('', views.AnalysisList.as_view(), name='Analysis List'),
    path('create-analysis', views.AnalysisCreate.as_view(), name='new-analysis'),
]