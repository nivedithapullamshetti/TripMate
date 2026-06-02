FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN cd travel_planner && python manage.py collectstatic --noinput

EXPOSE 10000

CMD ["sh", "-c", "cd travel_planner && gunicorn wsgi:application --bind 0.0.0.0:10000"]