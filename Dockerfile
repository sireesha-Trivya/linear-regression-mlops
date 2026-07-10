FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Train the model while building the image
RUN python train.py

EXPOSE 5000

CMD ["python", "app.py"]
