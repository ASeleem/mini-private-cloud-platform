FROM python:3.7 as bld

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
ENV PYTHONPATH=/app

RUN python -m coverage run --source=. -m unittest discover tests/unit/v1/ && python -m coverage report && coverage html

ENTRYPOINT ["/bin/bash"]