FROM python:3-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install .

EXPOSE 8080

CMD ["python", "mvp_counter/main.py"]