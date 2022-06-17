FROM python:3.9

# Install system requirements
RUN apt-get -y update && \
    apt-get -y install --no-install-recommends postgresql-client && \
    # Cleaning cache:
    apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*


WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY app /code/sql_app

COPY bin/app-start.sh /code/app-start.sh
