from django.urls import path
from . import views


urlpatterns = [
    path("all-transcripts/", views.AllTranscripts.as_view(), name="all-transcripts"),
    path("create-messages/<transcript_id>/", views.CreateMessages.as_view(), name="create-messages"),
    path("transcription/", views.Transcription.as_view(), name="transcription"),
    path('generate-update-title/<uuid:transcript_id>/', views.GenerateUpdateTitle.as_view(), name='generate-update-title'), 
    path("streamlit_test/", views.Streamlit_test.as_view(), name="Streamlit_test"),
    path('employee_create/', views.EmployeeCreateAPIView.as_view(), name='employee-create'),
]