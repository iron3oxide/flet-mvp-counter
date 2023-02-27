FROM python:3-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .

COPY . .

EXPOSE 8080

CMD ["python", "mvp_counter/main.py"]