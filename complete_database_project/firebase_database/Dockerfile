#
FROM python:3.8-slim-buster

# copy the contents of the local app directory to the app directory
COPY ./app /app

COPY ./requirements.txt .
# install the requirements

# installing all the python modules in the requirements.txt file
RUN pip install -r requirements.txt

# setting the app directory has working directory
WORKDIR /app

# exposing the port
EXPOSE 80

# command to run the restapi when docker container is started
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
