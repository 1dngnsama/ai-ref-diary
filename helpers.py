import json


nst = ['Дуже погано', 'Погано', 'Скоріше погано', 'Нейтрально','Скоріше добре',"Добре", "Дуже добре"]
MAP_NASTRII = dict(zip(nst, [i for i in range(-3, 4, 1)]))


def build_payload():
    payload = {
        "nastrii": st.session_state.nastrii,
        "impact": st.session_state.impact,
        "sleep_hours": st.session_state.sleep_hours,
        "day": st.session_state.day
    }
    return payload
