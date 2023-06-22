FROM python:3.9-slim

WORKDIR /app

COPY app1.py /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6000

CMD ["python3", "app1.py"]

