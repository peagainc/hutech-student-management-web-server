# Generated by Django 3.1.3 on 2020-11-29 14:15

import backend.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activation',
            fields=[
                ('activation_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('activation_name', models.CharField(max_length=255)),
                ('date_time_start', models.DateField()),
                ('date_time_end', models.DateField()),
                ('staged_area', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(1, 'Enable'), (0, 'Disable')], default=1)),
                ('check_code', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('campus_id', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('campus_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('max_floor', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('classroom_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('floor', models.IntegerField()),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.campus')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('day_start', models.DateField()),
                ('day_end', models.DateField()),
                ('term', models.CharField(max_length=10)),
                ('status', models.IntegerField(choices=[(1, 'Enable'), (0, 'Disable')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=100)),
                ('phone_numer', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birthday', models.DateField(blank=True)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('profile_image', models.ImageField(upload_to=backend.models.upload_to_employee_profile)),
                ('self_code', models.CharField(blank=True, max_length=255)),
                ('encode', models.TextField(blank=True)),
                ('model_url', models.URLField(blank=True)),
                ('model_file', models.FileField(blank=True, upload_to=backend.models.upload_to_employee_face_model)),
                ('status', models.IntegerField(choices=[(1, 'Enable'), (0, 'Disable')], default=1)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.department')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_account', models.CharField(max_length=100)),
                ('err_title', models.CharField(max_length=100)),
                ('user_note', models.CharField(max_length=100)),
                ('log_file', models.FileField(upload_to=backend.models.upload_to_log)),
                ('report_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=255)),
                ('day_start', models.DateField()),
                ('day_end', models.DateField()),
                ('status', models.IntegerField(choices=[(1, 'Enable'), (0, 'Disable')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Lession',
            fields=[
                ('lession_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('check_code', models.CharField(blank=True, max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.course')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='ModelLink',
            fields=[
                ('train_model_id', models.AutoField(primary_key=True, serialize=False)),
                ('model_url', models.URLField(blank=True)),
                ('model_file', models.FileField(blank=True, upload_to=backend.models.upload_to_train_model)),
                ('update_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birthday', models.DateField(blank=True)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('profile_image', models.ImageField(upload_to=backend.models.upload_to_student_profile)),
                ('self_code', models.CharField(blank=True, max_length=100)),
                ('encode', models.TextField(blank=True)),
                ('model_url', models.URLField(blank=True)),
                ('model_file', models.FileField(blank=True, upload_to=backend.models.upload_to_student_face_model)),
                ('status', models.IntegerField(choices=[(1, 'Enable'), (0, 'Disable')], default=1)),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.class')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=100)),
                ('theory_credit', models.FloatField()),
                ('practice_credit', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('checkin_time', models.DateTimeField()),
                ('checkin_image', models.ImageField(upload_to=backend.models.upload_to_student_attendance)),
                ('checkin_method', models.CharField(max_length=10)),
                ('actual_location', models.CharField(max_length=100)),
                ('lession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.lession')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.student')),
            ],
        ),
        migrations.CreateModel(
            name='EventAttendance',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('checkin_time', models.DateTimeField()),
                ('checkin_image', models.ImageField(upload_to=backend.models.upload_to_student_attendance)),
                ('checkin_method', models.CharField(max_length=10)),
                ('actual_location', models.CharField(max_length=100)),
                ('activation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.activation')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.student')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeTimeSheet',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('checkin_time', models.DateTimeField(blank=True)),
                ('checkout_time', models.DateTimeField(blank=True)),
                ('checkin_image', models.ImageField(blank=True, upload_to=backend.models.upload_to_employee_attendance)),
                ('checkout_image', models.ImageField(blank=True, upload_to=backend.models.upload_to_employee_attendance)),
                ('status', models.IntegerField(choices=[(1, 'Is Check-in'), (2, 'Is Check-out')], default=1)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.employee')),
            ],
        ),
        migrations.CreateModel(
            name='CourseStudentDetail',
            fields=[
                ('coursedetail_id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.subject'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.employee'),
        ),
        migrations.AddField(
            model_name='class',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.department'),
        ),
        migrations.AddField(
            model_name='activation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.event'),
        ),
    ]
