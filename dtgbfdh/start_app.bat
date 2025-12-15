@echo off
setlocal enabledelayedexpansion

echo ========================================
echo   CodeLearn - Запуск приложения
echo ========================================
echo.

:menu
echo Выберите способ запуска:
echo.
echo 1. 🚀 Демо-сервер на Python (быстро, без установки)
echo 2. 🔧 Установить Java 17 + Maven и запустить полную версию
echo 3. 🧪 Проверить текущее окружение
echo 4. 📖 Показать инструкции по установке
echo 5. ❌ Выход
echo.

set /p choice="Ваш выбор (1-5): "

if "%choice%"=="1" goto demo_server
if "%choice%"=="2" goto install_and_run
if "%choice%"=="3" goto test_env
if "%choice%"=="4" goto show_guide
if "%choice%"=="5" goto exit
goto menu

:demo_server
echo.
echo 🚀 Запуск демо-сервера...
echo Этот сервер покажет интерфейс приложения
echo но без backend функциональности (авторизация, БД)
echo.
python demo_server.py
if %errorlevel% neq 0 (
    echo ❌ Ошибка запуска Python сервера
    echo Убедитесь, что Python установлен
)
goto end

:install_and_run
echo.
echo 🔧 Установка Java 17 и Maven...
echo.
echo 1. Откройте PowerShell от имени администратора
echo 2. Выполните команды:
echo.
echo    winget install OpenJDK.JavaRuntimeEnvironment --version 17.0.8.7
echo    winget install Apache.Maven
echo.
echo 3. Перезапустите командную строку
echo 4. Запустите test_environment.bat для проверки
echo 5. Затем запустите run.bat
echo.
echo Подробности в файле: INSTALLATION_GUIDE.md
echo.
pause
goto menu

:test_env
echo.
echo 🧪 Тестирование окружения...
call test_environment.bat
goto menu

:show_guide
echo.
echo 📖 Показ инструкций...
type INSTALLATION_GUIDE.md
echo.
pause
goto menu

:exit
echo.
echo 👋 До свидания!
goto end

:end
echo.
echo ========================================
echo Нажмите любую клавишу для выхода...
pause >nul