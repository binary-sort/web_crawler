
# Web Crawler

Web crawler to crawl images from given web url.

Uses:

* Django
* Django Rest Framework
* Django Rest Swagger

### Running locally

Install requirements:

```sh
pip install -r requirements.txt
```

Run the server:

```sh
python manage.py runserver
```

Visit localhost:8000 for swagger docs.

### Running Locally with docker

Make sure to have the following on your host:

* Docker; if you don’t have it yet, follow the [installation instructions](https://docs.docker.com/install/#supported-platforms);
* Docker Compose; refer to the official documentation for the [installation guide](https://docs.docker.com/compose/install/).

Build the stack:

```sh
docker-compose -f local.yml build
```

Run the stack:

```sh
docker-compose -f local.yml up
```
