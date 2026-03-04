FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy only dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies into the system site-packages
# --system tells uv to ignore virtualenvs
# -r pyproject.toml tells it where the deps are
RUN uv pip install --system -r pyproject.toml

COPY . .

EXPOSE 8000

# Now uvicorn will be in the system PATH
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]