# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install pipenv requirements
COPY Pipfile Pipfile.lock .
RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . /app

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ParKING.wsgi"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
