FROM python:3.11
COPY . /app_dir
WORKDIR /app_dir
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:my_app