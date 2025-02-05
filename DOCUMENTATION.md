# News Aggregator Documentation

## 1. Introduction

The News Aggregator is a Django-based web application that automatically scrapes and aggregates news articles from multiple sources using Selenium. The project stores articles in a Django model and presents them through a clean, user-friendly interface. This documentation serves both developers looking to contribute or modify the project and end-users who want to deploy and use the system.

## 2. Project Overview

### Framework & Tools
- **Django**: Web framework
- **Selenium**: Web scraping
- **PostgreSQL**: Database
- **Bootstrap**: Frontend styling

### Key Components
- `news/models.py`: Defines the `Headline` model
- `news/views.py`: Contains views for scraping and display
- `news/urls.py`: URL routing configuration
- `news/scrapers/`: Scraper modules
- `templates/news/home.html`: Frontend template
- `news_aggregator/settings.py`: Project configuration

## 3. Installation and Setup

### Clone the Repository
```bash
git clone <repository-url>
cd news-aggregator
```

### Setup Virtual Environment & Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Database Configuration
1. Ensure PostgreSQL is installed and running
2. Update database settings in `news_aggregator/settings.py` if needed
3. Run migrations:
```bash
python manage.py migrate
```

### Running the Project
1. Start the development server:
```bash
python manage.py runserver
```
2. Visit `http://localhost:8000` in your browser
3. Click "Get my morning news" to trigger scraping

## 4. Architecture and Code Walkthrough

### Project Structure
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

#### Models (`news/models.py`)
The `Headline` model stores:
- `title`: Article title (CharField)
- `image`: Article image URL (URLField)
- `url`: Article link (TextField)

#### Scrapers (`news/scrapers/`)
- **Base Scraper**: Provides common functionality for all scrapers
  - Driver initialization
  - Page loading
  - Article saving
- **Specific Scrapers**: Implement parsing logic for different news sites
  - Dnevnik Scraper
  - Webcafe Scraper

#### Views (`news/views.py`)
- `scrape_multiple_sites`: Concurrent scraping implementation
- `news_list`: Displays aggregated news

#### Templates (`templates/news/home.html`)
Bootstrap-based responsive grid layout for news articles

## 5. Usage and Contribution

### Using the Application
1. Access the homepage to view current headlines
2. Click "Get my morning news" to fetch fresh articles
3. Click on headlines to read full articles on source websites

### Contributing
1. Fork the repository
2. Create a feature branch
3. Implement changes
4. Submit a pull request

Areas for contribution:
- New scrapers
- UI improvements
- Documentation updates
- Test coverage

## 6. Future Enhancements

1. Error Handling and Logging
   - Implement comprehensive error handling
   - Add logging system for debugging

2. Testing
   - Unit tests for scrapers
   - Integration tests
   - End-to-end testing

3. UI/UX Improvements
   - Advanced filtering
   - Search functionality
   - User preferences

4. Performance Optimization
   - Caching implementation
   - Database query optimization

## 7. References

### Project Files
- `news/models.py`: Data structure
- `news/views.py`: Core functionality
- `news/scrapers/`: Scraping implementation
- `templates/news/home.html`: Frontend template

### External Documentation
- [Django Documentation](https://docs.djangoproject.com/)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)