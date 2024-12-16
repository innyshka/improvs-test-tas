FROM python:3.11

LABEL maintainer = "inna8110302@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && apt-get clean \
RUN pip install psycopg2
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


RUN mkdir -p /vol/web/media


COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
