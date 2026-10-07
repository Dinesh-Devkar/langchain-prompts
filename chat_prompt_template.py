from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

chat_prompt_template=ChatPromptTemplate(messages=[
    ('system',"You are a {domain} expert"),
    ('human','Explain me the {topic} in 2-3 lines.')
    # ,
    # SystemMessage(content="You are a {domain} expert"),
    # HumanMessage(content='Explain me the {topic} in 2-3 lines.')
])

result=chat_prompt_template.invoke({'domain':'Machine Learning','topic':'EDA'})
print(result)