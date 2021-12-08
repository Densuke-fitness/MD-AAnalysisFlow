FROM jupyter/datascience-notebook
USER root

# Update
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y dist-upgrade
# MeCab + mecab-ipadic-NEologd (/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd)
RUN apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8 file patch make g++ 
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
RUN mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y
RUN pip3 install mecab-python3 oseti
RUN cp /etc/mecabrc /usr/local/etc/