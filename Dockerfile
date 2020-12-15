FROM python:3.8-alpine

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt



# Copy project
COPY . .

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]