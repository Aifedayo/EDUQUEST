# Generated by Django 4.0.5 on 2022-06-05 05:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('eduquestapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answercomment',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
    ]
