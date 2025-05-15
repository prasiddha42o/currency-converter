# Currency Converter FastAPI Microservice

## Overview

Using FastAPI framework, the project turns currencies into each other using recent exchange rates received from an external API. This application follows clean architecture, the 12-Factor principles, uses Docker for containers, has CI/CD, and automated testing.

---

## Features

- Convert between any two currencies using real-time rates from an external API
- Stores conversion history in a SQLite database
- RESTful API with automatic docs (Swagger UI)
- Environment-based configuration (12-Factor)
- Docker & Docker Compose support
- Automated tests with pytest
- Pre-commit hooks for code quality
- GitHub Actions CI workflow

---

## Getting Started

### Prerequisites

- Python 3.12+
- [Docker](https://www.docker.com/) (for containerization)
- [Git](https://git-scm.com/) (for version control)
- [pre-commit](https://pre-commit.com/) (optional, for hooks)

---

### Installation (Local)

1. **Clone the repository:**
   ```sh
   git clone <https://github.com/prasiddha42o/currency-converter>
   cd currency-converter
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in your project root:
     ```
     EXCHANGE_API_KEY=your_actual_api_key
     DATABASE_URL=currency.db
     ```

5. **Run the application:**
   ```sh
   uvicorn app.main:app --reload
   ```
   The API will be available at [http://localhost:8000](http://localhost:8000).

---

### Running with Docker

1. **Build and start the service:**
   ```sh
   docker-compose up --build
   ```
2. **Access the API:**  
   [http://localhost:8000](http://localhost:8000)

---

### API Endpoints

- `GET /` — Health check
- `POST /convert` — Convert currency (params: `amount`, `from_currency`, `to_currency`)
- `GET /history` — Get conversion history

Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Running Tests

```sh
PYTHONPATH=. pytest
```

---

### Pre-commit Hooks

1. **Install pre-commit (if not already):**
   ```sh
   pip install pre-commit
   ```
2. **Install hooks:**
   ```sh
   pre-commit install
   ```
3. **Now, every commit will be checked for code style and linting.**

---

### Branching Strategy

- Use feature branches for new work.
- Open pull requests to merge into `main`.
- All code is reviewed and tested before merging.

---

### CI/CD

- GitHub Actions runs tests automatically on every push and pull request.
- See `.github/workflows/ci.yml` for details.

---

## Configuration

All configuration is handled via environment variables (see `.env`).  
Sensitive data (like API keys) should **never** be committed to the repository.

---

## Documentation

- Interactive API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- (Optional) You can generate full project documentation with MkDocs:
  ```sh
  mkdocs serve
  ```
  Then visit [http://localhost:8000](http://localhost:8000)

---

## License

MIT License

---

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [pytest](https://docs.pytest.org/)
- [pre-commit](https://pre-commit.com/)
- [GitHub Actions](https://github.com/features/actions)

---

**Feel free to fork, contribute, and use this as a template for your own microservices!**