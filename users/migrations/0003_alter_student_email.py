# Generated by Django 4.2.6 on 2023-11-04 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_professor_email_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default='user@odu.edu', max_length=254),
        ),
    ]