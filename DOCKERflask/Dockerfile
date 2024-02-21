FROM python:3
WORKDIR /usr/src/pythonapp
COPY requirements.txt /usr/src/pythonapp/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000
CMD [ "python","flask_program.py" ]
