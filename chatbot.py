from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o')

chat_history=[
    SystemMessage(content='You are a helpful assistent')
]

while True:
    user_Input= input('You : ')
    chat_history.append(HumanMessage(content=user_Input))
    if user_Input== 'Exit':
        break
    result= model.invoke(chat_history)
    print(f"AI : {result.content}")
    chat_history.append(AIMessage(result.content))

print("========================================")
print(chat_history)