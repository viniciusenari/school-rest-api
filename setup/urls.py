"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CoursesViewSet, EnrollmentsViewSet, EnrollmentStudentList, StudentsEnrolledList
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('enrollments', EnrollmentsViewSet, basename='Enrollments')

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('management_page/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/enrollments/', EnrollmentStudentList.as_view()),
    path('courses/<int:pk>/enrollments/', StudentsEnrolledList.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
