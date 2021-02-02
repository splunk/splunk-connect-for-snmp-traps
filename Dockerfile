FROM registry.access.redhat.com/ubi8/ubi

WORKDIR /work

RUN curl -fsSL https://goss.rocks/install | GOSS_VER=v0.3.13 sh

RUN cd /tmp ;\
    dnf install tzdata curl wget nc python3.8 python3-pip procps-ng -y ;\
    dnf update -y

COPY lookups ./lookups
COPY entrypoint.sh .
COPY dist/*.whl /tmp
COPY config.yaml .
RUN pip3.8 install $(ls /tmp/*.whl); rm -f /tmp/*.whl

EXPOSE 2162/udp
ENTRYPOINT [ "/work/entrypoint.sh" ]
