from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory



load_dotenv()

llm=ChatOpenAI(model='gpt-4o')

chat_history=ChatMessageHistory()


# prompt=ChatPromptTemplate(messages=[
#     ('system',"you are a helpful polite and very kind assistent"),
#     ('human',"Summarize the below story in 2-3 lines : {story}")
#     # SystemMessage("you are a helpful polite and very kind assistent"),
#     # HumanMessage("Summarize the below story in 2-3 lines : {story}")
# ])

# prompt=ChatPromptTemplate(messages=[
#     ('system',"you are a helpful polite and very kind assistent"),
#     ('human',"Summarize the below story in 2-3 lines : {story}")
#     # SystemMessage("you are a helpful polite and very kind assistent"),
#     # HumanMessage("Summarize the below story in 2-3 lines : {story}")
# ])

parser=StrOutputParser()

# chain = prompt | llm | parser

# print(chain.invoke({'story':'Ramayan'}))


prompt =ChatPromptTemplate([
    ('system',"you are a helpful assistent who gives answers of user query into hindi language"),
    (MessagesPlaceholder(variable_name="chat_history")),
    ('human',"{input}")
])


while True :
    print(f"Current History : {chat_history.messages} \n")
    print("\n =============================================================================")
    user_input= input('You : ')

    if user_input.lower()=='exit':
        break
    chain= prompt | llm | parser
    result= chain.invoke({'input':user_input,'chat_history':chat_history.messages})

    print(f"AI : {result} \n")

    chat_history.add_user_message(user_input)
    chat_history.add_ai_message(result)

print("=============================== CHAT END ===================================")

print(chat_history.messages)




