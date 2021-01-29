# pull base image

FROM python:3



#Set enviromental variables

ENV PYTHONWRITE4BYTECODE 1
ENV PYTHONUNBUFFERED 1


#  Set work directory

WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/