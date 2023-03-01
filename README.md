# MONET TEST

Classroom application made in Django, with Django rest framework for the rest api and using the Django site admin.

## Description.

This app manages students, teachers, tests, questions and answers in a classroom.

### Teachers.

Teachers can login from the django admin, they can manage teachers, students, tests, and questions. And they will be able to see the students' answers.
`http://localhost:8000/admin/login/`

### Students.

Students will be able to login from the django admin, where they will be able to see their answers.
`http://localhost:8000/admin/login/`

### Students and Api Rest.

Through apirest students will be able to log in to get their JWTs and list the tests and their questions, as well as manage their answers.

- `http://localhost:8000/api/login/`
- `http://localhost:8000/api/test/`
- `http://localhost:8000/api/answer/`
- `Authorization : Bearer {token}`

Format for create a Answer

```bash
    {
        "question":{question_id},
        "selected_option":{seleted}
    }
```

## Install.

The installation is facilitated with the use of docker, to do this you must run:

```bash
docker compose up --build
```

Or

```bash
docker compose up
```

This will start the docker container and download the necessary dependencies for its use, as well as generate a postgres database.
Adicionamelte will start the application by executing the commands described in the file `docker-entrypoint.sh`.

- Checking of pending migrations.

```bash
python manage.py makemigrations
python manage.py makemigrations api
```

- Execution of database migrations

```bash
python manage.py migrate
python manage.py migrate api
```

- Creating a superuser for the administration site

```bash
python manage.py monet_init
```

- Test execution.

```bash
python manage.py test
```

If you don't use docker, you can initialize this app as any Django project and run the above commands separately. Remember to include the requirements.txt file in the app folder.
