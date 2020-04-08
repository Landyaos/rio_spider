FROM ubuntu:latest

MAINTAINER stone (1453793807@qq.com)

# 替换阿里云的源
RUN echo '--------> build rio/scrapy based on ubuntu ...' && \
    echo '--------> update apt-get source : using ustc university ...' && \
    echo 'deb http://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse' > /etc/apt/sources.list && \
    echo 'deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb http://cn.archive.ubuntu.com/ubuntu bionic main multiverse restricted universe' >> /etc/apt/sources.list && \
    echo 'deb http://cn.archive.ubuntu.com/ubuntu bionic-updates main multiverse restricted universe' >> /etc/apt/sources.list && \
    echo 'deb http://cn.archive.ubuntu.com/ubuntu bionic-security main multiverse restricted universe' >> /etc/apt/sources.list && \
    echo 'deb http://cn.archive.ubuntu.com/ubuntu bionic-proposed main multiverse restricted universe' >> /etc/apt/sources.list && \
    # 更新 包管理
    apt-get update && \
    apt-get -y upgrade && \
    echo 'update ... Done'
# 安装python环境 以及其他基础依赖
RUN echo '--------> install python ...' && \
    apt-get install -y python3 && \
    apt-get install -y python3-distutils && \

    echo '--------> install pip ...' && \
    apt-get install -y python3-pip && \

    echo '--------> update pip ...' && \
    mkdir ~/.pip && \
    touch ~/.pip/pip.conf && \
    echo '[global]' >> ~/.pip/pip.conf && \
    echo 'index-url = https://pypi.tuna.tsinghua.edu.cn/simple/' >> ~/.pip/pip.conf && \
    echo '[install]' >> ~/.pip/pip.conf && \
    echo 'trusted-host = pypi.tuna.tsinghua.edu.cn' >> ~/.pip/pip.conf && \
    pip3 install --upgrade pip && \


ADD . /root/rio_spider/
ENV APP_DIR /root/rio_spider
WORKDIR /root/rio_spider

RUN echo 'install requirements' && \
    python3 -m pip install -r requirements.txt && \
    echo '--------> rio/scrapy build SUCCESS <--------'