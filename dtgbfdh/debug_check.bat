@echo off
echo ========================================
echo   CodeLearn - Диагностика системы
echo ========================================
echo.

echo 1. Проверка Java:
java -version
echo.

echo 2. Проверка Maven:
mvn --version
if %errorlevel% neq 0 echo Maven НЕ найден!
echo.

echo 3. Проверка структуры проекта:
if exist pom.xml echo pom.xml - НАЙДЕН
if not exist pom.xml echo pom.xml - НЕ НАЙДЕН!
echo.

echo 4. Проверка основного класса:
if exist src\main\java\org\yourcompany\yourproject\Codemy.java echo Codemy.java - НАЙДЕН
if not exist src\main\java\org\yourcompany\yourproject\Codemy.java echo Codemy.java - НЕ НАЙДЕН!
echo.

echo 5. Проверка application.properties:
if exist src\main\resources\application.properties echo application.properties - НАЙДЕН
if not exist src\main\resources\application.properties echo application.properties - НЕ НАЙДЕН!
echo.

pause