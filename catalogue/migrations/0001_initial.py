
# Generated by Django 4.2.6 on 2023-11-29 02:04





from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [


        ('users', '0003_alter_student_email'),
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
            name='recQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionsText', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(

            name='Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrginalLocation', models.FileField(upload_to='documents/')),
                ('NormalizedLocation', models.CharField(max_length=120, verbose_name='Normalized Location')),

            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=50, verbose_name='Semester')),
                ('session', models.CharField(max_length=25, verbose_name='Session')),
                ('offering_time', models.CharField(default='00:00:00', max_length=255)),
                ('delivery_type', models.CharField(max_length=25)),
                ('meeting_type', models.CharField(max_length=25)),
                ('crn', models.IntegerField()),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.professor')),
            ],
        ),
        migrations.CreateModel(

            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Review', models.TextField(blank=True)),
                ('Rating', models.IntegerField(blank=True)),
                ('ProfessorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.professor')),



         

            ],
        ),
    ]
