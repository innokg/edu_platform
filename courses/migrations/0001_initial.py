# Generated by Django 4.0.3 on 2022-04-02 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_courses', models.CharField(max_length=150, unique=True, verbose_name='Название курса')),
                ('dates_of_event', models.DateField(verbose_name='Дата проведения')),
                ('mentor', models.CharField(max_length=255, verbose_name='Ментор')),
                ('course_completion_rate', models.IntegerField(blank=True, verbose_name='Процент освоения темы')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivation', models.TextField(blank=True, verbose_name='Мотивация')),
                ('actualization', models.TextField(blank=True, verbose_name='Актуализация')),
                ('new_theme', models.TextField(blank=True, verbose_name='Новая тема')),
                ('reflection', models.TextField(blank=True, verbose_name='Рефлексия')),
                ('comments', models.TextField(blank=True, verbose_name='Комментарии')),
                ('date_of_lesson', models.DateField(verbose_name='Дата занятия')),
                ('group', models.CharField(max_length=150, verbose_name='Название группы')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.courses')),
            ],
        ),
        migrations.CreateModel(
            name='LessonsBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_lessons', models.IntegerField(unique=True, verbose_name='Номер блока')),
                ('lessons_title', models.CharField(max_length=250, verbose_name='Уроки')),
                ('goals_at_the_end', models.TextField(blank=True, verbose_name='Цель по окончании')),
            ],
        ),
        migrations.CreateModel(
            name='LessonsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_lesson', models.DateField(verbose_name='Дата')),
                ('lesson', models.TextField(blank=True, verbose_name='Урок')),
                ('lessons_list', models.CharField(max_length=255, verbose_name='Список занятий')),
            ],
        ),
        migrations.CreateModel(
            name='Subthemes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtheme_title', models.CharField(max_length=255, verbose_name='Название подтемы')),
                ('comments', models.TextField(blank=True, verbose_name='Комментарии')),
                ('lessons_block_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.lessonsblock')),
                ('lessons_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.lesson')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='lessons_block_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.lessonsblock'),
        ),
        migrations.CreateModel(
            name='Hometasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_hometasks', models.DateField(verbose_name='Дата')),
                ('topics', models.CharField(max_length=250, verbose_name='Темы')),
                ('task', models.TextField(blank=True, verbose_name='Задание')),
                ('lessons_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Glossary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_blocks', models.CharField(max_length=250, verbose_name='Блок терминов')),
                ('term', models.CharField(max_length=250, verbose_name='Термин')),
                ('definition', models.TextField(blank=True, verbose_name='Определение')),
                ('using', models.TextField(blank=True, verbose_name='Использование')),
                ('lessons_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.lesson')),
                ('subtheme_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.subthemes')),
            ],
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_exam', models.DateField(verbose_name='Дата экзамена')),
                ('recomendations', models.TextField(blank=True, verbose_name='Общие рекомендации')),
                ('execution_time', models.DateField(verbose_name='Время выполнения')),
                ('task', models.TextField(blank=True, verbose_name='Задание')),
                ('solved_task', models.TextField(blank=True, verbose_name='Решенное задание')),
                ('results', models.IntegerField(blank=True, verbose_name='Результаты')),
                ('lessonsblock_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.lessonsblock')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='hometasks_list_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='courses.hometasks', verbose_name='Список ДЗ'),
        ),
        migrations.AddField(
            model_name='courses',
            name='lessons_block_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='courses.lessonsblock', verbose_name='Блок занятий'),
        ),
        migrations.AddField(
            model_name='courses',
            name='lessons_list_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='courses.lessonslist', verbose_name='Список уроков'),
        ),
        migrations.AddField(
            model_name='courses',
            name='subthemes_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='courses.subthemes', verbose_name='Подтемы'),
        ),
    ]
