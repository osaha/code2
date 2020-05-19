from django.contrib import admin
from .models import BookData, Student, Donor, BookRequest

admin.site.register(BookData)
admin.site.register(Student)
admin.site.register(Donor)
admin.site.register(BookRequest)
