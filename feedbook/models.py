from django.core import validators
from django.db import models
from django.utils import timezone


class BookData(models.Model):
    #book_id = models.CharField(max_length=20)
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    CHOICE_GENRE = (
        ('1', 'Language'),
        ('2', 'Math'),
        ('3', 'Others'),
    )
    genre = models.CharField(max_length=1, choices=CHOICE_GENRE)
    published_company = models.CharField(max_length=20)
    published_year = models.CharField(
        max_length=4,
        validators=[validators.RegexValidator(regex='(19[0-9]{2}|20[0-9]{2})')],
        )
    memo = models.TextField(max_length=300, blank=True, null=True)
    registered_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class BookRequest(models.Model):
    #unique_id = models.CharField(max_length=20)
    book = models.ForeignKey('BookData', on_delete=models.PROTECT)
    student = models.ForeignKey('Student', on_delete=models.PROTECT)
    CHOICE_REQUEST_STATUS = (
        ('1', 'Requested'),
        ('2', 'Offered'),
        ('3', 'Settled'),
        ('4', 'canceled'),
    )
    status = models.CharField(max_length=1, choices=CHOICE_REQUEST_STATUS)
    request_date = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.book.title


class Student(models.Model):
    student_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(blank=False, null=False)
    memo = models.TextField(max_length=300, blank=True, null=True)
    registered_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Donor(models.Model):
    donor_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(blank=False, null=False)
    memo = models.TextField(max_length=300, blank=True, null=True)
    registered_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
