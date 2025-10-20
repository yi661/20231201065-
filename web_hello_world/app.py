#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web版 Hello World 生成器 - 后端API
作者: 陈磊
学号: 20231201065
"""

from flask import Flask, request, jsonify, render_template
from datetime import datetime
import json
import os

app = Flask(__name__)

class HelloWorldGenerator:
    """Hello World 生成器类"""
    
    @staticmethod
    def generate_basic():
        """生成基础Hello World"""
        return {
            "message": "Hello World!",
            "author": "陈磊",
            "student_id": "20231201065",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    @staticmethod
    def generate_multiple(count=5):
        """生成多个Hello World"""
        messages = []
        for i in range(count):
            messages.append({
                "id": i + 1,
                "message": f"Hello World {i + 1}!",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        
        return {
            "messages": messages,
            "total": count,
            "author": "陈磊",
            "student_id": "20231201065"
        }
    
    @staticmethod
    def generate_custom(language="english", style="normal"):
        """生成自定义Hello World"""
        greetings = {
            "english": "Hello World!",
            "chinese": "你好，世界！",
            "spanish": "¡Hola Mundo!",
            "french": "Bonjour le Monde!",
            "german": "Hallo Welt!",
            "japanese": "こんにちは世界！",
            "korean": "안녕하세요 세계!"
        }
        
        styles = {
            "normal": "",
            "excited": "🎉 ",
            "formal": "👔 ",
            "casual": "😊 ",
            "tech": "💻 "
        }
        
        greeting = greetings.get(language.lower(), "Hello World!")
        style_prefix = styles.get(style.lower(), "")
        
        return {
            "message": f"{style_prefix}{greeting}",
            "language": language,
            "style": style,
            "author": "陈磊",
            "student_id": "20231201065",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

# API路由
@app.route('/')
def index():
    """主页"""
    return render_template('index.html')

@app.route('/api/hello', methods=['GET'])
def api_hello():
    """基础Hello World API"""
    result = HelloWorldGenerator.generate_basic()
    return jsonify(result)

@app.route('/api/hello/multiple', methods=['GET'])
def api_hello_multiple():
    """多个Hello World API"""
    count = request.args.get('count', 5, type=int)
    if count < 1 or count > 100:
        return jsonify({"error": "数量必须在1-100之间"}), 400
    
    result = HelloWorldGenerator.generate_multiple(count)
    return jsonify(result)

@app.route('/api/hello/custom', methods=['GET', 'POST'])
def api_hello_custom():
    """自定义Hello World API"""
    if request.method == 'POST':
        data = request.get_json()
        language = data.get('language', 'english')
        style = data.get('style', 'normal')
    else:
        language = request.args.get('language', 'english')
        style = request.args.get('style', 'normal')
    
    result = HelloWorldGenerator.generate_custom(language, style)
    return jsonify(result)

@app.route('/api/info')
def api_info():
    """应用信息API"""
    return jsonify({
        "name": "Web Hello World Generator",
        "version": "1.0.0",
        "author": "陈磊",
        "student_id": "20231201065",
        "description": "一个基于Web的Hello World生成器应用",
        "github": "https://github.com/yi661/20231201065-"
    })

@app.route('/health')
def health_check():
    """健康检查"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

if __name__ == '__main__':
    # 创建必要的目录
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    print("🚀 Web Hello World 生成器启动中...")
    print("作者: 陈磊")
    print("学号: 20231201065")
    print("访问地址: http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)