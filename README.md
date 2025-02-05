# News Aggregator

A Django-based web application that automatically scrapes and aggregates news articles from multiple sources using Selenium. This project provides a clean, user-friendly interface to view aggregated news content from various sources in one place.

## Features

- Automatic news scraping from multiple sources
- Concurrent scraping implementation for better performance
- Responsive design using Bootstrap
- Modular scraper architecture for easy addition of new sources
- PostgreSQL database for reliable data storage
- Clean and intuitive user interface

## Project Overview

### Architecture
```
news_aggregator/
├── manage.py
├── requirements.txt
├── DOCUMENTATION.md
├── news_aggregator/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── news/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── scrapers/
│       ├── base_scraper.py
│       ├── dnevnik_scraper.py
│       └── webcafe_scraper.py
└── templates/
    └── news/
        └── home.html
```

### Key Components
- `news/models.py`: Defines the data structure for news articles
- `news/views.py`: Contains core functionality and controller logic
- `news/scrapers/`: Houses modular scraping implementations
- `templates/news/home.html`: Frontend template for displaying news

## Requirements

- Python 3.x
- Django
- Selenium
- PostgreSQL
- Bootstrap

For a complete list of dependencies, please refer to `requirements.txt`.

## Installation and Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd news-aggregator
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure PostgreSQL:
- Ensure PostgreSQL is installed and running
- Update database settings in `news_aggregator/settings.py` if needed

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## Usage

1. Access the application at `http://localhost:8000`
2. Click "Get my morning news" to trigger the scraping process
3. Browse through the aggregated news articles
4. Click on headlines to read full articles on their source websites

## Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- New scrapers for additional news sources
- UI/UX improvements
- Documentation updates
- Test coverage expansion
- Performance optimizations

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