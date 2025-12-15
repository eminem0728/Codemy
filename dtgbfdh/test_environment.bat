@echo off
echo ========================================
echo   CodeLearn - Тест окружения
echo ========================================
echo.

echo 1. Тест Java 17:
java -version
echo.

echo 2. Тест Java Compiler:
javac -version
echo.

echo 3. Тест Maven:
mvn --version
if %errorlevel% neq 0 echo Maven НЕ найден!
echo.

echo 4. Тест Spring Boot:
if exist target\*.jar (
    echo JAR файлы найдены в папке target:
    dir target\*.jar
) else (
    echo JAR файлы НЕ найдены в папке target
)
echo.

echo 5. Проверка структуры проекта:
if exist pom.xml echo pom.xml - OK
if exist src\main\java\org\yourcompany\yourproject\Codemy.java echo Codemy.java - OK
if exist src\main\resources\application.properties echo application.properties - OK
echo.

echo 6. Тест компиляции:
if exist pom.xml (
    echo Попытка компиляции...
    mvn compile
) else (
    echo pom.xml не найден - пропускаем компиляцию
)
echo.

pause