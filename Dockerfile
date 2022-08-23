FROM python:3.7-alpine
ADD rest_app.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD python3 rest_app.py
