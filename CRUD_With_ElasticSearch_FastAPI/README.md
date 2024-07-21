
# CRUD Application with ElasticSearch and FastAPI

In this project, we have developed a complete application that performs CRUD (Create, Read, Update, Delete) operations on an Elasticsearch database using Python. We have implemented wrapper functions for each CRUD operation and integrated these functions with the FastAPI framework to expose these operations as RESTful APIs.


## Table of Contents
- Prerequisites
- Setup and Run the Application
- Endpoints
- Testing
- Challenges Faced
- Conclusion
## Prerequisites
- Docker
- Python 3.10+
- Elasticsearch and Kibana Docker images
## Setup and Run the Application
1. Clone the Repsotory
```shell
git clone https://github.com/ParasharAayush/CRUD_With_ElasticSearch_FastAPI.git
cd CRUD_With_ElasticSearch_FastAPI
```
2. Docker setup for Elasticsearch and Kibana
a. Pull Elasticsearch and Kibana Docker Images
```shell
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.3.2
docker pull docker.elastic.co/kibana/kibana:8.3.2
```
b. Run Elasticsearch container
```shell
docker run -d --name elasticsearch -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.3.2
```
c. Run Kibana Container (optional)
```shell
docker run -d --name kibana --link elasticsearch:elasticsearch -p 5601:5601 docker.elastic.co/kibana/kibana:8.3.2
```
3. Elasticsearch Wrapper Configuration
Ensure your elasticsearch_wrapper.py file is configured correctly
```shell
python

from elasticsearch import Elasticsearch, exceptions

class ElasticsearchWrapper:
    def __init__(self):
        self.client = Elasticsearch(
            ['https://localhost:9200'],
            http_auth=('elastic', '123456'),  # Replace '123456' with the actual password you set
            verify_certs=False  # Set to True if you have valid certificates
        )
```
Note: In the code above, verify_certs=False is set to bypass certificate verification for development purposes. Ensure to use valid certificates in production.

4. Run FastAPI Application
```shell
uvicorn main:app --reload
```
The application will be running on http://127.0.0.1:8000



## Endpoints
1. Create a Document
- URL: '/documents/{doc_id}'
- Method: 'POST'
- Request Body:
```shell
{
    "field1": "value1",
    "field2": "value2",
    "field3": "value3",
    "field4": 123
}
```
- Response:
```shell
{
    "_index": "my_index",
    "_type": "_doc",
    "_id": "{doc_id}",
    "_version": 1,
    "result": "created",
    "_shards": {
        "total": 2,
        "successful": 1,
        "failed": 0
    },
    "_seq_no": 0,
    "_primary_term": 1
}
```
2. Read a Document
- URL: '/documents/{doc_id}'
- Method: 'GET'
- Response:
```shell
{
    "_index": "my_index",
    "_type": "_doc",
    "_id": "{doc_id}",
    "_version": 1,
    "found": true,
    "_source": {
        "field1": "value1",
        "field2": "value2",
        "field3": "value3",
        "field4": 123
    }
}
```
3. Update a Document
- URL: '/documents/{doc_id}'
- Method: 'PUT'
- Request Body: 
```shell
{
    "field1": "new_value1",
    "field2": "new_value2",
    "field3": "new_value3",
    "field4": 456
}
```
- Response:
```shell
{
    "_index": "my_index",
    "_type": "_doc",
    "_id": "{doc_id}",
    "_version": 2,
    "result": "updated",
    "_shards": {
        "total": 2,
        "successful": 1,
        "failed": 0
    },
    "_seq_no": 1,
    "_primary_term": 1
}
```
4. Delete a Document
```shell
- URL: '/documents/{doc_id}'
- Method: 'DELETE'
- Response:
```shell
{
    "_index": "my_index",
    "_type": "_doc",
    "_id": "{doc_id}",
    "_version": 3,
    "result": "deleted",
    "_shards": {
        "total": 2,
        "successful": 1,
        "failed": 0
    },
    "_seq_no": 2,
    "_primary_term": 1
}
```
## Testing
Use Postman to test the API endpoints. Ensure that Elasticsearch is running and accessible at 'https://localhost:9200'
## Challenges Faced
1. Docker Installation and Configuration:
- Issue: Encountered an error indicating that the Docker daemon was not running.
- Solution: Verified and started the Docker service to resolve the issue.
2. Elasticsearch and Kibana Setup
- Issue: Configuring Elasticsearch and Kibana to run in Docker containers, ensuring they were accessible.
- Solution: Adjusted Docker run commands and environment variables to correctly start and link the containers.
3. Connecting to Elasticsearch:
- Issue: Faced authentication and connection issues when trying to connect to Elasticsearch from the FastAPI application.
- Solution: Disabled security for development purposes using the environment variable 'xpack.security.enabled=false' in the Elasticsearch Docker command. Also, updated the connection settings in the 'elasticsearch_wrapper.py' file to bypass certificate verification during development by setting 'verify_certs=False' and providing the appropriate 'http_auth' credentials.
4. Implementing and Testing CRUD Operations:
- Issue: Encountered various exceptions and errors while implementing and testing CRUD operations.
- Solution: Added appropriate exception handling for connection errors, authentication errors, and general Elasticsearch exceptions to provide meaningful error messages and ensure robustness.
5. Testing APIs with Postman:
- Issue: Encountered errors during API requests due to misconfigurations and missing fields.
- Solution:  Ensured that the API endpoints were correctly defined and that the request payloads were properly structured. Verified the success of the operations using Postman and Elasticsearch's Kibana interface.
## Conclusion
This project provides a basic setup for creating, reading, updating, and deleting documents in Elasticsearch using FastAPI. It demonstrates the integration of FastAPI with Elasticsearch and containerization using Docker. The detailed setup instructions and robust error handling ensure a smooth development and testing experience.