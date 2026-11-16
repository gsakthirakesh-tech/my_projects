
from uuid import uuid4

from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

from settings import api_key, collection_name, model, url


client = QdrantClient(url=url, api_key=api_key)

embedder = SentenceTransformer(model)


# CREATE COLLECTION
def create_collection():

    if not client.collection_exists(collection_name):

        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=384,
                distance=models.Distance.COSINE
            )
        )

        print("Collection created!")


# CREATE DOCUMENT
def create_document(text, category):

    vector = embedder.encode(text).tolist()
    document_id = str(uuid4())

    client.upsert(
        collection_name=collection_name,
        points=[
            models.PointStruct(
                id=document_id,
                vector=vector,
                payload={
                    "text": text,
                    "category": category
                }
            )
        ]
    )

    return document_id


# READ DOCUMENT
def read_document(document_id):

    result = client.retrieve(
        collection_name=collection_name,
        ids=[document_id],
        with_payload=True
    )

    return [
        {
            "id": str(point.id),
            "payload": point.payload
        }
        for point in result
    ]


# UPDATE DOCUMENT
def update_document(document_id, new_text, new_category):

    vector = embedder.encode(new_text).tolist()

    client.upsert(
        collection_name=collection_name,
        points=[
            models.PointStruct(
                id=document_id,
                vector=vector,
                payload={
                    "text": new_text,
                    "category": new_category
                }
            )
        ]
    )

    return document_id


# DELETE DOCUMENT
def delete_document(document_id):

    client.delete(
        collection_name=collection_name,
        points_selector=models.PointIdsList(
            points=[document_id]
        )
    )

    return "Document deleted successfully"


# SEARCH DOCUMENTS
def search_documents(query):

    vector = embedder.encode(query).tolist()

    results = client.query_points(
        collection_name=collection_name,
        query=vector,
        limit=5,
        with_payload=True
    )

    return [
        {
            "id": str(point.id),
            "score": point.score,
            "payload": point.payload
        }
        for point in results.points
    ]


# MAIN FUNCTION
def main():

    # create_collection()

    # document_id = create_document(
    #     "Python is a programming language",
    #     "Programming"
    # )
    # print("Document ID:", document_id)

    # Read document
    # print("Read document:", read_document("b876e256-b001-4d22-9ae0-e176aa96471e"))

    # # Update document
    # document_id = update_document("b876e256-b001-4d22-9ae0-e176aa96471e", "Java is a programming language", "...")

    # # Delete document
    # # print(delete_document(b876e256-b001-4d22-9ae0-e176aa96471e))

    # Search documents
    # print(
    #     'search_documents("what is java ?"): ',
    #     search_documents("what is java ?")
    # )


if __name__ == "__main__":
    main()
