FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code


RUN apt-get update -yqq \
  && apt-get install -yqq --no-install-recommends \
    postgresql-client \
  && rm -rf /var/lib/apt/lists

WORKDIR /user/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0
