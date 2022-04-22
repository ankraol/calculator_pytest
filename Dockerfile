FROM python:3.6-slim

COPY . /python_tests_calculator

WORKDIR /python_tests_calculator/

RUN pip install --no-cache-dir -r requirments.txt

RUN ["pytest", "-v", "--junitxml=reports/result.xml"]

CMD tail -f /dev/null