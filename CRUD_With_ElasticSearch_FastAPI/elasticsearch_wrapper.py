from elasticsearch import Elasticsearch, exceptions

class ElasticsearchWrapper:
    def __init__(self):
        self.client = Elasticsearch(
            ['https://localhost:9200'],
            http_auth=('elastic', '123456'),  # Replace 'your_password' with the actual password you set
            verify_certs=False  # Set to True if you have valid certificates
        )

    def create_document(self, index, doc_id, document):
        try:
            response = self.client.index(index=index, id=doc_id, body=document)
            return response
        except exceptions.ConnectionError as e:
            print(f"Connection error: {e}")
            return None
        except exceptions.AuthenticationException as e:
            print(f"Authentication error: {e}")
            return None
        except exceptions.ElasticsearchException as e:
            print(f"Error creating document: {e}")
            return None

    def get_document(self, index, doc_id):
        try:
            response = self.client.get(index=index, id=doc_id)
            return response
        except exceptions.ConnectionError as e:
            print(f"Connection error: {e}")
            return None
        except exceptions.AuthenticationException as e:
            print(f"Authentication error: {e}")
            return None
        except exceptions.ElasticsearchException as e:
            print(f"Error getting document: {e}")
            return None

    def update_document(self, index, doc_id, document):
        try:
            response = self.client.update(index=index, id=doc_id, body={"doc": document})
            return response
        except exceptions.ConnectionError as e:
            print(f"Connection error: {e}")
            return None
        except exceptions.AuthenticationException as e:
            print(f"Authentication error: {e}")
            return None
        except exceptions.ElasticsearchException as e:
            print(f"Error updating document: {e}")
            return None

    def delete_document(self, index, doc_id):
        try:
            response = self.client.delete(index=index, id=doc_id)
            return response
        except exceptions.ConnectionError as e:
            print(f"Connection error: {e}")
            return None
        except exceptions.AuthenticationException as e:
            print(f"Authentication error: {e}")
            return None
        except exceptions.ElasticsearchException as e:
            print(f"Error deleting document: {e}")
            return None

# Test the connection
if __name__ == "__main__":
    es_wrapper = ElasticsearchWrapper()
    print(es_wrapper.client.info())
