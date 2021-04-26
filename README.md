# APP Mobile API Version
## Version
1.0.1
## Python Version
Python 3.9.2

## Deploy App

### Install library with local
```
pip install env
pipenv shell
pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy
```
or file in docker
```
pip3 freeze > requirements.txt
```
### Build an image
```
docker build --tag python-docker .
```
### Tag image
```
docker tag python-docker:latest python-docker:v1.0.0
```
### Run container
```
docker run --detach -p 5000:5000 <image>
```

## DELETE APP & FIX ERROR
### Remove Docker Container Stoped
```
docker rm $(docker ps -aq)
```

### Error Docker in windows
```
"C:\Program Files\Docker\Docker\DockerCli.exe" -SwitchDaemon
```
