@echo off
chcp 65001 >nul
echo ========================================
echo    Hello World 生成器应用
echo    作者: 陈磊
echo    学号: 20231201065
echo ========================================
echo.
echo 正在启动应用...

REM 检查Python是否可用
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请确保Python已安装并添加到PATH
    echo 或者使用虚拟环境中的Python
    pause
    exit /b 1
)

REM 尝试使用虚拟环境中的Python
if exist ".venv\Scripts\python.exe" (
    echo 使用虚拟环境中的Python...
    .venv\Scripts\python.exe hello_world_app.py
) else (
    echo 使用系统Python...
    python hello_world_app.py
)

echo.
echo 应用已关闭
pause