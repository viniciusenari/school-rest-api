from rest_framework.test import APITestCase
from school.models import Course
from django.urls import reverse
from rest_framework import status

class CoursesTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Courses-list')
        self.course_1 = Course.objects.create(course_id='TC1', description='Test Course 1', level='A')
        self.course_1 = Course.objects.create(course_id='TC2', description='Test Course 2', level='I')

    def test_request_get_courses_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_request_post_create_course(self):
        data = {
            'course_id': 'TC3',
            'description': 'Test Course 3',
            'level': 'A'
            }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['course_id'], 'TC3')
        self.assertEqual(response.data['description'], 'Test Course 3')
        self.assertEqual(response.data['level'], 'A')

    def test_request_delete_course(self):
        response = self.client.delete(self.list_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_request_put_course(self):
        data = {
            'course_id': 'TC1',
            'description': 'Test Course 1 - Updated',
            'level': 'B'
            }
        response = self.client.put(self.list_url + '1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['course_id'], 'TC1')
        self.assertEqual(response.data['description'], 'Test Course 1 - Updated')
        self.assertEqual(response.data['level'], 'B')