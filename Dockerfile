FROM python:3.6-jessie

RUN apt update

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt --no-cache-dir

ADD . /app

ENV PORT 8000
CMD ["gunicorn", "api:app", "--config=config.py"]