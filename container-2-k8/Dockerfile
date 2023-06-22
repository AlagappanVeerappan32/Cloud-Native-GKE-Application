FROM python:3.9-slim

WORKDIR /app

COPY app2.py /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["python3", "app2.py"]
