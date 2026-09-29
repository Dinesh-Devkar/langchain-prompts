from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

messages=[
    SystemMessage(content='You Are A Helpfuf Assistent'),
    HumanMessage(content='tell me about mumbai city in 2 lines.')

]

model= ChatOpenAI(model='gpt-4o')
result= model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)