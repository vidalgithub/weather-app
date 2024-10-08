FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=main.py
ENV APIKEY="18e2928167mshd20e5fa1543fp174f73jsn41b17"
CMD ["flask", "run", "--host=0.0.0.0"]
