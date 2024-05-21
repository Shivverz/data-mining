from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain_core.messages import get_buffer_string
from langchain_core.prompts import format_document
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.runnables import RunnableLambda,RunnablePassthrough
from langchain.memory import ConversationBufferMemory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from operator import itemgetter

condense_question = """
Instruction:
You are an expert on Portuguese football, specifically the Primeira Liga. Your goal is to condense and focus the user's question to its core essence, removing any unnecessary details while retaining the key information needed to provide an accurate and insightful response. If there is no research to answer the question just say that you are not able to answer that question.


Follow Up Input:{question}

Standalone question:
"""

CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(condense_question)


ans= """
Instruction: 
You're an expert on Portuguese football, specifically the Primeira Liga. Your goal is to provide insightful, accurate, and up-to-date information about teams, players, matches, and statistics. 
Answer questions, offer analysis, and engage in discussions with users who want to know more about the league.
If there is no reasearch to answer the question just say that you are not able to answer that question.


##Research:
{context}

##Question:
{question}

"""
ANSWER_PROMPT = ChatPromptTemplate.from_template(ans)


DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(
    template="Source Document: {source}, Page {page}:\n{page_content}"
)


def _combine_documents(
    docs, document_prompt=DEFAULT_DOCUMENT_PROMPT, document_separator="\n\n"
):
    doc_strings = [format_document(doc, document_prompt) for doc in docs]
    return document_separator.join(doc_strings)

memory=ConversationBufferMemory(
    return_messages=True,output_key="answer", input_key="question"
)

def getChatChain(llm,db):
    retriever=db.as_retriever(search_kwargs={"k":10})

    loaded_memory= RunnablePassthrough.assign(
        chat_history=RunnableLambda(memory.load_memory_variables)
        | itemgetter("history")
    )

    standalone_question= {
        "standalone_question": {
            "question": lambda x: x["question"],
            "chat_history": lambda x: get_buffer_string(x["chat_history"]),
        }
        | CONDENSE_QUESTION_PROMPT
        | llm
    }

    retrieved_documents={
        "docs": itemgetter("standalone_question") |retriever,
        "question": lambda x : x["standalone_question"],
    }

    final_inputs={
        "context":lambda x: _combine_documents(x["docs"]),
        "question": itemgetter("question"),
    }

    answer = {
        "answer": final_inputs 
        | ANSWER_PROMPT 
        | llm.with_config(callbacks=[StreamingStdOutCallbackHandler()]),
        "docs": itemgetter("docs"),
    }

    final_chain= loaded_memory| standalone_question| retrieved_documents| answer

    def chat(question:str):
        inputs={"question":question}
        result=final_chain.invoke(inputs)
        #memory.save_context(inputs,{"answer":result[answer]})
        return result["answer"]

    return chat