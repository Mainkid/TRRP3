FROM python:3.6
COPY . usr/TRRP3_Server
RUN pip install psycopg2
RUN pip install grpcio-tools
ENV PYTHONPATH /usr
WORKDIR usr/TRRP3_Server/
EXPOSE 5432
CMD ["python","-u","main.py"]