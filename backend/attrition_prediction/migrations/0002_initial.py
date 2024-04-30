# Generated by Django 5.0.4 on 2024-04-30 04:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("attrition_prediction", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="chatmessage",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="employee_data",
            name="Employee_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="attrition_prediction.employee",
                verbose_name="Employee",
            ),
        ),
        migrations.AddField(
            model_name="transcript",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="chatmessage",
            name="transcript",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="attrition_prediction.transcript",
            ),
        ),
    ]