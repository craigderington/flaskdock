FROM ubuntu:latest
MAINTAINER Craig Derington "craig@craigderington.me"
RUN apt -y update
RUN apt install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
