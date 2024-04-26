from django.urls import path
from . import views


urlpatterns = [
    path("attrition_prediction/", views.AttritionPrediction.as_view(), name="all-transcripts"),
]