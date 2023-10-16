FROM unit:1.31.0-python3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app /app/

COPY ./unit.json /docker-entrypoint.d/unit.json

