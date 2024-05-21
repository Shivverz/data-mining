from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain_core.messages import get_buffer_string
from langchain_core.prompts import format_document
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from operator import itemgetter


condense_question_resp = """
Instruction:
You are an expert on Portuguese football, specifically the Primeira Liga. Your goal is to condense and focus the user's question to its core essence, removing any unnecessary details while retaining the key information needed to provide an accurate and insightful response. If there is no research to answer the question just say that you are not able to answer that question.

## Original Question

{question}

## Condensed Question
"""

CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(condense_question_resp)


resp= """
Instruction: 
You're an expert on Portuguese football, specifically the Primeira Liga. Your goal is to provide insightful, accurate, and up-to-date information about teams, players, matches, and statistics. 
Answer questions, offer analysis, and engage in discussions with users who want to know more about the league.
If there is no reasearch to answer the question just say that you are not able to answer that question.


##Question

{question}

"""
PROMPT = ChatPromptTemplate.from_template(resp)



def getChatChain(llm, db):

    standalone_question = {
            "question": lambda x: x["question"]
        | CONDENSE_QUESTION_PROMPT
        | llm
    }


    # Now we construct the inputs for the final prompt
    final_inputs = {
        "question": itemgetter("question")
    }

    # And finally, we do the part that returns the answers
    answer = {
        "answer": final_inputs
        | PROMPT
        | llm.with_config(callbacks=[StreamingStdOutCallbackHandler()]),
        "docs": itemgetter("docs"),
    }

    final_chain = standalone_question | answer 

    def chat(question: str):
        inputs = {"question": question}
        result = final_chain.invoke(inputs)
        return result["answer"]

    return chat