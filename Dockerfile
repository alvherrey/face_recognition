FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y build-essential cmake
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY app .
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]