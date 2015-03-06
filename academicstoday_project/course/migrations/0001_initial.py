# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=31)),
                ('body', models.TextField()),
                ('post_date', models.DateField(null=True, auto_now_add=True, auto_now=True)),
            ],
            options={
                'db_table': 'at_announcements',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('course_id', models.PositiveIntegerField()),
                ('order_num', models.PositiveSmallIntegerField(default=0)),
                ('type', models.PositiveSmallIntegerField()),
                ('due_date', models.DateField(null=True)),
            ],
            options={
                'db_table': 'at_assignments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssignmentReview',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('student_id', models.BigIntegerField()),
                ('assignment_id', models.PositiveIntegerField()),
                ('course_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=31)),
                ('comment', models.TextField()),
                ('marks', models.PositiveSmallIntegerField(default=0)),
                ('post_date', models.DateField(null=True, auto_now_add=True, auto_now=True)),
            ],
            options={
                'db_table': 'at_assignment_reviews',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssignmentSubmission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('assignment_id', models.PositiveIntegerField()),
                ('student_id', models.BigIntegerField()),
                ('course_id', models.PositiveIntegerField()),
                ('order_num', models.PositiveSmallIntegerField(default=0)),
                ('type', models.PositiveSmallIntegerField()),
                ('marks', models.PositiveSmallIntegerField(default=0)),
                ('submission_date', models.DateField(null=True)),
                ('is_marked', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'at_assignment_submissions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('image_filename', models.CharField(max_length=31)),
                ('title', models.CharField(max_length=63)),
                ('sub_title', models.CharField(max_length=127)),
                ('category', models.CharField(max_length=31)),
                ('description', models.TextField()),
                ('start_date', models.DateField(null=True)),
                ('finish_date', models.DateField(null=True)),
                ('is_official', models.BooleanField(default=False)),
                ('is_available', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'at_courses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EssayQuestion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('assignment_id', models.PositiveIntegerField()),
                ('course_id', models.PositiveIntegerField()),
                ('question_num', models.PositiveSmallIntegerField()),
                ('title', models.CharField(default='', max_length=31)),
                ('description', models.TextField(default='')),
            ],
            options={
                'db_table': 'at_essay_questions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EssaySubmission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('assignment_id', models.BigIntegerField()),
                ('student_id', models.BigIntegerField()),
                ('course_id', models.PositiveIntegerField()),
                ('file', models.FileField(upload_to='uploads')),
                ('submission_date', models.DateTimeField(null=True, auto_now_add=True, auto_now=True)),
                ('is_marked', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'at_essay_submissions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('course_id', models.PositiveIntegerField()),
                ('order_num', models.PositiveSmallIntegerField(default=0)),
                ('type', models.PositiveSmallIntegerField()),
                ('start_date', models.DateField(null=True)),
                ('due_date', models.DateField(null=True)),
            ],
            options={
                'db_table': 'at_exams',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExamSubmission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('exam_id', models.PositiveIntegerField()),
                ('student_id', models.BigIntegerField()),
                ('course_id', models.PositiveIntegerField()),
                ('order_num', models.PositiveSmallIntegerField(default=0)),
                ('type', models.PositiveSmallIntegerField()),
                ('marks', models.PositiveSmallIntegerField(default=0)),
                ('submission_date', models.DateField(null=True)),
                ('is_marked', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'at_exam_submissions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('course_id', models.PositiveIntegerField()),
                ('week_num', models.PositiveSmallIntegerField(max_length=7)),
                ('lecture_num', models.PositiveSmallIntegerField(default=0, max_length=7)),
                ('title', models.CharField(null=True, default='', max_length=31)),
                ('description', models.TextField(null=True, default='')),
                ('youtube_url', models.URLField(null=True, default='')),
                ('vimeo_url', models.URLField(null=True, default='')),
                ('bliptv_url', models.URLField(null=True, default='')),
                ('preferred_service', models.CharField(max_length=31)),
            ],
            options={
                'db_table': 'at_lectures',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('exam_id', models.PositiveIntegerField(default=0)),
                ('assignment_id', models.PositiveIntegerField()),
                ('course_id', models.PositiveIntegerField()),
                ('question_num', models.PositiveSmallIntegerField()),
                ('title', models.CharField(default='', max_length=31)),
                ('description', models.TextField(default='')),
                ('json_choices', models.CharField(default='{}', max_length=1055)),
                ('json_answers', models.CharField(default='{}', max_length=127)),
            ],
            options={
                'db_table': 'at_multiple_choice_questions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MultipleChoiceSubmission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('student_id', models.BigIntegerField()),
                ('assignment_id', models.PositiveIntegerField()),
                ('exam_id', models.PositiveIntegerField(default=0)),
                ('course_id', models.PositiveIntegerField()),
                ('question_num', models.PositiveSmallIntegerField(default=0)),
                ('json_answers', models.CharField(default='{}', max_length=127)),
                ('marks', models.PositiveSmallIntegerField(default=0)),
                ('submission_date', models.DateTimeField(null=True, auto_now_add=True, auto_now=True)),
                ('is_marked', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'at_multiple_choice_submissions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('course_id', models.PositiveIntegerField()),
                ('url', models.URLField(default='')),
            ],
            options={
                'db_table': 'at_policys',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('course_id', models.PositiveIntegerField()),
                ('order_num', models.PositiveSmallIntegerField(default=0)),
                ('type', models.PositiveSmallIntegerField()),
                ('due_date', models.DateField(null=True)),
            ],
            options={
                'db_table': 'at_quizzes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuizSubmission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('quiz_id', models.PositiveIntegerField()),
                ('student_id', models.BigIntegerField()),
                ('course_id', models.PositiveIntegerField()),
                ('order_num', models.PositiveSmallIntegerField(default=0)),
                ('type', models.PositiveSmallIntegerField()),
                ('marks', models.PositiveSmallIntegerField(default=0)),
                ('submission_date', models.DateField(null=True)),
                ('is_marked', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'at_quiz_submissions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResponseQuestion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('assignment_id', models.PositiveIntegerField()),
                ('course_id', models.PositiveIntegerField()),
                ('question_num', models.PositiveSmallIntegerField()),
                ('title', models.CharField(default='', max_length=31)),
                ('description', models.TextField(default='')),
                ('answer', models.TextField(default='')),
            ],
            options={
                'db_table': 'at_response_questions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResponseSubmission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('student_id', models.BigIntegerField()),
                ('assignment_id', models.PositiveIntegerField()),
                ('course_id', models.PositiveIntegerField()),
                ('question_num', models.PositiveSmallIntegerField(default=0)),
                ('answer', models.TextField(default='')),
                ('marks', models.PositiveSmallIntegerField(default=0)),
                ('submission_date', models.DateTimeField(null=True, auto_now_add=True, auto_now=True)),
                ('is_marked', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'at_response_submissions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('courses', models.ManyToManyField(to='course.Course')),
            ],
            options={
                'db_table': 'at_students',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('course_id', models.PositiveIntegerField()),
                ('url', models.URLField(default='')),
            ],
            options={
                'db_table': 'at_syllabus',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('courses', models.ManyToManyField(to='course.Course')),
            ],
            options={
                'db_table': 'at_teachers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrueFalseQuestion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('assignment_id', models.PositiveIntegerField(default=0)),
                ('quiz_id', models.PositiveIntegerField(default=0)),
                ('course_id', models.PositiveIntegerField()),
                ('question_num', models.PositiveSmallIntegerField()),
                ('title', models.CharField(default='', max_length=31)),
                ('description', models.TextField(default='')),
                ('true_choice', models.CharField(null=True, max_length=127)),
                ('false_choice', models.CharField(null=True, max_length=127)),
                ('answer', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'at_true_false_questions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrueFalseSubmission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('student_id', models.BigIntegerField()),
                ('assignment_id', models.PositiveIntegerField(default=0)),
                ('quiz_id', models.PositiveIntegerField(default=0)),
                ('course_id', models.PositiveIntegerField()),
                ('question_num', models.PositiveSmallIntegerField(default=0)),
                ('answer', models.BooleanField(default=False)),
                ('marks', models.PositiveSmallIntegerField(default=0)),
                ('submission_date', models.DateTimeField(null=True, auto_now_add=True, auto_now=True)),
                ('is_marked', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'at_true_false_submissions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, max_length=11)),
                ('course_id', models.PositiveIntegerField()),
                ('week_num', models.PositiveSmallIntegerField(max_length=7)),
                ('title', models.CharField(max_length=31)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'at_weeks',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='announcement',
            name='courses',
            field=models.ManyToManyField(to='course.Course'),
            preserve_default=True,
        ),
    ]