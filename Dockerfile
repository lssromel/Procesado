From ubuntu:16.04
MAINTAINER Romel Barrios <lssromel@outlook.com>

RUN apt-get update && apt-get install -y --no-install-recommends \
	python-dev \ 
	python-pip \
	git \
	vim \
	build-essential
RUN pip install -U pip
RUN pip install pymongo 
RUN pip install setuptools 
RUN pip install import_file pandas
RUN pip install xlrd
RUN pip install tables
RUN pip install "bokeh==0.11.0"
WORKDIR /workspace
RUN git clone https://github.com/lssromel/Procesado.git
WORKDIR /workspace/Procesado
