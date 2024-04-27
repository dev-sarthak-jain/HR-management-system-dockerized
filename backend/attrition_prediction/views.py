from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import EmployeeSerializer, EmployeeDataSerializer
import os
import pickle
import pandas as pd
from rest_framework import generics
from django.db import transaction

#initialize models

file_path = os.path.join(os.path.dirname(__file__), 'AI_models', 'attrition_model', 'attrition_prediction_model.pkl')
model = open(file_path,'rb')
attrition_model = pickle.load(model)
model.close()
file_path = os.path.join(os.path.dirname(__file__), 'AI_models', 'attrition_model', 'preprocessing_pipeline_attrition.pkl')
model = open(file_path,'rb')
preprocessing_pipeline = pickle.load(model)
model.close()

class Streamlit_test(APIView):
    def post(self, request):
        data=request.data
        return Response(data, status=status.HTTP_200_OK)

def AttritionPredictionFunction(data):
    input_transformed = preprocessing_pipeline.transform(data)
    output = attrition_model.predict(input_transformed)
    return {"Attrition_prediction":output[0]}

class AttritionPrediction(APIView):
    def post(self, request):
        if isinstance(request.data, list):
            serialized_list = []
            for data in request.data:
                serialized = EmployeeSerializer(data=data)
                serialized_list.append(serialized)
            if all(serialized.is_valid() for serialized in serialized_list):
                validated_data_list = [serialized.validated_data for serialized in serialized_list]
                input_data_list = [pd.DataFrame(data, index=[0]) for data in validated_data_list]

                # Extract names and drop the 'name' column for each DataFrame
                name_columns = [df.pop('name') for df in input_data_list]  # This modifies input_data_list in-place

                input_transformed_list = [preprocessing_pipeline.transform(input_data) for input_data in input_data_list]
                output_list = [attrition_model.predict(input_transformed) for input_transformed in input_transformed_list]
                
                # Combine name and output into a single list of results
                results = [{'name': name, 'attrition prediction': output.tolist()} for name, output in zip(name_columns, output_list)]
                
                return Response(results, status=status.HTTP_200_OK)
            else:
                errors = [serialized.errors for serialized in serialized_list]
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serialized = EmployeeSerializer(data=request.data)
            if serialized.is_valid():
                validated_data = serialized.validated_data
                input_data = pd.DataFrame(validated_data, index=[0])
                
                # Extract name and drop from DataFrame
                name_column = input_data.pop('name')
                
                input_transformed = preprocessing_pipeline.transform(input_data)
                output = attrition_model.predict(input_transformed)
                
                result = {'name': name_column.iloc[0], 'attrition prediction': output.tolist()}
                
                return Response(result, status=status.HTTP_200_OK)
            else:
                return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeCreateAPIView(generics.GenericAPIView):
    def post(self, request):
        Employee_data = EmployeeSerializer(data=request.data, many ='True')
        if Employee_data.is_valid():
            Employee_data.save()
            data = Employee_data.data
            for i in data:
                emp_id = i['Employee_id']
                del i['Attrition']
                del i['Employee_id']
                del i['Name']
                input_data = pd.DataFrame([i])
                new_data = AttritionPredictionFunction(input_data)
                new_data['Employee_id'] = emp_id
                new_data = EmployeeDataSerializer(data=new_data)
                if new_data.is_valid():
                    new_data.save()
            return Response("Saved", status=status.HTTP_201_CREATED)
        else:
            return Response("Not Saved", status=status.HTTP_400_BAD_REQUEST)