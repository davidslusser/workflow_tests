FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install flask gunicorn

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app.app:app"]
