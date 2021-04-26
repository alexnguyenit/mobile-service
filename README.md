# APP Mobile API Version
## Version
1.0.1
## Python Version
Python >= 3.8

## Deploy App

### Install library with local
```
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
```
### Build an image
```
docker build --tag hoangnguyenngoctb/mobileservice .
```
### Tag image
```
docker tag hoangnguyenngoctb/mobileservice:latest hoangnguyenngoctb/mobileservice:v1.0.1
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
### Remove cache file git
```
git rm env.local --cached
```