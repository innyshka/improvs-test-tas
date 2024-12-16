FROM python:3.11

LABEL maintainer = "inna8110302@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


RUN mkdir -p /vol/web/media


COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
