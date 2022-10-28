from rest_framework import serializers
from school.models import Student, Course, Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'phone', 'birthday']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
    
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        exclude = []

class EnrollmentStudentListSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = ['course', 'period']
        
    def get_period(self, obj):
        return obj.get_period_display()

class StudentsEnrolledListSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Enrollment
        fields = ['student']

    def get_period(self, obj):
        return obj.get_period_display()

class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'ssn', 'email', 'phone', 'birthday']