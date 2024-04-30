from django.db import models
from user.models import User
import uuid

class Employee(models.Model):
    Employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Attrition = models.CharField(max_length=3, default='No', help_text="Attrition status: 'Yes' or 'No'")
    Age = models.IntegerField()
    BusinessTravel = models.CharField(max_length=50)
    DailyRate = models.IntegerField()
    Department = models.CharField(max_length=100)
    DistanceFromHome = models.IntegerField()
    Education = models.IntegerField()
    EducationField = models.CharField(max_length=50)
    EmployeeCount = models.IntegerField()
    EmployeeNumber = models.IntegerField()
    EnvironmentSatisfaction = models.IntegerField()
    Gender = models.CharField(max_length=10)
    HourlyRate = models.IntegerField()
    JobInvolvement = models.IntegerField()
    JobLevel = models.IntegerField()
    JobRole = models.CharField(max_length=100)
    JobSatisfaction = models.IntegerField()
    MaritalStatus = models.CharField(max_length=20)
    MonthlyIncome = models.IntegerField()
    MonthlyRate = models.IntegerField()
    NumCompaniesWorked = models.IntegerField()
    Over18 = models.CharField(max_length=5)
    OverTime = models.CharField(max_length=10)
    PercentSalaryHike = models.IntegerField()
    PerformanceRating = models.IntegerField()
    RelationshipSatisfaction = models.IntegerField()
    StandardHours = models.IntegerField()
    StockOptionLevel = models.IntegerField()
    TotalWorkingYears = models.IntegerField()
    TrainingTimesLastYear = models.IntegerField()
    WorkLifeBalance = models.IntegerField()
    YearsAtCompany = models.IntegerField()
    YearsInCurrentRole = models.IntegerField()
    YearsSinceLastPromotion = models.IntegerField()
    YearsWithCurrManager = models.IntegerField()
    Name = models.CharField(max_length=100)

class Employee_Data(models.Model):
    Employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Employee")
    Attrition_prediction = models.BooleanField(default=False)
    Appraisal_suggestion = models.FloatField()

class Transcript(models.Model):
    transcript_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transcript {self.transcript_id} by {self.user.email}"


class ChatMessage(models.Model):
    chat_id = models.AutoField(primary_key=True)
    transcript = models.ForeignKey(Transcript, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # Specify a default value
    user_response = models.TextField()
    ai_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat Message {self.chat_id}"