FROM python:3.10-slim
LABEL authors="mary"

WORKDIR /opt/tools

COPY . /opt/tools/
RUN mkdir /opt/tools/results

# Change to your data if wanted. Originally /data folder is copied to container and can be used
#COPY <path-to-data> /opt/tools/<path-to-data>

# Change to your data if wanted. Originally index program stores files into /opt/tools/results
#COPY <path-to-indexfile> /opt/tools/<path-to-indexfile>
#COPY <path-to-filenames> /opt/tools/<path-to-filenames>

RUN pip3 install -r requirements.txt