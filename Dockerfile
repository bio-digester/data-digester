from python:latest

env PYTHONUNBUFFERED 1
copy ./start.sh /start.sh
copy . /code
workdir /code

run pip install -r requirements.txt \
    && chmod +x /start.sh

expose 8000
expose 8888

cmd /start.sh
