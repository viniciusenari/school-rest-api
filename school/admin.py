from django.contrib import admin
from school.models import Student, Course

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'birthday')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_id', 'description')
    list_display_links = ('id', 'course_id')
    search_fields = ('course_id',)

admin.site.register(Course, Courses)