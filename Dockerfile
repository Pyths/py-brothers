FROM python:3.6-alpine
WORKDIR app
COPY src src
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 8070
ENTRYPOINT ["python3", "src/brothers.py"]