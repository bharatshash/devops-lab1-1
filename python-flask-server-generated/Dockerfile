FROM python:3.9-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

#EXPOSE MONGO_URL = "mongodb://user:password@mongo:27017/?directConnection=true"

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]