# PasteBin clone
[![Build Status](https://travis-ci.com/newtonkiragu/django-restful.svg?branch=master)](https://travis-ci.com/newtonkiragu/django-restful)
[![Maintainability](https://api.codeclimate.com/v1/badges/f255d310fa438c258136/maintainability)](https://codeclimate.com/github/newtonkiragu/django-restful/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f255d310fa438c258136/test_coverage)](https://codeclimate.com/github/newtonkiragu/django-restful/test_coverage)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/newtonkiragu/django-restful/blob/master/LICENSE)

#### PasteBin Clone

## Description
A pastebin or text storage site is a type of online content hosting service where users can store plain text, e.g. to source code snippets for code review via Internet Relay Chat. This application allows users to paste their code and share it with others for code review.

#### Link to deployed site
coming soon :-)

## Table of content
1. [Description](#description)
2. [Setup and installations](#setup-and-installations)
3. [Deployment](#deployment)
4. [Contributing](#contributing)
5. [Bugs](#bugs)
6. [Contact me](#support-and-contact-details)
7. [Licensing](#license)


## Setup and installations

#### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
2. [Postgres](https://www.postgresql.org/download/)
3. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
4. [Pip](https://pip.pypa.io/en/stable/installing/)
5. [Django](https://www.djangoproject.com/download/)
5. [Django Rest Framework](http://www.django-rest-framework.org/#installation)

#### Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    - Django, Django Rest Framework

#### Clone the Repo and checkout into the project folder.
```bash
git clone git@github.com:newtonkiragu/django-restful.git && cd django-restful
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='<Secret_key>'
NAME='tutorial'
USER='<Username>'
PASSWORD='<password>'
HOST='localhost'
MODE='dev'
DEBUG=True
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Create the Database
In a new terminal, open the postgresql shell with `psql`.
```bash
CREATE DATABASE tutorial;
```

#### Make and run migrations
```bash
python3.6 manage.py makemigrations && python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

## Deployment
To deploy the application, please follow the instructions in [this gist](https://gist.github.com/newtonkiragu/42f2500e56d9c2375a087233587eddd0)

## Contributing
Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute. Pull requests are welcome :-)

## Bugs
Create an issue mentioning the bug you have found

#### Known bugs
 - cannot subscribe to email list in live application



## Support and contact details
Contact [Newton Karanu](karanunewton4@gmail.com) for further help/support

### License
MIT

Copyright (c)2018 **Newton Karanu**
