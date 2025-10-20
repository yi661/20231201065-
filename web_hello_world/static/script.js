// Web Hello World 生成器 - 前端JavaScript

// 标签页切换功能
document.addEventListener('DOMContentLoaded', function() {
    // 标签页切换
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const tabId = this.getAttribute('data-tab');
            
            // 移除所有active类
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // 添加active类到当前标签
            this.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });
    
    // 初始化应用信息
    loadAppInfo();
});

// 显示消息提示
function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = `toast ${type} show`;
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// 加载应用信息
async function loadAppInfo() {
    try {
        const response = await fetch('/api/info');
        const data = await response.json();
        console.log('应用信息:', data);
    } catch (error) {
        console.error('加载应用信息失败:', error);
    }
}

// 基础Hello World生成
async function generateBasic() {
    const output = document.getElementById('output');
    const generateBtn = document.querySelector('[onclick="generateBasic()"]');
    const originalText = generateBtn.innerHTML;
    
    // 显示加载状态
    generateBtn.innerHTML = '<div class="loading"></div> 生成中...';
    generateBtn.disabled = true;
    
    try {
        const response = await fetch('/api/hello');
        const data = await response.json();
        
        if (response.ok) {
            output.textContent = formatBasicOutput(data);
            output.className = 'output-box success';
            showToast('Hello World生成成功！', 'success');
        } else {
            throw new Error(data.error || '生成失败');
        }
    } catch (error) {
        output.textContent = `错误: ${error.message}`;
        output.className = 'output-box error';
        showToast('生成失败，请重试', 'error');
    } finally {
        // 恢复按钮状态
        generateBtn.innerHTML = originalText;
        generateBtn.disabled = false;
    }
}

// 格式化基础输出
function formatBasicOutput(data) {
    return `🌍 ${data.message}

📅 生成时间: ${data.timestamp}
👤 作者: ${data.author}
🎓 学号: ${data.student_id}

✨ 这是一个基础的Hello World消息！`;
}

// 批量生成Hello World
async function generateMultiple() {
    const countInput = document.getElementById('count');
    const count = parseInt(countInput.value) || 5;
    const output = document.getElementById('output');
    const generateBtn = document.querySelector('[onclick="generateMultiple()"]');
    const originalText = generateBtn.innerHTML;
    
    // 验证数量
    if (count < 1 || count > 100) {
        showToast('数量必须在1-100之间', 'warning');
        return;
    }
    
    // 显示加载状态
    generateBtn.innerHTML = '<div class="loading"></div> 批量生成中...';
    generateBtn.disabled = true;
    
    try {
        const response = await fetch(`/api/hello/multiple?count=${count}`);
        const data = await response.json();
        
        if (response.ok) {
            output.textContent = formatMultipleOutput(data);
            output.className = 'output-box success';
            showToast(`成功生成${count}个Hello World！`, 'success');
        } else {
            throw new Error(data.error || '批量生成失败');
        }
    } catch (error) {
        output.textContent = `错误: ${error.message}`;
        output.className = 'output-box error';
        showToast('批量生成失败，请重试', 'error');
    } finally {
        // 恢复按钮状态
        generateBtn.innerHTML = originalText;
        generateBtn.disabled = false;
    }
}

// 格式化批量输出
function formatMultipleOutput(data) {
    let output = `📦 批量生成结果 (共${data.total}个)\n\n`;
    
    data.messages.forEach(msg => {
        output += `${msg.id}. ${msg.message} (${msg.timestamp})\n`;
    });
    
    output += `\n👤 作者: ${data.author}\n`;
    output += `🎓 学号: ${data.student_id}\n`;
    output += `\n✨ 批量生成完成！`;
    
    return output;
}

