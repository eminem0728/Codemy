@echo off
setlocal enabledelayedexpansion

echo ========================================
echo   CodeLearn - Установка Java 17 и Maven
echo ========================================
echo.

REM Создаем папки для установки
if not exist "C:\JavaMaven" mkdir "C:\JavaMaven"
if not exist "C:\JavaMaven\java17" mkdir "C:\JavaMaven\java17"
if not exist "C:\JavaMaven\maven" mkdir "C:\JavaMaven\maven"

echo Скачивание Java 17 JDK...
echo Это может занять несколько минут...

REM Скачиваем OpenJDK 17
powershell -Command "Invoke-WebRequest -Uri 'https://download.java.net/java/GA/jdk17.0.2/dfd4a8d0985749f896bed50d7138ee7f/8/GPL/openjdk-17.0.2_windows-x64_bin.zip' -OutFile 'C:\JavaMaven\java17\openjdk-17.zip'"

if exist "C:\JavaMaven\java17\openjdk-17.zip" (
    echo Java 17 скачан успешно!
    echo Распаковка...
    powershell -Command "Expand-Archive -Path 'C:\JavaMaven\java17\openjdk-17.zip' -DestinationPath 'C:\JavaMaven\java17\' -Force"
    del "C:\JavaMaven\java17\openjdk-17.zip"
    echo Java 17 установлен в C:\JavaMaven\java17\
) else (
    echo Ошибка: не удалось скачать Java 17
    echo Попробуйте скачать вручную с https://jdk.java.net/17/
    pause
    exit /b 1
)

echo.
echo Скачивание Maven...
echo Это может занять несколько минут...

REM Скачиваем Maven
powershell -Command "Invoke-WebRequest -Uri 'https://archive.apache.org/dist/maven/maven-3/3.9.4/binaries/apache-maven-3.9.4-bin.zip' -OutFile 'C:\JavaMaven\maven\maven.zip'"

if exist "C:\JavaMaven\maven\maven.zip" (
    echo Maven скачан успешно!
    echo Распаковка...
    powershell -Command "Expand-Archive -Path 'C:\JavaMaven\maven\maven.zip' -DestinationPath 'C:\JavaMaven\maven\' -Force"
    del "C:\JavaMaven\maven\maven.zip"
    echo Maven установлен в C:\JavaMaven\maven\
) else (
    echo Ошибка: не удалось скачать Maven
    echo Попробуйте скачать вручную с https://maven.apache.org/download.cgi
    pause
    exit /b 1
)

echo.
echo Настройка переменных окружения...

REM Получаем текущий PATH
for /f "tokens=2*" %%a in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion" /v ProgramFilesDir') do set "ProgramFiles=%%b"

REM Добавляем в PATH (для текущего пользователя)
setx PATH "%PATH%;C:\JavaMaven\java17\jdk-17.0.2\bin;C:\JavaMaven\maven\apache-maven-3.9.4\bin" /M

if %errorlevel% equ 0 (
    echo Переменные окружения настроены успешно!
) else (
    echo Предупреждение: не удалось настроить PATH автоматически
    echo Добавьте вручную:
    echo C:\JavaMaven\java17\jdk-17.0.2\bin
    echo C:\JavaMaven\maven\apache-maven-3.9.4\bin
)

echo.
echo ========================================
echo Установка завершена!
echo.
echo Перезапустите командную строку или компьютер
echo для применения изменений PATH
echo ========================================
echo.

pause