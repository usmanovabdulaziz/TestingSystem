from django.urls import path
from .views import *

urlpatterns = [
    path('tests/', TestListCreateAPIView.as_view(), name='test-list'),
    path('tests/<int:pk>/', TestDetailAPIView.as_view(), name='test-detail'),
    path('test-results/', TestResultListCreateAPIView.as_view(), name='test-result-list'),
    path('test-results/<int:pk>/', TestResultDetailAPIView.as_view(), name='test-result-detail'),
    path('test-results/student/<int:student_id>/', TestResultByStudentAPIView.as_view(), name='test-result-by-student'),
    path('test-results/test/<int:test_id>/', TestResultByTestAPIView.as_view(), name='test-result-by-test'),
    path('test-results/test/<int:test_id>/average/', TestAverageScoreAPIView.as_view(), name='test-average-score'),
    path('test-results/test/<int:test_id>/highest/', TestHighestScoreAPIView.as_view(), name='test-highest-score'),
]
