FROM python:3.9


WORKDIR /usr/src/flaskblog

ADD . /usr/src/flaskblog

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]