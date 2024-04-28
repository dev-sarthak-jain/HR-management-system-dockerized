from django.urls import path
from . import views


urlpatterns = [
    #path("attrition_prediction/", views.AttritionPrediction.as_view(), name="all-transcripts"),
    path("streamlit_test/", views.Streamlit_test.as_view(), name="Streamlit_test"),
    path('employee_create/', views.EmployeeCreateAPIView.as_view(), name='employee-create'),
]