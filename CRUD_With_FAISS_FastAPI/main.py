# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crud_faiss import FAISSCRUD
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Initialize FAISSCRUD
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
dimension = model.get_sentence_embedding_dimension()
faiss_crud = FAISSCRUD(dimension)

class TextData(BaseModel):
    text: str

@app.post("/create")
async def create_item(data: TextData):
    embedding = model.encode([data.text])[0]
    idx = faiss_crud.create(embedding)
    return {"id": idx}

@app.get("/read/{idx}")
async def read_item(idx: int):
    embedding = faiss_crud.read(idx)
    if embedding is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"embedding": embedding.tolist()}

@app.put("/update/{idx}")
async def update_item(idx: int, data: TextData):
    embedding = model.encode([data.text])[0]
    success = faiss_crud.update(idx, embedding)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated"}

@app.delete("/delete/{idx}")
async def delete_item(idx: int):
    success = faiss_crud.delete(idx)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
