
# CT-Factory API Documentation

## Project Overview
The **CT-Factory API** is a robust solution for managing factory operations, offering streamlined management of customers, employees, orders, products, and production processes. Built with Python's Flask framework, the system ensures modularity and scalability for future expansions.

## Key Features
- **RESTful API**: Exposes endpoints for CRUD operations across various factory entities.
- **Swagger Documentation**: Provides an interactive interface for testing API endpoints.
- **Database Integration**: Uses SQLite for local development, with support for other databases like PostgreSQL or MySQL in production.
- **CI/CD Workflow**: Automated testing and deployment via GitHub Actions.
- **Modular Design**: Organized codebase with blueprints for maintainability.

---

## File Structure
```
CT-FACTORY-API-Documentation-main-updated/
    app.py                 # Main application file for running the Flask server
    config.py              # Configuration file for environment and database settings
    migrations/            # Database migration files (generated with Flask-Migrate)
    models.py              # SQLAlchemy models defining database schema
    requirements.txt       # Python dependencies
    swagger.yaml           # Swagger API documentation
    swagger_config.py      # Configuration for Swagger UI
    .github/
        workflows/
            main.yml       # CI/CD GitHub Actions workflow
    blueprints/            # Blueprint files for modular APIs
        customer.py        # Customer API
        employee.py        # Employee API
        order.py           # Order API
        ...
    instance/
        factory.db         # Local SQLite database
    static/
        swagger.yaml       # Static copy of Swagger documentation
    tests/                 # Unit test files
        test_customer.py   # Test cases for customer module
        ...
```

---

## Prerequisites
Before setting up the project, ensure the following tools are installed:
1. **Python**: Version 3.8 or higher.
2. **pip**: Python's package installer.
3. **SQLite**: Pre-installed with Python; optional for switching to a production database.
4. **Git**: For cloning the repository.
5. **Virtual Environment Tool**: `venv` or `virtualenv`.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-link>
cd CT-FACTORY-API-Documentation-main-updated
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment:
```bash
# On Linux/MacOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
Install required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
Initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5. Run the Application
Start the development server:
```bash
python app.py
```
Access the API locally at `http://127.0.0.1:5000`.

### 6. View API Documentation
Visit `http://127.0.0.1:5000/swagger` for Swagger documentation and to test API endpoints interactively.

---

## Testing the Application

### Running Unit Tests
Execute unit tests using `pytest`:
```bash
pytest
```

Ensure all tests in the `tests/` folder pass before deploying.

### Testing API Endpoints
Use tools like **Postman** or **Swagger UI** to test the API endpoints manually.

---

## Deployment

### Modify Configuration
Update `config.py` for the production environment. Example:
- Change the database URL to your production database (e.g., PostgreSQL).
- Set the `DEBUG` flag to `False`.

### Host the Application
Choose a hosting platform, such as:
- [Render](https://render.com)
- [Heroku](https://www.heroku.com/)
- [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)

Deploy the application by following the platform-specific instructions.

### Automate Deployment with CI/CD
The `.github/workflows/main.yml` file is preconfigured to automate testing and deployment:
- Triggers on every push or pull request to the `main` branch.
- Runs unit tests and deploys if all tests pass.

---

## Hosted Site
Provide the live site link here once deployed:
[Hosted Site Link](#)

---

## Contributing

### Reporting Issues
Submit an issue via the GitHub repository with a detailed description and reproduction steps.

### Submitting Pull Requests
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request for review.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.
