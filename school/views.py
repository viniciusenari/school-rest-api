from rest_framework import viewsets, generics
from school.models import Student, Course, Enrollment
from school.serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer, EnrollmentStudentListSerializer, StudentsEnrolledListSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentsViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentStudentList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = EnrollmentStudentListSerializer

class StudentsEnrolledList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = StudentsEnrolledListSerializer