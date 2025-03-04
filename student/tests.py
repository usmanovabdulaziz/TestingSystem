from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from student.models import Student


class StudentAPITestCase(APITestCase):

    def test_create_student(self):
        """Student yaratish (POST /students/)"""
        url = reverse('student-list')
        data = {
            "name": "Jane Doe",
            "email": "jane.doe@example.com"  # Email qo'shildi
        }
        response = self.client.post(url, data, format='json')
        print("CREATE RESPONSE:", response.data)  # Xato sababini ko'rish uchun
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def setUp(self):
        """Test uchun student yaratamiz"""
        self.student = Student.objects.create(
            name="John Doe",
            email="john.doe@example.com"
        )

    def test_update_student(self):
        """Studentni yangilash (PUT /students/{id}/)"""
        url = reverse('student-detail', args=[self.student.id])
        data = {
            "name": "John Smith",
            "email": "john.smith@example.com"
        }
        response = self.client.put(url, data, format='json')
        print("UPDATE RESPONSE:", response.data)  # Xato sababini ko'rish uchun
        self.assertEqual(response.status_code, status.HTTP_200_OK)
