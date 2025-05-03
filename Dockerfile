# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Apply migrations and collect static files
RUN python manage.py makemigrations
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput --clear --verbosity 2

# Expose the port the app runs on
EXPOSE 8000

# Command to run the Django app using Gunicorn with increased timeout
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "90", "survey_project.wsgi:application"]