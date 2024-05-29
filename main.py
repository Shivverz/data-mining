from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

def load_db(path, model_name, files, chain_type, k):
    #documents = []
#
    #for file in files:
    #    loader = PyPDFLoader(path + file)
    #    documents.extend(loader.load())
#
    #text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    #docs = text_splitter.split_documents(documents)
    embeddings = OllamaEmbeddings(model=model_name)

    # TODO: Mudar isto para uma função à parte no futuro
    #vectordb = Chroma.from_documents(
    #                documents=docs,
    #                embedding=embeddings,
    #                persist_directory='docs/chroma/',
    #           )
    #db = DocArrayInMemorySearch.from_documents(docs, embeddings)  # Using DocArrayInMemorySearch

    #memory = ConversationBufferMemory(
    #    memory_key="chat_history",
    #    return_messages=True
    #)

    db = Chroma(persist_directory='docs/chroma/', embedding_function=embeddings)
    retriever = db.as_retriever(search_type="similarity")

    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
                       You're an expert on Portuguese football, specifically the Primeira Liga. Your goal is to provide insightful, accurate, and up-to-date information about teams, players, matches, and statistics. 
                       Answer questions, offer analysis, and engage in discussions with users who want to know more about the league.

                       {context}
                       Question: {question}
                       Helpful Answer:"""

    QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=template)

    qa = RetrievalQA.from_chain_type(
                llm = Ollama(model=model_name, temperature=0),
                retriever=retriever,
                return_source_documents=True,
                chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
                )

    return qa

def main(modeln, path):
    files = ["champion.pdf", "standings.pdf", "pt_cup_winners.pdf"]
    qa = load_db(path, modeln, files, "map_rerank", 3)

    while True:
        question = input("Question:")
        result = qa.invoke({"query": question.strip()})
        print("Answer: ", result['result'])

if __name__ == "__main__":
    main("mistral", "./Final_FIles/")