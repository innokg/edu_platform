from django.db import models


class Courses():
    title_of_courses = models.CharField(max_length=150, verbose_name='Название курса')
    dates_of_event = models.DateTimeField(auto_now_add=True, verbose_name='Дата проведения')
    mentor = models.CharField(max_length=255, verbose_name='Ментор')
    subthemes_id = models.ForeignKey('Subthemes', on_delete=models.CASCADE)
    lessons_block_id = models.ForeignKey('LessonsBlock', on_delete=models.CASCADE )
    lessons_list_id = models.ForeignKey('LessonsList', on_delete=models.CASCADE)
    hometasks_list_id = models.ForeignKey('Hometasks', on_delete=models.CASCADE)
    course_completion_rate = models.IntegerField(blank=True, verbose_name='Процент освоения темы')

class Subthemes():
    subtheme_title = models.CharField(max_length=255, verbose_name='Название подтемы')
    lessons = models.ForeignKey('Lesson', on_delete=models.PROTECT)
    comments = models.TextField(blank=True, verbose_name='Комментарии' )
    lessons_block_id = models.ForeignKey('LessonsBlock', on_delete=models.PROTECT)

class LessonsBlock():
    number_of_lessons = models.IntegerField(unique=True, verbose_name='Номер блока')
    lessons_title = models.CharField(max_length=250, verbose_name='Уроки')
    goals_at_the_end = models.TextField(blank=True, verbose_name='Цель по окончании')

class Lesson():
    motivation = models.TextField(blank=True, verbose_name='Мотивация')
    actualization = models.TextField(blank=True, verbose_name='Актуализация')
    new_theme = models.TextField(blank=True, verbose_name='Новая тема')
    reflection = models.TextField(blank=True, verbose_name='Рефлексия')
    comments = models.TextField(blank=True, verbose_name='Комментарии')
    date_of_lesson = models.DateTimeField(auto_now_add=True, verbose_name='Дата занятия')
    course_id = models.ForeignKey('Courses', on_delete=models.PROTECT)
    group = models.CharField(max_length=150, verbose_name='Название группы')
    lessons_block_id = models.ForeignKey('LessonsBlock',  on_delete=models.PROTECT)

class LessonsList():
    date_of_lesson = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    lesson = models.TextField(blank=True, verbose_name='Урок')
    lessons_list = models.CharField(max_length=255, verbose_name='Список занятий')


class Glossary():
    terms_blocks = models.CharField(max_length=250, verbose_name='Блок терминов')
    term = models.CharField(max_length=250, verbose_name='Термин')
    definition = models.TextField(blank=True, verbose_name='Определение')
    using = models.TextField(blank=True, verbose_name='Использование')
    lessons_id = models.ForeignKey('Lesson', on_delete=models.PROTECT)
    subtheme_id = models.ForeignKey('Subthemes', on_delete=models.PROTECT)


class Hometasks():
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    lessons_id = models.ForeignKey('Lesson', on_delete=models.PROTECT)
    topics = models.CharField(max_length=250, verbose_name='Темы')
    task = models.TextField(blank=True, verbose_name='Задание')

class Examination():
    date_of_exam = models.DateTimeField(auto_now_add=True, verbose_name='Дата экзамена')
    recomendations = models.TextField(blank=True, verbose_name='Общие рекомендации')
    execution_time = models.DateTimeField(auto_now_add=True, verbose_name='Время выполнения')
    lessonsblock_id = models.ForeignKey('LessonsBlock', on_delete=models.PROTECT)
    task = models.TextField(blank=True, verbose_name='Задание')
    solved_task = models.TextField(blank=True, verbose_name='Решенное задание')
    results = models.IntegerField(blank=True, verbose_name='Результаты')
