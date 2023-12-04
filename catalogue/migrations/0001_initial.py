# Generated by Django 4.2.6 on 2023-12-03 15:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Course Name')),
                ('department', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True)),
                ('number', models.CharField(default='100', max_length=10, verbose_name='Course Number')),
                ('credits', models.CharField(default=3, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.IntegerField(blank=True, verbose_name='Course Number')),
                ('subject', models.CharField(max_length=255)),
                ('semester', models.CharField(max_length=30)),
                ('professor_id', models.CharField(max_length=255, verbose_name='Professor Name')),
                ('review', models.TextField(blank=True)),
                ('difficulty_rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Difficulty Rating')),
                ('workload_rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Workload Rating')),
                ('openness_rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Openness Rating')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=50, verbose_name='Semester')),
                ('session', models.CharField(max_length=25, verbose_name='Session')),
                ('offering_time', models.CharField(default='00:00:00', max_length=255)),
                ('delivery_type', models.CharField(max_length=255)),
                ('meeting_type', models.CharField(max_length=255)),
                ('crn', models.IntegerField()),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=50, verbose_name='Abbreviated semester, i.e. 202410')),
                ('friendly_name', models.CharField(max_length=255, verbose_name='Readable semester, i.e. Fall 2014')),
                ('readonly', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(default='name', max_length=50, verbose_name='Course')),
                ('original_location', models.FileField(upload_to='documents/')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.section')),
            ],
        ),
    ]
