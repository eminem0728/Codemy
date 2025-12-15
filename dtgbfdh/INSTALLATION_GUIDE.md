# CodeLearn - Руководство по установке

## Проблема
Spring Boot приложение не запускается из-за отсутствия:
- Maven (для управления зависимостями)
- Java 17+ (Spring Boot 3.2.0 требует Java 17+)

## Быстрое решение (рекомендуется)

### Вариант 1: Через PowerShell (от имени администратора)
```powershell
winget install OpenJDK.JavaRuntimeEnvironment --version 17.0.8.7
winget install Apache.Maven
```

### Вариант 2: Ручная установка
1. **Java 17**: Скачайте с https://jdk.java.net/17/
2. **Maven**: Скачайте с https://maven.apache.org/download.cgi
3. Установите в `C:\Java\`
4. Добавьте в PATH:
   - `C:\Java\jdk-17.0.2\bin`
   - `C:\Java\apache-maven-3.9.4\bin`

## После установки

### Проверка окружения
```bash
test_environment.bat
```

### Запуск приложения
```bash
run.bat
```

## Обходное решение (если не хотите устанавливать)

### Создание автономного JAR файла
1. Установите Maven временно (можно portable версию)
2. Выполните: `mvn clean package -DskipTests`
3. Запустите: `java -jar target/codemy6-1.0-SNAPSHOT.jar`

## Проверка работоспособности
После запуска откройте http://localhost:8080

Должны быть доступны:
- Главная страница (/)
- Авторизация (/login, /register)
- Курсы (/courses)
- H2 консоль (/h2-console)

## Устранение неполадок

### Если Java 8 все еще используется
Проверьте PATH: `where java`
Удалите старые пути к Java 8

### Если Maven не найден
Проверьте установку: `mvn --version`
Перезапустите командную строку

### Если порт 8080 занят
Измените в `application.properties`:
```properties
server.port=8081