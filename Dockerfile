# set base image (host OS)
FROM python:3.7

# set the working directory in the container
RUN mkdir /code
WORKDIR /code
ADD . /code/

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
EXPOSE 5000
CMD [ "python", "/code/main.py" ]