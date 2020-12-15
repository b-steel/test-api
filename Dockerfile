FROM python:3.8-alpine

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# migrate
RUN python manage.py migrate

# CMD gunicorn --bind 0.0.0.0:$PORT test_api.wsgi:application
CMD ["/usr/local/bin/python3", "manage.py", "runserver", "0.0.0.0:8000" ]