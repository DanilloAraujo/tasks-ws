# crud_ws Back-end implementation

## Guide for installation in Ubuntu 16

Run:
``` bash
docker-compose up -d

docker-compose run --rm django python manage.py migrate

docker-compose run --rm django python manage.py createsuperuser

```


Access: http://localhost:8000/admin/

Enter with your username and password

Create OAuth Application

Import Tasks.postman_collection.json to yout postman and update the Client ID and Client Secret.