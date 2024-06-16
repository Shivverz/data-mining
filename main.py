import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory

def check_init_db(directory, path, folder_name, model_name, files):
    folder_path = os.path.join(directory, folder_name)
    if not os.path.isdir(folder_path):
        full_directory = os.path.join(directory, folder_name)
        os.makedirs(full_directory, exist_ok=True)
        init_db(full_directory, path, model_name, files)

def init_db(directory, path, model_name, files):
    documents = []

    for file in files:
        loader = PyPDFLoader(os.path.join(path, file))
        documents.extend(loader.load())

    # Initialize text splitter and embeddings
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)
    embeddings = OllamaEmbeddings(model=model_name)

    # Create Chroma vector store
    Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=directory,
    )

def load_db(directory, model_name, chain_type, k):
    embeddings = OllamaEmbeddings(model=model_name)
    db = Chroma(persist_directory=directory, embedding_function=embeddings)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": k})

    template = """
    You are an expert on Portuguese football, specifically the Primeira Liga. Your goal is to provide insightful, accurate, and up-to-date information about teams, players, matches, and statistics. 
    Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know. Do not try to make up an answer.
    Override any outdated information with more recent data provided in the context. Be thorough and ensure your response includes all relevant details from the context.
    
    IMPORTANT: Only provide information directly relevant to the key points mentioned in the question. Do not include information from other seasons or irrelevant details such as game formations unless explicitly asked.
    
    Context:
    {context}
    
    Question: {question}
    
    Guidelines for your answer:
    1. Identify the key points of the question and focus your response on addressing those key points.
    2. Start with a brief summary of the main points related to the question.
    3. Provide detailed information using bullet points or numbered lists to improve readability and clarity.
    4. If applicable, include statistics, historical data, and recent developments to support your answer.
    5. Maintain a polite and professional tone throughout your response.
    6. Ensure that your response only includes information relevant to the season specified in the question or context.
    
    Helpful Answer:
    """

    QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=template)


    qa = RetrievalQA.from_chain_type(
        llm=Ollama(model=model_name, temperature=0),
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )

    return qa

def main(modeln, path):
    files = ["champion.pdf", "standings.pdf", "pt_cup_winners.pdf", "formations.pdf", "intro.pdf", "referees.pdf", "seasons.pdf", "statistics.pdf", "teams.pdf"]
    directory = 'docs/chroma'
    check_init_db('docs/', path, 'chroma', 'mistral', files)
    qa = load_db(directory, modeln, "map_rerank", 5)

    # Memory management for conversation context
    memory = ConversationBufferMemory(output_key='result')  # Explicitly set output_key here
    qa.memory = memory

    while True:
        question = input("Question: ").strip()
        if question.lower() in ['exit', 'quit']:
            break
        result = qa.invoke({"query": question})
        answer = result['result']  # Ensure you access the correct key based on your output structure
        print("Answer: ", answer)

if __name__ == "__main__":
    main("mistral", "./Final_FIles/")
