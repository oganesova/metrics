# Metrics Data Ingestion Pipeline

## Overview

This project sets up a data ingestion pipeline for user metrics, including `talked_time`, `microphone_used`, `speaker_used`, and `voice_sentiment`.
The project uses Docker to orchestrate the application and MySQL database.

## Project Structure

- `app.py`: The Flask application for handling HTTP requests and interacting with the MySQL database.
- `init.sql`: SQL script for initializing the database schema and stored procedures.
- `Dockerfile`: Defines the environment for the Flask application.
- `docker-compose.yml`: Configures and runs Docker containers for the Flask application and MySQL.
- `requirements.txt`: Lists Python dependencies.

### Prerequisites

- Docker and Docker Compose installed on your machine.

### Setup

1. **Clone the Repository**

2.Build and Start Containers

Build and start the Docker containers using Docker Compose:
docker-compose up --build

3.Accessing the Application
Flask Application: Accessible at http://localhost:5000

4. Running the SQL Script Manually
If you need to run the init.sql script manually inside the MySQL container, follow these steps:
Copy the SQL Script into the Container

docker cp init.sql mysql_db:/init.sql
docker exec -it mysql_db /bin/bash
Run the SQL Script - 
mysql -uroot -p1111 metrics_db < /init.sql

Access the MySQL command-line client to check the tables:
mysql -uroot -p1111

USE metrics_db;
SHOW TABLES;

4.Testing the API Endpoints
You can use Postman to test the API endpoints. Here are example JSON payloads for each endpoint:
Endpoints
![image](https://github.com/user-attachments/assets/d37ad824-1ffa-4431-a4f2-823dc4648148)

1. POST /metrics/talked_time
Inserts a record into the talked_time table.

Request
URL: http://localhost:5000/metrics/talked_time
Method: POST
Headers:
Content-Type: application/json
Body:
json

{
  "user_id": 1,
  "session_id": 101,
  "start_time": "2024-08-10T10:00:00",
  "end_time": "2024-08-10T10:30:00",
  "duration": "00:30:00"
}
Response
Success (201 Created):
json

{
  "message": "Data inserted successfully into talked_time"
}
Error (400 Bad Request):
json

{
  "error": "Error message here"
}
2. POST /metrics/microphone_used
Inserts a record into the microphone_used table.

Request
URL: http://localhost:5000/metrics/microphone_used
Method: POST
Headers:
Content-Type: application/json
Body:
json

{
  "user_id": 1,
  "session_id": 101,
  "usage_start": "2024-08-10T10:00:00",
  "usage_end": "2024-08-10T10:30:00"
}
Response
Success (201 Created):
json

{
  "message": "Data inserted successfully into microphone_used"
}
Error (400 Bad Request):
json

{
  "error": "Error message here"
}
3. POST /metrics/speaker_used
Inserts a record into the speaker_used table.

Request
URL: http://localhost:5000/metrics/speaker_used
Method: POST
Headers:
Content-Type: application/json
Body:
json

{
  "user_id": 1,
  "session_id": 101,
  "usage_start": "2024-08-10T10:00:00",
  "usage_end": "2024-08-10T10:30:00"
}
Response
Success (201 Created):
json

{
  "message": "Data inserted successfully into speaker_used"
}
Error (400 Bad Request):
json

{
  "error": "Error message here"
}
4. POST /metrics/voice_sentiment
Inserts a record into the voice_sentiment table.

Request
URL: http://localhost:5000/metrics/voice_sentiment
Method: POST
Headers:
Content-Type: application/json
Body:
json
{
  "user_id": 1,
  "session_id": 101,
  "sentiment_score": 0.85,
  "sentiment_label": "positive"
}
Response
Success (201 Created):

json
{
  "message": "Data inserted successfully into voice_sentiment"
}
Error (400 Bad Request):
json
{
  "error": "Error message here"
}
5. GET /metrics/talked_time
Retrieves all records from the talked_time table.

Request
URL: http://localhost:5000/metrics/talked_time
Method: GET
Response
Success (200 OK):
json
[
  {
    "id": 1,
    "user_id": 1,
    "session_id": 101,
    "start_time": "2024-08-10T10:00:00",
    "end_time": "2024-08-10T10:30:00",
    "duration": "00:30:00",
    "timestamp": "2024-08-10T10:00:00"
  }
  
]
6. GET /metrics/microphone_used
Retrieves all records from the microphone_used table.

Request
URL: http://localhost:5000/metrics/microphone_used
Method: GET
Response
Success (200 OK):
json
[
  {
    "id": 1,
    "user_id": 1,
    "session_id": 101,
    "usage_start": "2024-08-10T10:00:00",
    "usage_end": "2024-08-10T10:30:00",
    "timestamp": "2024-08-10T10:00:00"
  }

]
7. GET /metrics/speaker_used
Retrieves all records from the speaker_used table.

Request
URL: http://localhost:5000/metrics/speaker_used
Method: GET
Response
Success (200 OK):
json

[
  {
    "id": 1,
    "user_id": 1,
    "session_id": 101,
    "usage_start": "2024-08-10T10:00:00",
    "usage_end": "2024-08-10T10:30:00",
    "timestamp": "2024-08-10T10:00:00"
  }
  
]
8. GET /metrics/voice_sentiment
Retrieves all records from the voice_sentiment table.

Request
URL: http://localhost:5000/metrics/voice_sentiment
Method: GET
Response
Success (200 OK):
json
[
  {
    "id": 1,
    "user_id": 1,
    "session_id": 101,
    "sentiment_score": 0.85,
    "sentiment_label": "positive",
    "timestamp": "2024-08-10T10:00:00"
  }
  
]
