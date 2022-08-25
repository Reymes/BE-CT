FROM python:3

RUN apt-get update

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

WORKDIR /annotate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]