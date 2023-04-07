FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "-m", "flask", "--app", "run", "run", "--host=0.0.0.0", "--port", "8000"]