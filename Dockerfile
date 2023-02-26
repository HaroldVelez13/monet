FROM python:3.11-alpine

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt /requirements.txt
COPY ./docker-entrypoint.sh /app/docker-entrypoint.sh

RUN pip3 install --upgrade pip --no-cache-dir \
    && pip install psycopg2\ 
    && pip3 install -r requirements.txt --no-cache-dir


WORKDIR /app
COPY ./app /app
RUN adduser -D user
USER user

ENTRYPOINT ["sh", "/app/docker-entrypoint.sh"]