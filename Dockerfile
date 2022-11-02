FROM jupyter/datascience-notebook
USER root

RUN apt-get -y upgrade
RUN apt-get -y dist-upgrade