import os
from elasticsearch import Elasticsearch

# Connecting to Elasticsearch
es = Elasticsearch("http://elasticsearch:9200")


# Indexing documents from a directory
def index_documents(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        with open(file_path, "r") as f:
            content = f.read()
            es.index(index="documents", body={"content": content, "file_path": file_path})


# Getting the path to the documents folder
documents_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "", "documents")

# Calling the indexing function
index_documents(documents_folder)
