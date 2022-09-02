FROM python:3.8-slim

ENV PYTHONUNBUFFERED True
ENV FLASK_APP run.py
ENV PORT 80

COPY run.py requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
