FROM python:3.12-slim

WORKDIR /app

COPY ./backend-app .

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]