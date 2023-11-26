from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    last_update = models.DateTimeField()


class Category(models.Model):
    name = models.CharField(max_length=250)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=250)
    head_category = models.ManyToManyField(Category)

    class Meta:
        db_table = 'sub_categories'

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=250)
    about = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    categories = models.ManyToManyField(SubCategory)
    target_audience = models.CharField(max_length=200)
    course_thumbnail = models.FileField(upload_to='media/images/')
    trailer = models.FileField(upload_to='media/videos/')
    last_update = models.DateTimeField(default=timezone.now)


class CourseComment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)


class CourseStar(models.Model):
    STAR_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.PositiveIntegerField(choices=STAR_CHOICES)


# This is a bridge table between course and mentors
class MentorCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User is a mentor
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.course.title + ' -> ' + self.user.get_username()


class Modul(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.course.title + ' -> ' + self.title


class Lesson(models.Model):
    modul = models.ForeignKey(Modul, on_delete=models.CASCADE)
    video_location = models.FileField(upload_to='media/videos/')
    length = models.DurationField(default=timedelta(seconds=0))
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    thumbnail = models.FileField(upload_to='media/images/')

    def __str__(self):
        return f'{self.modul}'


class LessonComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField()


class LessonStar(models.Model):
    STAR_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.PositiveIntegerField(choices=STAR_CHOICES)

    def __str__(self):
        return f'{self.lesson} -> {self.star}'


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField()


# bridge table between transactions and courses
class TransactionCourse(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'transaction_courses'


class Enrolled(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.course


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Webinar(models.Model):
    CHOICES = (
        ('youtube', 'YouTube'),
        ('agora', 'Agora'),
    )
    title = models.CharField(max_length=250)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    trailer = models.FileField(upload_to='media/videos/')
    thumbnail = models.FileField(upload_to='media/images/')
    date = models.DateTimeField()
    start_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube = models.TextField()
    webinar_type = models.CharField(choices=CHOICES, max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.title