// 自定义生成Hello World
async function generateCustom() {
    const language = document.getElementById('language').value;
    const style = document.getElementById('style').value;
    const output = document.getElementById('output');
    const generateBtn = document.querySelector('[onclick="generateCustom()"]');
    const originalText = generateBtn.innerHTML;
    
    // 显示加载状态
    generateBtn.innerHTML = '<div class="loading"></div> 自定义生成中...';
    generateBtn.disabled = true;
    
    try {
        const response = await fetch(`/api/hello/custom?language=${language}&style=${style}`);
        const data = await response.json();
        
        if (response.ok) {
            output.textContent = formatCustomOutput(data);
            output.className = 'output-box success';
            showToast('自定义Hello World生成成功！', 'success');
        } else {
            throw new Error(data.error || '自定义生成失败');
        }
    } catch (error) {
        output.textContent = `错误: ${error.message}`;
        output.className = 'output-box error';
        showToast('自定义生成失败，请重试', 'error');
    } finally {
        // 恢复按钮状态
        generateBtn.innerHTML = originalText;
        generateBtn.disabled = false;
    }
}

// 格式化自定义输出
function formatCustomOutput(data) {
    return `🎨 自定义Hello World\n\n` +
           `💬 消息: ${data.message}\n` +
           `🌐 语言: ${data.language}\n` +
           `🎭 风格: ${data.style}\n` +
           `📅 生成时间: ${data.timestamp}\n` +
           `👤 作者: ${data.author}\n` +
           `🎓 学号: ${data.student_id}\n\n` +
           `✨ 自定义生成完成！`;
}

// 复制到剪贴板
async function copyToClipboard() {
    const output = document.getElementById('output');
    const text = output.textContent;
    
    if (!text || text === '点击上方按钮生成Hello World...') {
        showToast('请先生成Hello World文本', 'warning');
        return;
    }
    
    try {
        await navigator.clipboard.writeText(text);
        showToast('文本已复制到剪贴板！', 'success');
    } catch (error) {
        // 降级方案：使用execCommand
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        
        try {
            document.execCommand('copy');
            showToast('文本已复制到剪贴板！', 'success');
        } catch (err) {
            showToast('复制失败，请手动选择文本复制', 'error');
        }
        
        document.body.removeChild(textArea);
    }
}

// 清空输出
function clearOutput() {
    const output = document.getElementById('output');
    output.textContent = '点击上方按钮生成Hello World...';
    output.className = 'output-box';
    showToast('输出已清空', 'success');
}

// 下载输出
function downloadOutput() {
    const output = document.getElementById('output');
    const text = output.textContent;
    
    if (!text || text === '点击上方按钮生成Hello World...') {
        showToast('没有内容可下载', 'warning');
        return;
    }
    
    const blob = new Blob([text], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    
    a.href = url;
    a.download = `hello_world_${new Date().getTime()}.txt`;
    a.click();
    
    URL.revokeObjectURL(url);
    showToast('文件下载成功！', 'success');
}

// 键盘快捷键
document.addEventListener('keydown', function(event) {
    // Ctrl + 1: 基础生成
    if (event.ctrlKey && event.key === '1') {
        event.preventDefault();
        generateBasic();
    }
    
    // Ctrl + 2: 批量生成
    if (event.ctrlKey && event.key === '2') {
        event.preventDefault();
        generateMultiple();
    }
    
    // Ctrl + 3: 自定义生成
    if (event.ctrlKey && event.key === '3') {
        event.preventDefault();
        generateCustom();
    }
    
    // Ctrl + C: 复制
    if (event.ctrlKey && event.key === 'c') {
        const activeElement = document.activeElement;
        if (!activeElement || activeElement.tagName === 'BODY') {
            event.preventDefault();
            copyToClipboard();
        }
    }
});

// 健康检查
async function healthCheck() {
    try {
        const response = await fetch('/health');
        const data = await response.json();
        console.log('应用健康状态:', data);
    } catch (error) {
        console.error('健康检查失败:', error);
    }
}

// 定期健康检查
setInterval(healthCheck, 30000); // 每30秒检查一次