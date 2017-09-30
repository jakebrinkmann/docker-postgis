FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .

ENV DB_CONFIG_PATH run/config.ini

CMD ["intersect"]
