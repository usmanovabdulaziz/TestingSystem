from django.contrib import admin
from .models import Test, TestResult

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'max_score')
    search_fields = ('name',)

@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'test', 'score')
    search_fields = ('student__name', 'test__name')
