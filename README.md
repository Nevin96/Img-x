# ImgX – Image Processing API

A production-style **image processing backend** built with **FastAPI, PostgreSQL, and Docker**.  
ImgX allows authenticated users to upload images, generate resized variants, and retrieve them through a secure API.

---

## Features

- JWT Authentication (Access + Refresh Tokens)
- Image Upload API
- Dynamic Image Transformations (resize variants)
- Background Image Processing
- Metadata Storage in PostgreSQL
- Signed URL Access for Images
- Pagination for Image Listing
- Automated Tests with Pytest
- Dockerized Deployment
- Database Migrations with Alembic

---

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- Pydantic

### Database
- PostgreSQL
- Alembic migrations

### Image Processing
- Pillow

### Security
- JWT Authentication (`python-jose`)
- Password hashing (`passlib`)

### Infrastructure
- Docker
- Docker Compose

### Testing
- Pytest
- HTTPX

---

## Project Structure

```
imgx/
│
├── app/
│   ├── auth/          # authentication routes & logic
│   ├── core/          # configuration & security
│   ├── db/            # database session & dependencies
│   ├── images/        # image upload & processing
│   ├── schemas/       # pydantic models
│   └── main.py        # FastAPI entrypoint
│
├── migrations/        # alembic database migrations
├── media/             # uploaded images
├── tests/             # automated tests
│
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

---

## API Endpoints

### Authentication

```
POST /auth/register
POST /auth/login
POST /auth/refresh
```

### Images

```
POST /images/upload
GET /images
GET /images/{id}
GET /images/{id}/variant
```

### Health Check

```
GET /
```

---

## Running the Project

### Requirements

- Docker
- Docker Compose

Start the backend and database:

```
docker compose up --build
```

API will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

---

## Run Database Migrations

```
docker compose exec api uv run alembic upgrade head
```

---

## Running Tests

```
uv run pytest
```

---

## Example Workflow

### 1. Register a user

```
POST /auth/register
```

### 2. Login and obtain JWT

```
POST /auth/login
```

### 3. Upload an image

```
POST /images/upload
```

### 4. Request resized variant

```
GET /images/{id}/variant?width=300&height=300
```

---

## Future Improvements

- Redis caching
- Rate limiting
- Object storage (S3)
- CI/CD pipeline
- Async task queue (Celery or RQ)

---

## Author

**Nevin Babu**


## License

MIT License
