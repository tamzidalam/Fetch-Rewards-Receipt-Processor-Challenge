# Fetch-Rewards-Receipt-Processor-Challenge



## Description
In this API challenge two endpoints have been created Process Receipts endpoints and Get Points.

The "Process Receipts" endpoint receives a JSON representation of a receipt and generates a unique ID for it. This ID is crucial for retrieving the number of points awarded to the receipt later on. The points awarded are determined based on specific rules.

Example Response

```bash
{ "id": "7fb1377b-b223-49d9-a31a-5a02701dd310" }
```

The "Get Points" endpoint is a getter endpoint designed to fetch the number of points awarded to a receipt identified by its ID. It retrieves the points based on the rules defined and returns them in a JSON object.

Example Response:

```bash
{ "points": 32 }
```

## Prerequisite

- Docker installed on your local machine.

## How to Run
1. Clone the Repository:
```bash
git clone https://github.com/tamzidalam/Fetch-Receipt-Processor-Challenge.git
```
2. Navigate to the Project Directory:
```bash
cd <project_directory>
```
3. Pull Docker Image:
```bash
docker pull tamzidalam/fetch:final
```
4. Run Docker Container:
```bash
docker container run -d -p 8000:8000 tamzidalam/fetch:final
```

## Accessing the Application

Once the Docker container is running, you can access the application by navigating to http://localhost:8000 in your web browser.

### Endpoint: Process Receipts

- **Path**: /receipts/process  
- **Method**: POST  
- **Payload**: Receipt JSON  
- **Response**: JSON containing an id for the receipt
- **Accessible URL**: http://localhost:8000/receipts/process


Endpoint: Process Receipts
Path: /receipts/process
Method: POST
Payload: Receipt JSON
Response: JSON containing an id for the receipt

Accessible URL: http://localhost:8000/receipts/process

### Endpoint: Get Points
- **Path** : /receipts/{id}/points
- **Method**: GET
- **Response**: A JSON object containing the number of points awarded.
- **Accessible URL**: http://localhost:8000/receipts/id/points



