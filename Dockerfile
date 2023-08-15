FROM ubuntu:18.04

MAINTAINER John Ziegler "zieglerj1@sou.edu"

RUN apt-get update -y

RUN apt-get install -y python-pip

COPY /MedfordCharities /app

WORKDIR /app

RUN pip install --no-cache -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
