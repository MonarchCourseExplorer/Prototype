# Generated by Django 4.2.6 on 2023-12-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='is_professor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='is_professor',
            field=models.BooleanField(default=False),
        ),
    ]
