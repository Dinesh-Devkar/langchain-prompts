from langchain_core.prompts import MessagesPlaceholder
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

chat_prompt_template= ChatPromptTemplate(messages=
                                         [('system','You are a helpful customer support agent'),
                                          MessagesPlaceholder(variable_name='chat_history'),
                                          ('human','where is my refund')]
                                         )

chat_history=[
    HumanMessage(content="I want to request a refund for my order #12345."),
    AIMessage(content="Your refund request for order #12345 has been initiated. It will be processed in 3-5 business days.")
]

prompt=chat_prompt_template.invoke({'chat_history':chat_history})
print(prompt)
print("=====================================================================")
model=ChatOpenAI(model='gpt-4o')
result=model.invoke(prompt)
print(result)