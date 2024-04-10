FROM python:3.12-slim
LABEL authors="halone"
WORKDIR /app
COPY . .
RUN pip install poetry && poetry config virtualenvs.create false
RUN poetry install
ENTRYPOINT ["poetry", "run", "python", "rest_memory_testing/$(echo $VENDOR)/app.py"]