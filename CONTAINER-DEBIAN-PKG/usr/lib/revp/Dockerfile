FROM docker.io/amd64/debian
EXPOSE 80/tcp
EXPOSE 443/tcp

ADD PACKAGE /
ADD bootstrap.sh /

RUN ["/bin/bash", "/bootstrap.sh"]
