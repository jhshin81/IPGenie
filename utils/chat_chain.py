# utils/chat_chain.py

from langchain_core.messages import ChatMessage
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
import streamlit as st
import pickle

# 검색기 생성
def initialize_chain():
    retriever = create_retriever()
    return create_chain(retriever)

# 검색기 및 체인 생성 함수
def create_retriever():
    with open('./model/embedding_ko_sroberta_multitask.pkl', 'rb') as f:
        embedding = pickle.load(f)
    vectordb = Chroma(
        persist_directory='totalDB2_ko-sroberta-multitask',
        embedding_function=embedding,
        collection_name="totalDB20241031"
    )
    return vectordb.as_retriever(search_kwargs={"k": 3})

def create_chain(retriever, model_name="ollama"):
    llm = ChatOllama(model="EEVE-Korean-10.8B:latest", temperature=0)
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

# 채팅 기록 및 메시지 추가 함수
def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)

def add_message(role, message):
    st.session_state["messages"].append(ChatMessage(role=role, content=message))

# 사용자 입력 처리 및 응답 출력
def handle_user_input(user_input):
    chain = st.session_state["chain"]
    st.chat_message("user").write(user_input)
    chat_history = [(msg.role, msg.content) for msg in st.session_state["messages"]]
    response = chain({"question": user_input, "chat_history": chat_history})
    ai_answer = response["answer"]
    
    with st.chat_message("assistant"):
        st.markdown(ai_answer)
    
    add_message("user", user_input)
    add_message("assistant", ai_answer)

