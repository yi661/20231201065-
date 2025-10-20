from django.shortcuts import render
from django.http import HttpResponse

# 学生信息数据
student_data = {
    'student_id': '20231201065',
    'name': '陈磊',
    'gender': '男',
    'birth_date': '2000-01-01',
    'major': '计算机科学与技术',
    'class_name': '计算机科学与技术2023级1班',
    'email': '20231201065@example.com',
    'phone': '13800138000',
    'address': '北京市海淀区',
    'enrollment_date': '2023-09-01',
    'hobbies': ['编程', '阅读', '运动', '音乐'],
    'skills': ['Python', 'Java', 'HTML/CSS', 'JavaScript', 'Django'],
    'courses': [
        {'name': '数据结构', 'score': 95},
        {'name': '算法分析', 'score': 92},
        {'name': '数据库系统', 'score': 88},
        {'name': '操作系统', 'score': 90},
        {'name': '计算机网络', 'score': 87}
    ],
    'achievements': [
        '2023年度优秀学生',
        '程序设计大赛二等奖',
        '英语四级证书',
        '计算机二级证书'
    ]
}

def student_page(request):
    """学生个人页面"""
    return render(request, 'student/student_page.html', {'student': student_data})

def student_info(request):
    """学生基本信息页面"""
    return render(request, 'student/student_info.html', {'student': student_data})

def student_courses(request):
    """学生课程成绩页面"""
    return render(request, 'student/student_courses.html', {'student': student_data})

def student_achievements(request):
    """学生成就页面"""
    return render(request, 'student/student_achievements.html', {'student': student_data})