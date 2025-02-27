# Spy Cat Agency Project

## Installation

You need to clone this project on your local machine from GitHub repo.

```bash
git clone https://github.com/maxlapchuk/spy-cat-agency.git
```

Then you need to create virtual environment and install all project dependencies
```bash
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

Run the migrations
```bash
python manage.py migrate
```

You need to create an .env file in the project directory and add DJANGO_SECRET_KEY (see .env.example).
If you don't have one, use this
```bash
django-insecure-u9%$%cwgz^ok!5^67*89_7xd@h!h4bjz&ismh-z3=ue-r(a0==
```

And after all that, you can run the server
```bash
python manage.py runserver
```

## Using

There is a Postman collection with all the endpoints listed:

https://www.postman.com/maxlapchuk/workspace/spy-cat-agency/collection/32288069-6e98dd62-14f6-476c-8120-7037a98fb4e2?action=share&creator=32288069