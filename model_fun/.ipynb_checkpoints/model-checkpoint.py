from langchain_community.llms.ollama import Ollama
from langchain.prompts import ChatPromptTemplate

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def ask_model(prompt,text):
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=text, question=prompt)
    model = Ollama(model="Financial-Advisor-model")
    response_text = model.invoke(prompt)
    return response_text
#    print("llm response---",response_text,"\n---")

#this is used only for 1st run
def ask_model1(text):
    model = Ollama(model="Financial-Advisor-model")
    response_text = model.invoke(text)
    return response_text