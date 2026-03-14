
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install numpy matplotlib

CMD ["python", "autograder.py"]