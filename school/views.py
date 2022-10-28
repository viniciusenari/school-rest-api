from rest_framework import viewsets, generics
from school.models import Student, Course, Enrollment
from school.serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer, EnrollmentStudentListSerializer, StudentSerializerV2, StudentsEnrolledListSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        else:
            return StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class EnrollmentsViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class EnrollmentStudentList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = EnrollmentStudentListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentsEnrolledList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = StudentsEnrolledListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]