# Creates Docker Container to run .fit File Battery Check Script
# alex@nerdathlete.de
FROM python:3.9-alpine
COPY . /code
#RUN python3 -m venv /code/venv
COPY requirements.txt /requirements.txt
RUN . /code/venv/bin/activate && pip install -r /requirements.txt
WORKDIR /code
CMD . /code/venv/bin/activate && exec python3 /code/app.py

