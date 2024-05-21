from langchain.text_splitter import RecursiveCharacterTextSplitter
from documents_load import process_docs
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama


from llm import getChatChain

# Configuração do divisor de texto
SPLITTER = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=100)

def load_docs_db(model, path) -> Chroma:
    try:
        # Processa os documentos a partir do caminho fornecido
        preprocessed_docs = process_docs(path)
        # Divide os documentos em partes menores
        docs = SPLITTER.split_documents(preprocessed_docs)
        
        # Cria embeddings dos documentos
        embeddings = OllamaEmbeddings(model=model)
        # Inicializa o banco de dados vetorial Chroma com persistência
        db = Chroma(persist_directory="../Files_DB", embedding_function=embeddings)
        
        return db
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e}")
        raise

def main(modeln, path):
    try:
        db = load_docs_db(modeln, path)
    except FileNotFoundError as f:
        print(f)
        return

    llm = Ollama(model=modeln)
    conv = getChatChain(llm, db)

    while True:
        try:
            input_us = input("\nType Your Question to FootballPro. Type 'quit' to exit: ")
            if input_us.lower() == "quit":
                break
            response = conv(input_us)  # Aqui chamamos a função retornada por getChatChain
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main("mistral", "/home/jbtescudeiro16/4ANO2SEM/DataMining/Final_FIles")
