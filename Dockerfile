FROM python:3.9

COPY models/tuned_gpt_model /home/.models/tuned_gpt_model

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

ENV FLASK_APP=app.py

CMD ["python",  "app.py"]