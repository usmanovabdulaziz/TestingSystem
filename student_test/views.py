from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Max
from .models import Test, TestResult
from .serializers import TestSerializer, TestResultSerializer

class TestListCreateAPIView(APIView):
    def get(self, request):
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Test.objects.get(pk=pk)
        except Test.DoesNotExist:
            return None

    def get(self, request, pk):
        test = self.get_object(pk)
        if test is None:
            return Response({"error": "Test topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TestSerializer(test)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        test = self.get_object(pk)
        if test is None:
            return Response({"error": "Test topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        test = self.get_object(pk)
        if test is None:
            return Response({"error": "Test topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        test.delete()
        return Response({"message": "Test o‘chirildi"}, status=status.HTTP_204_NO_CONTENT)

class TestResultListCreateAPIView(APIView):
    def get(self, request):
        results = TestResult.objects.all()
        serializer = TestResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TestResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestResultDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return TestResult.objects.get(pk=pk)
        except TestResult.DoesNotExist:
            return None

    def get(self, request, pk):
        result = self.get_object(pk)
        if result is None:
            return Response({"error": "Test natijasi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TestResultSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        result = self.get_object(pk)
        if result is None:
            return Response({"error": "Test natijasi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TestResultSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        result = self.get_object(pk)
        if result is None:
            return Response({"error": "Test natijasi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        result.delete()
        return Response({"message": "Test natijasi o‘chirildi"}, status=status.HTTP_204_NO_CONTENT)

class TestResultByStudentAPIView(APIView):
    def get(self, request, student_id):
        results = TestResult.objects.filter(student_id=student_id)
        serializer = TestResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TestResultByTestAPIView(APIView):
    def get(self, request, test_id):
        results = TestResult.objects.filter(test_id=test_id)
        serializer = TestResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TestAverageScoreAPIView(APIView):
    def get(self, request, test_id):
        avg_score = TestResult.objects.filter(test_id=test_id).aggregate(Avg('score'))
        return Response({"average_score": avg_score['score__avg']}, status=status.HTTP_200_OK)

class TestHighestScoreAPIView(APIView):
    def get(self, request, test_id):
        highest_score = TestResult.objects.filter(test_id=test_id).aggregate(Max('score'))
        return Response({"highest_score": highest_score['score__max']}, status=status.HTTP_200_OK)
