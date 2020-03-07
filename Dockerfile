FROM python:3.7

RUN mkdir -p /opt/python_service_expose_metrics/src
COPY ./requirements.txt /opt/python_service_expose_metrics/
COPY ./src/app.py /opt/python_service_expose_metrics/src/
RUN pip install -r /opt/python_service_expose_metrics/requirements.txt

WORKDIR /opt/python_service_expose_metrics/
ENV PYTHONPATH '/opt/python_service_expose_metrics/'

CMD ["python" , "/opt/python_service_expose_metrics/src/app.py"]
