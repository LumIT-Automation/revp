FROM docker.io/amd64/debian:bullseye
LABEL AUTOMATION_CONTAINER_IMAGE="revp"
EXPOSE 80/tcp
EXPOSE 443/tcp

ADD PACKAGE /
ADD bootstrap.sh /

RUN ["/bin/bash", "/bootstrap.sh"]
