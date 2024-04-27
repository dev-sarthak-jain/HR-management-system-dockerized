# Generated by Django 5.0.4 on 2024-04-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attrition_prediction', '0003_employee_attrition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_data',
            name='appraisal_suggestion',
        ),
        migrations.AlterField(
            model_name='employee',
            name='Attrition',
            field=models.CharField(default='No', help_text="Attrition status: 'Yes' or 'No'", max_length=3),
        ),
    ]
