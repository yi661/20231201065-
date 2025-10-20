#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hello World 命令行版本
作者: 陈磊
学号: 20231201065
"""

import argparse
import sys

def generate_hello_world():
    """生成Hello World"""
    return "Hello World! - 来自学号: 20231201065 陈磊"

def main():
    parser = argparse.ArgumentParser(description='Hello World 生成器')
    parser.add_argument('--count', '-c', type=int, default=1, 
                       help='生成Hello World的次数')
    parser.add_argument('--version', '-v', action='store_true',
                       help='显示版本信息')
    
    args = parser.parse_args()
    
    if args.version:
        print("Hello World Generator v1.0")
        print("作者: 陈磊")
        print("学号: 20231201065")
        return
    
    for i in range(args.count):
        if args.count > 1:
            print(f"{i+1}. {generate_hello_world()}")
        else:
            print(generate_hello_world())

if __name__ == "__main__":
    main()