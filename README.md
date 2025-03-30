# 📰 News Aggregator

> Автоматизиран агрегатор на новини, изграден с Django и Selenium, който събира и представя новини от различни български и международни източници на едно място.

[![Django Version](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## ✨ Основни характеристики

### 📱 Поддържани източници
| Източник | Тип съдържание | Език |
|----------|----------------|------|
| Dnevnik.bg | Новини от България | 🇧🇬 BG |
| Webcafe.bg | Статии и анализи | 🇧🇬 BG |
| BBC.com | Международни новини | 🇬🇧 EN |
| Gong.bg | Спортни новини | 🇧🇬 BG |

### 🚀 Функционалности
- ⚡ Паралелно извличане на новини за по-добра производителност
- 🔄 Индивидуално обновяване по източник
- 📱 Отзивчив дизайн с Bootstrap
- 🔌 Модулна архитектура за лесно добавяне на нови източници
- 🗄️ PostgreSQL база данни
- 🎨 Изчистен и интуитивен интерфейс

---

## 🏗️ Архитектура на проекта

```
news_aggregator/
├── 📄 manage.py
├── 📋 requirements.txt
├── 📚 DOCUMENTATION.md
├── 📁 news_aggregator/
│   ├── ⚙️ settings.py
│   ├── 🔗 urls.py
│   └── 🌐 wsgi.py
├── 📁 news/
│   ├── 📊 models.py
│   ├── 👀 views.py
│   ├── 🔗 urls.py
│   └── 📁 scrapers/
│       ├── 🔧 base_scraper.py
│       ├── 📰 dnevnik_scraper.py
│       ├── 📰 webcafe_scraper.py
│       ├── 📰 bbc_scraper.py
│       └── 📰 gong_scraper.py
└── 📁 templates/
    └── 📁 news/
        └── 🎨 home.html
```

### 🔑 Основни компоненти
- `📊 models.py`: Структура на данните за новините
- `👀 views.py`: Основна логика и контролери
- `🔧 scrapers/`: Модули за извличане на данни от всеки източник
- `🎨 templates/`: Шаблони за визуализация

---

## 📋 Изисквания

### 🛠️ Технически изисквания
- ![Python](https://img.shields.io/badge/Python-3.8+-blue)
- ![Django](https://img.shields.io/badge/Django-4.2+-green)
- ![Selenium](https://img.shields.io/badge/Selenium-4.0+-yellow)
- ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13.0+-blue)
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0+-purple)
- ![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-latest-orange)
- ![Requests](https://img.shields.io/badge/Requests-latest-red)

> 📝 За пълен списък на зависимостите, вижте `requirements.txt`

---

## 🚀 Инсталация и настройка

### 1️⃣ Клониране на хранилището
```bash
git clone <repository-url>
cd news-aggregator
```

### 2️⃣ Създаване на виртуална среда
```bash
python -m venv venv
source venv/bin/activate  # За Windows: venv\Scripts\activate
```

### 3️⃣ Инсталиране на зависимостите
```bash
pip install -r requirements.txt
```

### 4️⃣ Настройка на базата данни
- ✅ Уверете се, че PostgreSQL е инсталиран и работи
- ⚙️ Актуализирайте настройките в `settings.py` при нужда
- 🔄 Изпълнете миграциите:
```bash
python manage.py migrate
```

### 5️⃣ Стартиране на сървъра
```bash
python manage.py runserver
```

---

## 📖 Използване

1. 🌐 Отворете `http://localhost:8000` в браузъра
2. 🔄 Изберете начин за обновяване:
   - 📰 "Вземи всички новини" за всички източници
   - 🎯 Използвайте бутоните за конкретен източник
3. 📱 Разгледайте новините по категории
4. 🔗 Кликнете върху заглавие за пълната статия

---

## 🤝 Принос към проекта

### Как да допринесете
1. 🍴 Направете Fork на проекта
2. 🌿 Създайте feature branch (`git checkout -b feature/ИмеНаФункцията`)
3. ✍️ Направете промените
4. 📤 Публикувайте branch-a (`git push origin feature/ИмеНаФункцията`)
5. 📫 Отворете Pull Request

### 🎯 Области за принос
- 🔌 Нови скрейпъри за допълнителни източници
- 🎨 Подобрения на потребителския интерфейс
- 📚 Обновяване на документацията
- ✅ Разширяване на тестовото покритие
- ⚡ Оптимизации на производителността
- 🌍 Многоезична поддръжка

## Testing

The project includes a comprehensive test suite covering unit tests, integration tests, and end-to-end tests.

### Test Structure
```
tests/
├── unit/
│   ├── test_models.py
│   ├── test_views.py
│   └── test_scrapers/
│       ├── test_base_scraper.py
│       ├── test_dnevnik_scraper.py
│       ├── test_webcafe_scraper.py
│       ├── test_bbc_scraper.py
│       └── test_gong_scraper.py
├── integration/
│   └── test_scraping_workflow.py
└── e2e/
    └── test_user_interface.py
```

### Running Tests

1. Run the entire test suite:
```bash
python manage.py test
```

2. Run specific test categories:
```bash
python manage.py test tests.unit  # Run unit tests only
python manage.py test tests.integration  # Run integration tests
python manage.py test tests.e2e  # Run end-to-end tests
```

3. Run tests with coverage report:
```bash
coverage run manage.py test
coverage report
coverage html  # Generates detailed HTML report
```

### Test Categories

#### Unit Tests
- `test_models.py`: Tests for Headline model and its methods
- `test_views.py`: Tests for view functions and their responses
- `test_scrapers/`: Tests for individual scraper implementations
  - Uses mocking to simulate Selenium and web responses
  - Tests scraper logic in isolation

#### Integration Tests
- Tests the interaction between different components
- Verifies scraping workflow and data persistence
- Ensures proper communication between scrapers and database

#### End-to-End Tests
- Simulates real user interactions with the application
- Tests the complete flow from triggering scrapes to viewing results
- Verifies UI elements and responsive design

### Setting Up Test Environment

1. Install testing dependencies:
```bash
pip install coverage
pip install pytest
```

2. Configure test database in `settings.py`:
```python
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }
    }
```

3. Create test fixtures if needed:
```bash
python manage.py dumpdata news > tests/fixtures/sample_headlines.json
```

### Writing Tests

When contributing new features, ensure to:
- Add corresponding unit tests
- Update integration tests if component interactions change
- Follow existing test patterns and naming conventions
- Use appropriate assertions and test cases
- Include docstrings explaining test purposes

## Future Enhancements

1. Error Handling and Logging
   - Comprehensive error handling system
   - Logging system for debugging

2. Testing
   - Unit tests for scrapers
   - Integration tests
   - End-to-end testing

3. UI/UX Improvements
   - Advanced filtering options
   - Search functionality
   - User preferences

4. Performance Optimization
   - Caching implementation
   - Database query optimization

## References

### Project Documentation
- Detailed documentation available in `DOCUMENTATION.md`

### External Documentation
- [Django Documentation](https://docs.djangoproject.com/)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

---
For more detailed information about the project's architecture, implementation details, and contribution guidelines, please refer to `DOCUMENTATION.md`.
