from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import EmployeeSerializer
import os
import pickle
import pandas as pd
import sklearn


#initialize models

file_path = os.path.join(os.path.dirname(__file__), 'attrition_prediction_model.pkl')
model = open(file_path,'rb')
attrition_model = pickle.load(model)
model.close()
file_path = os.path.join(os.path.dirname(__file__), 'preprocessing_pipeline.pkl')
model = open(file_path,'rb')
preprocessing_pipeline = pickle.load(model)
model.close()


class AttritionPrediction(APIView):
    def post(self, request):
        # Check if request data is a list
        if isinstance(request.data, list):
            serialized_list = []
            for data in request.data:
                # Serialize each data item
                serialized = EmployeeSerializer(data=data)
                serialized_list.append(serialized)

            # Check if all serialized data is valid
            if all(serialized.is_valid() for serialized in serialized_list):
                validated_data_list = [serialized.validated_data for serialized in serialized_list]

                # Convert validated data to a list of pandas DataFrames
                input_data_list = [pd.DataFrame(data, index=[0]) for data in validated_data_list]

                # Perform transformation for each input data
                input_transformed_list = [preprocessing_pipeline.transform(input_data) for input_data in input_data_list]

                # Make predictions for each input data
                output_list = [attrition_model.predict(input_transformed) for input_transformed in input_transformed_list]

                return Response(output_list, status=status.HTTP_200_OK)
            else:
                errors = [serialized.errors for serialized in serialized_list]
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # If request data is not a list, handle it as single input
            serialized = EmployeeSerializer(data=request.data)
            if serialized.is_valid():
                validated_data = serialized.validated_data
                
                # Convert validated data to a pandas DataFrame
                input_data = pd.DataFrame(validated_data, index=[0])  # Assuming single sample
                
                # Perform transformation
                input_transformed = preprocessing_pipeline.transform(input_data)
                
                # Make prediction
                output = attrition_model.predict(input_transformed)
                return Response(output, status=status.HTTP_200_OK)
            else:
                return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)