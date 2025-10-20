#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hello World 生成器应用
作者: 陈磊
学号: 20231201065
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

def generate_hello_world():
    """生成Hello World"""
    return "Hello World! - 来自学号: 20231201065 陈磊"

class HelloWorldApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello World 生成器")
        self.root.geometry("400x300")
        self.root.resizable(True, True)
        
        # 设置应用图标（如果有的话）
        try:
            self.root.iconbitmap("icon.ico")
        except:
            pass
        
        self.setup_ui()
    
    def setup_ui(self):
        """设置用户界面"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 标题
        title_label = ttk.Label(main_frame, text="Hello World 生成器", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # 作者信息
        author_label = ttk.Label(main_frame, text="作者: 陈磊 | 学号: 20231201065",
                                font=("Arial", 10))
        author_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # 生成按钮
        generate_btn = ttk.Button(main_frame, text="生成 Hello World", 
                                 command=self.generate_output)
        generate_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        # 输出文本框
        self.output_text = tk.Text(main_frame, height=8, width=40, 
                                  font=("Consolas", 10))
        self.output_text.grid(row=3, column=0, columnspan=2, pady=10)
        
        # 滚动条
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", 
                                 command=self.output_text.yview)
        scrollbar.grid(row=3, column=2, sticky=(tk.N, tk.S))
        self.output_text.configure(yscrollcommand=scrollbar.set)
        
        # 按钮框架
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        # 复制按钮
        copy_btn = ttk.Button(button_frame, text="复制到剪贴板", 
                             command=self.copy_to_clipboard)
        copy_btn.grid(row=0, column=0, padx=5)
        
        # 清空按钮
        clear_btn = ttk.Button(button_frame, text="清空输出", 
                             command=self.clear_output)
        clear_btn.grid(row=0, column=1, padx=5)
        
        # 退出按钮
        exit_btn = ttk.Button(button_frame, text="退出", 
                            command=self.root.quit)
        exit_btn.grid(row=0, column=2, padx=5)
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
    
    def generate_output(self):
        """生成Hello World输出"""
        hello_text = generate_hello_world()
        
        # 清空并插入新文本
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, hello_text)
        
        # 在控制台也输出
        print(hello_text)
    
    def copy_to_clipboard(self):
        """复制文本到剪贴板"""
        try:
            text = self.output_text.get(1.0, tk.END).strip()
            if text:
                self.root.clipboard_clear()
                self.root.clipboard_append(text)
                messagebox.showinfo("成功", "文本已复制到剪贴板！")
            else:
                messagebox.showwarning("警告", "没有文本可复制！")
        except Exception as e:
            messagebox.showerror("错误", f"复制失败: {str(e)}")
    
    def clear_output(self):
        """清空输出文本框"""
        self.output_text.delete(1.0, tk.END)

def main():
    """主函数"""
    # 创建主窗口
    root = tk.Tk()
    
    # 创建应用实例
    app = HelloWorldApp(root)
    
    # 启动主循环
    root.mainloop()

if __name__ == "__main__":
    # 命令行版本
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        print(generate_hello_world())
    else:
        main()