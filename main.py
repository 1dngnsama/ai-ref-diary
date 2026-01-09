import streamlit as st
import uuid
from helpers import MAP_NASTRII


st.set_page_config(
    page_title='helper',
    page_icon='random',
    layout='wide'
    )
st.title('AI Щоденник рефлексії', anchor=False)
def init_session_state():
    if not 'nastrii' in st.session_state:
        st.session_state.nastrii = -2
    if not 'impact' in st.session_state:
        st.session_state.impact = {}
    
init_session_state()

st.header('Як ви зараз?', anchor=False)


st.session_state.nastrii = MAP_NASTRII[st.select_slider(
    options=['Дуже погано', 'Погано', 'Скоріше погано', 'Нейтрально','Скоріше добре',"Добре", "Дуже добре"],
    label= 'Оцініть ваш настрій прямо зараз!',
    label_visibility='collapsed'
    )]
st.header('Що зараз найбільше впливає на ваш стан?', anchor=False)

c1,c2,c3 = st.columns(3)
with c1:
    st.session_state.impact['work'] = st.checkbox("Робота")
    st.session_state.impact['health'] = st.checkbox("Здоров'я")
    st.session_state.impact['study'] = st.checkbox("Навчання")
    st.session_state.impact['money'] = st.checkbox("Гроші")
with c2:
    st.session_state.impact['partner'] = st.checkbox('Партнер')
    st.session_state.impact['family'] = st.checkbox("Сім'я")
    st.session_state.impact['friends'] = st.checkbox("Друзі")
    st.session_state.impact['society'] = st.checkbox("Суспільство") 
with c3:
    st.session_state.impact['date'] = st.checkbox("Побачення")
    st.session_state.impact['events'] = st.checkbox("Поточні події")
    st.session_state.impact['weather'] = st.checkbox("Погода")
    st.session_state.impact['other'] = st.checkbox("Інше")
    



st.write(st.session_state)