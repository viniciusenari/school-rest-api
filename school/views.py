from rest_framework import viewsets, generics, status
from school.models import Student, Course, Enrollment
from school.serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer, EnrollmentStudentListSerializer, StudentSerializerV2, StudentsEnrolledListSerializer
from rest_framework.response import Response

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        else:
            return StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response

class EnrollmentsViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    http_method_names = ['get', 'post']

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