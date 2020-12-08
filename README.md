[![Build Status](https://travis-ci.org/5starkarma/RESTfulServerArchitectureTest.svg?branch=master)](https://travis-ci.org/5starkarma/video-razor) [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# RESTful Server Architecture Test

A coding test for Bixly Python/Django Back-end position.

---

### Installing and Testing Locally
```
git clone https://github.com/5starkarma/RESTfulServerArchitectureTest.git
cd RESTfulServerArchitectureTest
```
### Create and Activate New VirtualEnv
```
mkdir venv
python3 -m venv venv
source venv/bin/activate
```
### Install required packages
```
pip install -r requirements.txt 
```
### Make sure sqlite came along and has been migrated
```
python3 manage.py makemigrations users
python3 manage.py makemigrations
python3 manage.py migrate
```
### Runserver
```
python3 manage.py runserver
```
## Test APIs using curl
### Create user
#### POST
```yaml
{
    "username": "test_user",
    "password": "test_password"
}
```
```
http://127.0.0.1:8000/users/create/
```
### Get JWT

#### POST
```yaml
{
    "username": "test_user",
    "password": "test_password"
}
```
```
http://127.0.0.1:8000/api/token/
```
- Copy "access" value
- Select "Authorization" tab > Select "Bearer Token"
- Paste "access" value into "token" field
- Submit Get, Post, Put, and Delete requests to resource as such:

### Get Boat List
#### GET
```
http://127.0.0.1:8000/boats/
```
### Create Boat Object
#### POST
```yaml
{
    "make": "Sky",
    "model": "Supreme",
    "year": 2020,
    "length": "14 ft",
    "width": "8 ft",
    "hin": "xyxyxyxyyx",
    "current_hours": 201,
    "service_interval": 100,
    "next_service": 301
}
```
```
http://127.0.0.1:8000/boats/
```
