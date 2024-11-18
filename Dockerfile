FROM python:3.11-alpine

COPY requirements.txt requirements.txt

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main.app", "--host", "0.0.0.0", "--port", "80"]