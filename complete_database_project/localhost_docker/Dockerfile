FROM python:3.8-slim-buster

# create a dataset directory
# RUN mkdir /datasets

# copy all the contents of datasets directory to the container datasets directory
COPY datasets /datasets

# copy the app directory to the container app directory

COPY app /app

# copy the requirements.txt file to the container root directory
COPY requirements.txt /

# install the requirements
RUN pip install -r /requirements.txt

# set the working directory to the app directory
WORKDIR /app

# expose port 80
EXPOSE 80

# The below command is used to create and load database in docker container
CMD ["sh", "-c", "python3 data_converter.py && uvicorn main:app --host 0.0.0.0 --port 80"]