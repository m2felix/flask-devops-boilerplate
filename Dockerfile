FROM python:3.11-slim

WORKDIR /app
COPY app/ app/
RUN pip install --no-cache-dir -r app/requirements.txt
RUN pytest app/test_app.py

CMD ["python", "app/main.py"]

