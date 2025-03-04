from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from student.models import Student
from student_test.models import Test, TestResult

class TestAPITestCase(APITestCase):

    def setUp(self):
        """Testlar uchun oldindan obyektlar yaratamiz."""
        self.test = Test.objects.create(name="Mathematics", max_score=100)
        self.student = Student.objects.create(name="John Doe")  # Student modelida `name` maydon borligini tekshiring.
        self.test_result = TestResult.objects.create(student=self.student, test=self.test, score=90)

    def test_create_test(self):
        """Test yaratish (POST /tests/)"""
        url = reverse('test-list')
        data = {"name": "Physics", "max_score": 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Test.objects.count(), 2)

    def test_get_tests(self):
        """Barcha testlarni olish (GET /tests/)"""
        url = reverse('test-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_test_detail(self):
        """Test tafsilotlarini olish (GET /tests/{id}/)"""
        url = reverse('test-detail', args=[self.test.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Mathematics")

    def test_update_test(self):
        """Testni yangilash (PUT /tests/{id}/)"""
        url = reverse('test-detail', args=[self.test.id])
        data = {"name": "Advanced Mathematics", "max_score": 150}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.test.refresh_from_db()
        self.assertEqual(self.test.name, "Advanced Mathematics")

    def test_delete_test(self):
        """Testni o‘chirish (DELETE /tests/{id}/)"""
        url = reverse('test-detail', args=[self.test.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Test.objects.count(), 0)

class TestResultAPITestCase(APITestCase):

    def setUp(self):
        """Test natijalari uchun obyekt yaratamiz."""
        self.test = Test.objects.create(name="Science", max_score=100)
        self.student = Student.objects.create(name="Jane Doe")  # Student modelida `name` borligini tekshiring.
        self.test_result = TestResult.objects.create(student=self.student, test=self.test, score=85)

    def test_create_test_result(self):
        """Test natijasi qo‘shish (POST /test-results/)"""
        url = reverse('test-result-list')
        data = {"student": self.student.id, "test": self.test.id, "score": 95}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TestResult.objects.count(), 2)

    def test_get_test_results(self):
        """Barcha test natijalarini olish (GET /test-results/)"""
        url = reverse('test-result-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_test_result_detail(self):
        """Test natijasi tafsilotlarini olish (GET /test-results/{id}/)"""
        url = reverse('test-result-detail', args=[self.test_result.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['score'], 85)

    def test_update_test_result(self):
        """Test natijasini yangilash (PUT /test-results/{id}/)"""
        url = reverse('test-result-detail', args=[self.test_result.id])
        data = {"student": self.student.id, "test": self.test.id, "score": 95}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.test_result.refresh_from_db()
        self.assertEqual(self.test_result.score, 95)

    def test_delete_test_result(self):
        """Test natijasini o‘chirish (DELETE /test-results/{id}/)"""
        url = reverse('test-result-detail', args=[self.test_result.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TestResult.objects.count(), 0)
