FROM python:3.10-slim
LABEL authors="grg"

WORKDIR /usr/src/app
EXPOSE 5000

RUN pip install --no-cache-dir beautifulsoup4 flask psycopg2-binary requests

COPY .. ./

CMD python3 app.py
