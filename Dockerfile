# Use the official Python image as the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project directory into the container
COPY . /app/

# Install the project dependencies
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

# Expose the port that FastAPI is running on (default is 8000)
EXPOSE 8000

# Command to start your FastAPI application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]