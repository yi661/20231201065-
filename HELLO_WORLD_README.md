# Hello World 生成器应用

## 项目信息
- **作者**: 陈磊
- **学号**: 20231201065
- **创建时间**: 2024年

## 应用介绍

这是一个简单的Hello World生成器应用，包含两个版本：

1. **GUI版本** (`hello_world_app.py`) - 图形界面应用
2. **命令行版本** (`hello_world_cli.py`) - 命令行工具

## 文件说明

- `hello_world_app.py` - 图形界面应用主文件
- `hello_world_cli.py` - 命令行版本
- `run_hello_world.bat` - Windows批处理启动文件

## 使用方法

### 方法1: 使用批处理文件（推荐）
1. 双击 `run_hello_world.bat` 文件
2. 应用将自动启动

### 方法2: 直接运行Python文件
```bash
# GUI版本
python hello_world_app.py

# 命令行版本
python hello_world_cli.py
python hello_world_cli.py --count 3  # 生成3次
python hello_world_cli.py --version  # 显示版本信息
```

### 方法3: 使用虚拟环境
```bash
# 激活虚拟环境
.venv\Scripts\activate

# 运行应用
python hello_world_app.py
```

## 功能特点

### GUI版本功能
- ✅ 一键生成Hello World
- ✅ 复制文本到剪贴板
- ✅ 清空输出内容
- ✅ 现代化的界面设计
- ✅ 响应式布局

### 命令行版本功能
- ✅ 基本Hello World输出
- ✅ 支持多次生成
- ✅ 版本信息显示

## 系统要求

- Python 3.6+
- Windows/Linux/macOS
- tkinter库（通常随Python一起安装）

## 技术栈

- **编程语言**: Python 3
- **GUI框架**: tkinter
- **界面组件**: ttk

## 作者信息

**陈磊**  
学号: 20231201065  
GitHub: [https://github.com/yi661/20231201065-](https://github.com/yi661/20231201065-)

---

*这是一个简单的Hello World生成器应用，用于演示基本的Python GUI编程和命令行工具开发。*