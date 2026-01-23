import streamlit as st
import uuid
from helpers import MAP_NASTRII
import json
import requests
from datetime import datetime

base_url = 'http://127.0.0.1:8000'


def build_payload():
    payload = {
        "datetime" : str(datetime.now()),
        "nastrii": st.session_state.nastrii,
        "work": st.session_state.impact['work'],
        "health": st.session_state.impact['health'],
        "study": st.session_state.impact['study'],
        "money": st.session_state.impact['money'],
        "partner": st.session_state.impact['partner'],
        "family": st.session_state.impact['family'],
        "friends": st.session_state.impact['friends'],
        "society": st.session_state.impact['society'],
        "date" : st.session_state.impact['date'],
        "events" : st.session_state.impact['events'],
        "weather" : st.session_state.impact['weather'],
        "other" : st.session_state.impact['other'],
        "sleep_hours": st.session_state.sleep_hours,
        "note": st.session_state.note
    }
    return payload



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
    if not 'sleep_hours' in st.session_state:
        st.session_state.sleep_hours = None
    if not 'note' in st.session_state:
        st.session_state.note = None
        
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
    
st.header('Скільки ви спали?')
st.session_state.sleep_hours = st.segmented_control(options=['До 2 годин', '2-4 годин', '4-6 годин', '6-8 годин', '8-10 годин','10-12 годин', 'Понад 12 годин'], label='none', label_visibility='collapsed')


st.header('Опишіть ваш день')
note = st.text_area(label='none', label_visibility='collapsed', height=200)

if st.button('Зберегти', key='save_button', type='secondary', use_container_width=True):
    st.session_state.note = note
    payload = build_payload()
    response = requests.post(f"{base_url}/save", json=payload)
    if response.status_code == 200:
        st.success("Дані успішно збережено!")
        st.json(response.json())
    else:
        st.error("Сталася помилка під час збереження.")
        st.text(f"Status Code: {response.status_code}")
        st.text(f"Response: {response.text}")