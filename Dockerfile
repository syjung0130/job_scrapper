FROM ubuntu:16.04

RUN sed -i s/archive.ubuntu.com/ftp.daumkakao.com/g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update 
RUN apt-get install -y make 
RUN apt-get install -y git unzip 
RUN apt-get install -y wget
RUN apt-get install -y build-essential

# install python3.6
# for use "add-apt-repository command"
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update
RUN apt-get install -y python3.6

# Set environment variables
# ENV PATH=$PATH:/tmp/ndk-toolchain/bin

VOLUME /workdir/job_scrapper
VOLUME /workdir/build

WORKDIR /workdir/build

CMD ["/bin/bash"]
