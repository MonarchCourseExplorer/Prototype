# Generated by Django 4.2.6 on 2023-12-05 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_remove_feedback_professor_remove_feedback_section_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='professor_id',
        ),
    ]
