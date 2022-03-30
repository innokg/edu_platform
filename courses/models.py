"""
standart models for educational project
"""
from django.db import models


class Courses(models.Model):
    """Class for courses"""
    title_of_courses = models.CharField(
        max_length=150,
        verbose_name='Название курса',
        unique=True)
    dates_of_event = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата проведения')
    mentor = models.CharField(
        max_length=255,
        verbose_name='Ментор')
    subthemes_id = models.ForeignKey(
        'Subthemes',
        on_delete=models.CASCADE,
        verbose_name='Подтемы',
        blank=True, null=True)
    lessons_block_id = models.ForeignKey(
        'LessonsBlock',
        on_delete=models.CASCADE,
        verbose_name='Блок занятий',
        blank=True, null=True)
    lessons_list_id = models.ForeignKey(
        'LessonsList',
        on_delete=models.CASCADE,
        verbose_name='Список уроков',
        blank=True, null=True)
    hometasks_list_id = models.ForeignKey(
        'Hometasks',
        on_delete=models.CASCADE,
        verbose_name='Список ДЗ',
        blank=True, null=True)
    course_completion_rate = models.IntegerField(
        blank=True,
        verbose_name='Процент освоения темы')
    objects = models.Manager()


class Subthemes(models.Model):
    """Class for subthemes of courses"""
    subtheme_title = models.CharField(
        max_length=255,
        verbose_name='Название подтемы')
    lessons_id = models.ForeignKey(
        'Lesson',
        on_delete=models.PROTECT)
    comments = models.TextField(
        blank=True,
        verbose_name='Комментарии')
    lessons_block_id = models.ForeignKey(
        'LessonsBlock',
        on_delete=models.PROTECT)


class LessonsBlock(models.Model):
    """Class for block of lessons"""
    number_of_lessons = models.IntegerField(
        unique=True,
        verbose_name='Номер блока')
    lessons_title = models.CharField(
        max_length=250,
        verbose_name='Уроки')
    goals_at_the_end = models.TextField(
        blank=True,
        verbose_name='Цель по окончании')


class Lesson(models.Model):
    """Class for Lessons"""
    motivation = models.TextField(
        blank=True,
        verbose_name='Мотивация')
    actualization = models.TextField(
        blank=True,
        verbose_name='Актуализация')
    new_theme = models.TextField(
        blank=True,
        verbose_name='Новая тема')
    reflection = models.TextField(
        blank=True,
        verbose_name='Рефлексия')
    comments = models.TextField(
        blank=True,
        verbose_name='Комментарии')
    date_of_lesson = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата занятия')
    course_id = models.ForeignKey(
        'Courses',
        on_delete=models.PROTECT)
    group = models.CharField(
        max_length=150,
        verbose_name='Название группы')
    lessons_block_id = models.ForeignKey(
        'LessonsBlock',
        on_delete=models.PROTECT)


class LessonsList(models.Model):
    """Class for list of lessons"""
    date_of_lesson = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата')
    lesson = models.TextField(
        blank=True,
        verbose_name='Урок')
    lessons_list = models.CharField(
        max_length=255,
        verbose_name='Список занятий')


class Glossary(models.Model):
    """Class for lessons list"""
    terms_blocks = models.CharField(
        max_length=250,
        verbose_name='Блок терминов')
    term = models.CharField(
        max_length=250,
        verbose_name='Термин')
    definition = models.TextField(
        blank=True,
        verbose_name='Определение')
    using = models.TextField(
        blank=True,
        verbose_name='Использование')
    lessons_id = models.ForeignKey(
        'Lesson',
        on_delete=models.PROTECT)
    subtheme_id = models.ForeignKey(
        'Subthemes',
        on_delete=models.PROTECT)


class Hometasks(models.Model):
    """Class for hometasks"""
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата')
    lessons_id = models.ForeignKey(
        'Lesson',
        on_delete=models.PROTECT)
    topics = models.CharField(
        max_length=250,
        verbose_name='Темы')
    task = models.TextField(
        blank=True,
        verbose_name='Задание')


class Examination(models.Model):
    """Class for exams"""
    date_of_exam = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата экзамена')
    recomendations = models.TextField(
        blank=True,
        verbose_name='Общие рекомендации')
    execution_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время выполнения')
    lessonsblock_id = models.ForeignKey(
        'LessonsBlock',
        on_delete=models.PROTECT)
    task = models.TextField(
        blank=True,
        verbose_name='Задание')
    solved_task = models.TextField(
        blank=True,
        verbose_name='Решенное задание')
    results = models.IntegerField(
        blank=True,
        verbose_name='Результаты')
