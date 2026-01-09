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
    if not 'work' in st.session_state:
        st.session_state.work = False
    if not 'study' in st.session_state:
        st.session_state.study = False
    if not 'health' in st.session_state:
        st.session_state.health = False
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
    st.session_state.work = st.checkbox('Робота')
    st.session_state.study = st.checkbox('Навчання')



st.code(st.session_state, language='json')