#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CodeLearn Demo Server
Простой веб-сервер для демонстрации приложения
пока устанавливается Java и Maven
"""

import http.server
import socketserver
import os
import webbrowser
from urllib.parse import urlparse, parse_qs
import sys

# Устанавливаем UTF-8 для Windows
if sys.platform.startswith('win'):
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.detach())

class CodeLearnHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=".", **kwargs)
    
    def do_GET(self):
        # Обработка маршрутов
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == "/" or parsed_path.path == "":
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            html = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodeLearn - Демо</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 40px; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container { 
            max-width: 800px; 
            margin: 0 auto; 
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }
        h1 { 
            text-align: center; 
            color: #fff; 
            margin-bottom: 30px;
        }
        .status { 
            background: #4CAF50; 
            color: white; 
            padding: 15px; 
            border-radius: 8px; 
            margin: 20px 0;
            text-align: center;
        }
        .nav { 
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 30px 0;
        }
        .nav a { 
            display: block; 
            padding: 15px; 
            background: rgba(255,255,255,0.2); 
            color: white; 
            text-decoration: none; 
            border-radius: 8px;
            text-align: center;
            transition: all 0.3s ease;
        }
        .nav a:hover { 
            background: rgba(255,255,255,0.3);
            transform: translateY(-2px);
        }
        .warning {
            background: #ff9800;
            color: white;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
        }
        .info {
            background: #2196F3;
            color: white;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎓 CodeLearn - Демо версия</h1>
        
        <div class="status">
            ✅ Веб-сервер запущен и работает!
        </div>
        
        <div class="warning">
            ⚠️ Это демо-версия на Python. 
            Для полной функциональности установите Java 17 и Maven.
        </div>
        
        <div class="info">
            📖 Доступные курсы программирования:
        </div>
        
        <div class="nav">
            <a href="/python-lecture-1.html">🐍 Python - Лекция 1</a>
            <a href="/java-lecture-1.html">☕ Java - Лекция 1</a>
            <a href="/js-lecture-1.html">🌐 JavaScript - Лекция 1</a>
            <a href="/go-lecture-1.html">🔷 Go - Лекция 1</a>
            <a href="/rust-lecture-1.html">🦀 Rust - Лекция 1</a>
            <a href="/cpp-lecture-1.html">⚡ C++ - Лекция 1</a>
            <a href="/kotlin-lecture-1.html">🟡 Kotlin - Лекция 1</a>
            <a href="/courses.html">📚 Все курсы</a>
            <a href="/login.html">🔐 Вход</a>
            <a href="/register.html">📝 Регистрация</a>
        </div>
        
        <div class="info">
            🔧 Инструкции по установке полной версии: <strong>INSTALLATION_GUIDE.md</strong><br>
            🧪 Тест окружения: <strong>test_environment.bat</strong><br>
            ⚡ Быстрая установка: <strong>quick_install.bat</strong>
        </div>
    </div>
</body>
</html>'''
            self.wfile.write(html.encode('utf-8'))
            
        elif parsed_path.path == "/health":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "ok", "message": "Demo server running"}')
        else:
            # Обработка статических файлов
            super().do_GET()

def main():
    PORT = 8081  # Меняем порт, чтобы избежать конфликта
    
    print("=" * 50)
    print("   CodeLearn Demo Server")
    print("=" * 50)
    print(f"Server starting on port {PORT}")
    print(f"Open browser: http://localhost:{PORT}")
    print("=" * 50)
    
    try:
        with socketserver.TCPServer(("", PORT), CodeLearnHandler) as httpd:
            print("Server started successfully!")
            print("Open browser and go to http://localhost:8081")
            print("Press Ctrl+C to stop")
            print("=" * 50)
            
            # Автоматически открываем браузер
            try:
                webbrowser.open(f'http://localhost:{PORT}')
            except:
                pass
                
            httpd.serve_forever()
            
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"Error: Port {PORT} is already in use!")
            print("Try to stop other server or change port")
        else:
            print(f"Server startup error: {e}")
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()