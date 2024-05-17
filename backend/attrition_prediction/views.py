from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
import os
import pickle
import pandas as pd
from rest_framework import generics
from django.db import transaction
from .Func1_chatResponse import generate_response
from .Func2_titleGeneration import generate_chat_title

#initialize models

file_path = os.path.join(os.path.dirname(__file__), 'AI_models', 'attrition_model', 'attrition_prediction_model.pkl')
model = open(file_path,'rb')
attrition_model = pickle.load(model)
model.close()
file_path = os.path.join(os.path.dirname(__file__), 'AI_models', 'attrition_model', 'preprocessing_pipeline_attrition.pkl')
model = open(file_path,'rb')
preprocessing_pipeline_attrition = pickle.load(model)
model.close()
file_path = os.path.join(os.path.dirname(__file__), 'AI_models', 'prediction_model', 'appraisal_prediction_model.pkl')
model = open(file_path,'rb')
appraisal_model = pickle.load(model)
model.close()
file_path = os.path.join(os.path.dirname(__file__), 'AI_models', 'prediction_model', 'preprocessing_pipeline_appraisal.pkl')
model = open(file_path,'rb')
preprocessing_pipeline_appraisal = pickle.load(model)
model.close()

class Streamlit_test(APIView):
    def post(self, request):
        data=request.data
        return Response(data, status=status.HTTP_200_OK)

def AttritionPredictionFunction(data):
    input_data = pd.DataFrame([data])
    input_transformed = preprocessing_pipeline_attrition.transform(input_data)
    output = attrition_model.predict(input_transformed)
    return output[0]

def AppraisalPredictionFunction(data):
    input_data = pd.DataFrame([data])
    input_transformed = preprocessing_pipeline_appraisal.transform(input_data)
    output = appraisal_model.predict(input_transformed)
    return output[0]

class EmployeeCreateAPIView(generics.GenericAPIView):
    def post(self, request):
        Employee_data = EmployeeSerializer(data=request.data, many ='True')
        print(Employee_Data)
        if Employee_data.is_valid():
            Employee_data.save()
            data = Employee_data.data
            for i in data:
                dict = {
                "Employee_id":i["Employee_id"],
                "Attrition_prediction" : AttritionPredictionFunction(i),
                "Appraisal_suggestion" : AppraisalPredictionFunction(i)
                }
                new_data = EmployeeDataSerializer(data=dict)
                if new_data.is_valid():
                    new_data.save()
            return Response("Saved", status=status.HTTP_201_CREATED)
        else:
            return Response("Not Saved", status=status.HTTP_400_BAD_REQUEST)        

class Transcription(APIView):
    def post(self, request):
        serialized_transcript = TranscriptSerializer(data=request.data)
        if serialized_transcript.is_valid():
            serialized_transcript.save()
            return Response(serialized_transcript.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_transcript.errors, status=status.HTTP_400_BAD_REQUEST)

class AllTranscripts(APIView):
    def get(self, request, user_id):
        # Retrieve all transcripts for the given user
        user_transcripts = Transcript.objects.filter(user_id=user_id)

        # Serialize and return the transcripts
        serializer = TranscriptSerializer(user_transcripts, many=True)
        return Response(serializer.data)


class GenerateUpdateTitle(APIView):
    def post(self, request, transcript_id):
        # Get the transcript object or return a 404 if not found
        transcript = get_object_or_404(Transcript, transcript_id=transcript_id)
        # Extract the title from the request data (assuming it's provided by the frontend)
        provided_title = request.data.get('title')
        # Generate a new title using your custom function (replace with your actual logic)
        generated_title = generate_chat_title(provided_title)
        # Update the transcript with the new title
        transcript.title = generated_title
        transcript.save()
        serializer = TranscriptSerializer(transcript)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, transcript_id):
        # Get the transcript object or return a 404 if not found
        transcript = get_object_or_404(Transcript, transcript_id=transcript_id)

        # Extract the new title from the request data
        new_title = request.data.get('title')

        # Update the title and save the transcript
        transcript.title = new_title
        transcript.save()

        # Return a response indicating success
        return Response({"message": "Transcript title updated successfully"}, status=status.HTTP_200_OK)


class CreateMessages(APIView):
    def get(self, request, transcript_id):
        # Get the transcript object or return a 404 if not found
        transcript = get_object_or_404(Transcript, pk=transcript_id)

        # Retrieve all messages of a particular transcript
        user_messages = ChatMessage.objects.filter(transcript=transcript_id)


        # Serialize and return the messages
        serializer = ChatMessagesSerializer(user_messages, many=True)
        return Response(serializer.data)

    def post(self, request, transcript_id):
        # Get the transcript object or return a 404 if not found
        transcript = get_object_or_404(Transcript, pk=transcript_id)
        transcript_id2 = transcript.transcript_id

        messages = ChatMessage.objects.filter(transcript=transcript_id2).order_by('timestamp')
        message_data = [{"user":message.user_response,"AI":message.ai_response} for message in messages]
    #     # message_data ={'user_response': 'Hello', 'user': 2, "AI": "Answer 1"}
    #     message_data = [
    #     {"user": "Hello", "AI": "Answer 1"},
    #     {"user": "Query 2", "AI": "Answer 2"},
    #     {"user": "Query 3", "AI": "Answer 3"}
    # ]

        # Extract user_response from the request data (adjust based on your request structure)
        user_response = request.data.get('user_response')

        user_id = request.data.get('user')
        user = get_object_or_404(User, id=user_id)



        # Generate AI response based on user input
        ######ai_response = llm_response(user_response)


        ai_response = generate_response(question=user_response, past_convo = message_data)
        # print(f"fther {user} {ai_response}")
        print(ai_response)
        chat_message = ChatMessage.objects.create(
            transcript=transcript,
            user=user,
            user_response=user_response,
            ai_response=ai_response
        )

        chat_message.save()
        serializer = ChatMessagesSerializer(chat_message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, transcript_id):
        transcript = get_object_or_404(Transcript, pk=transcript_id)
        transcript.delete()
        return Response({"message": "Transcript deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
