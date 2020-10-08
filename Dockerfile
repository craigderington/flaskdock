FROM ubuntu:latest
MAINTAINER Craig Derington "craigderington17@gmail.com"
RUN apt -y update
RUN apt install -y python3-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5880
CMD ["gunicorn", "-b", "0.0.0.0:5880", "-w", "2", "app:app"]
