# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

RUN mkdir /app

WORKDIR /app/

ADD . /app/

RUN pip install -r requirements.txt

CMD [ "gunicorn", "--blind", "0.0.0.0:5000", "app:app" ]
