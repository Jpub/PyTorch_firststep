FROM lucidfrontier45/pytorch

RUN mkdir /webapp
WORKDIR /webapp

COPY requirements.txt /webapp
RUN pip install --no-cache-dir -r requirements.txt

COPY app /webapp/app

COPY taco_burrito.prm /webapp/
COPY wsgi.py /webapp/

ENV PRM_FILE /webapp/taco_burrito.prm

CMD gunicorn --access-logfile - \
             -b 0.0.0.0:8080 -w 4 \
             --preload wsgi:app
