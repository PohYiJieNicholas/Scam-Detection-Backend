# Scam-Detection-Backend
The back-end application consists of an Application Programming Interface (API) with a POST method that runs a prediction function when called. It will retrieve the request body and use it as the input for classification, and the output will be sent back as a response along with a status message and duration for prediction. The back-end application was also containerize using Docker and the container would be hosted on a Google Cloud Serverless service.

## Download model
Download the trained model and add folder to project directory.

https://drive.google.com/file/d/1aacNp864UPzVWh4zae6iJmkm0LwzqOZ4/view?usp=sharing

## Setup
1. Install the python liberies

```
pip install -r requirements.txt
```

## Run locally
```
python app.py
```
or

```
python3 app.py
```

## Containerize with Docker
1. Download Docker
2. In console navigate to project folder
3. Build Docker image
```
docker build -t *image-name*
```
4. Create Docker container
```
docker compose up
```
or 
using Docker desktop
![Screenshot 2024-07-09 at 7 47 30 PM](https://github.com/PohYiJieNicholas/Scam-Detection-Backend/assets/97501534/7522109f-cc3b-4a4f-bf8e-72ecc4405e65)

![Screenshot 2024-07-09 at 7 48 05 PM](https://github.com/PohYiJieNicholas/Scam-Detection-Backend/assets/97501534/40adf9a8-c4cd-46a8-908b-4df4d4b5672d)
