# Generated by Django 4.2.6 on 2023-12-01 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_remove_feedback_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='professor_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='section_id',
            field=models.IntegerField(blank=True),
        ),
    ]