FROM python:stretch


WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
    && apt-get install -y netcat \
    && apt-get clean

RUN pip3 install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
# COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

RUN pip3 install -r requirements.txt

# RUN chmod +x /usr/src/app/entrypoint.sh

COPY . /usr/src/app

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]