from django.db import models

class Student(models.Model):
    """学生信息模型"""
    student_id = models.CharField(max_length=20, unique=True, verbose_name='学号')
    name = models.CharField(max_length=50, verbose_name='姓名')
    gender = models.CharField(max_length=10, choices=[('男', '男'), ('女', '女')], verbose_name='性别')
    birth_date = models.DateField(verbose_name='出生日期')
    major = models.CharField(max_length=100, verbose_name='专业')
    class_name = models.CharField(max_length=50, verbose_name='班级')
    email = models.EmailField(verbose_name='邮箱')
    phone = models.CharField(max_length=20, verbose_name='电话')
    address = models.TextField(verbose_name='地址')
    enrollment_date = models.DateField(verbose_name='入学日期')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'

    def __str__(self):
        return f"{self.student_id} - {self.name}"