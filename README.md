# NOTE API📝
#### Django REST framework

## ⚙️ Installation

Python3 must be already installed.

```shell
git clone https://github.com/innyshka/improvs-test-tas.git
cd improvs_test_task
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
#create .env file based on env.sample
python manage.py migrate
python manage.py runserver #starts Django server
```

## 🐳 Run with Docker

[Docker](https://www.docker.com/products/docker-desktop) should be installed.
```shell
docker-compose up --build
```

## ✅ Accessing the Application

You can now access the API by opening your web browser 
and navigating to http://localhost:8000.

#### 📍 Available urls
- create user `api/user/register/`
- get access token `api/user/login/`
- refresh token `api/user/token/refresh/`

- create note `api/notes/create/`
- get all notes `api/notes/`
- get note by id `api/notes/detail/<id>/`
- update note by id `api/notes/update/<id>/`
- delete note by id `api/notes/delete/<id>/`

#### 📃 Documentation
- `api/docs/`


## ✨ Features
- JWT Authenticated
- Documentation is located in `api/docs/`
- CRUD for Notes
