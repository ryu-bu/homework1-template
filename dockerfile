FROM debian:latest
ENTRYPOINT ["linux32"]
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt-get update -y
RUN apt-get install -y wget
RUN apt-get install -y python3-pip python-dev build-essential
WORKDIR /app

# set up docker repository
RUN apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# set up docker engine
RUN wget -c https://download.docker.com/linux/static/stable/aarch64/docker-18.09.0.tgz
RUN tar xzvf docker-18.09.0.tgz
RUN cp docker/* /usr/bin/
RUN dockerd &

COPY source /app
RUN pip3 install -r requirements.txt
CMD ["flask", "run"]
