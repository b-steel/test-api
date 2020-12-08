FROM python:3.8
WORKDIR /usr/src/test_api
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
EXPOSE 8050
RUN python manage.py makemigrations api
RUN python manage.py migrate
CMD [ "python" , "./manage.py", "runserver", "0.0.0.0:8075"]