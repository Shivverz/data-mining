import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

def process_docs(path):
    if not os.path.exists(path):
        print("This path doesn’t exist: " + path)
        return []

    loader = DirectoryLoader(
        path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True,
        use_multithreading=True
    )

    documents = loader.load()
    return documents


