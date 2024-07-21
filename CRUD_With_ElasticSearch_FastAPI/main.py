from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from elasticsearch_wrapper import ElasticsearchWrapper

# Initialize FastAPI app
app = FastAPI()

# Initialize Elasticsearch wrapper
es_wrapper = ElasticsearchWrapper()

# Define Pydantic model for data validation
class Document(BaseModel):
    field1: str
    field2: str
    field3: str
    field4: int

# Create a document
@app.post("/documents/{doc_id}")
async def create_document(doc_id: str, doc: Document):
    response = es_wrapper.create_document("my_index", doc_id, doc.dict())
    if not response:
        raise HTTPException(status_code=500, detail="Error creating document")
    return response

# Read a document
@app.get("/documents/{doc_id}")
async def read_document(doc_id: str):
    document = es_wrapper.get_document("my_index", doc_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

# Update a document
@app.put("/documents/{doc_id}")
async def update_document(doc_id: str, doc: Document):
    response = es_wrapper.update_document("my_index", doc_id, doc.dict())
    if not response:
        raise HTTPException(status_code=500, detail="Error updating document")
    return response

# Delete a document
@app.delete("/documents/{doc_id}")
async def delete_document(doc_id: str):
    response = es_wrapper.delete_document("my_index", doc_id)
    if not response:
        raise HTTPException(status_code=500, detail="Error deleting document")
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
