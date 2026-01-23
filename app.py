from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Optional
import sqlite3
from logger_config import logger


conn = sqlite3.connect('diary.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


cursor.execute(
    '''
CREATE TABLE IF NOT EXISTS diary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime TEXT,
    nastrii INTEGER,
    work BOOLEAN,
    health BOOLEAN,
    study BOOLEAN,
    money BOOLEAN,
    partner BOOLEAN,
    family BOOLEAN,
    friends BOOLEAN,
    society BOOLEAN,
    date BOOLEAN,
    events BOOLEAN,
    weather BOOLEAN,
    other BOOLEAN,
    sleep_hours TEXT,
    note TEXT
)
    '''
)

app = FastAPI()

class DiaryEntry(BaseModel):
    nastrii: int
    work: bool
    health: bool
    study: bool
    money: bool
    partner: bool
    family: bool
    friends: bool
    society: bool
    date: bool
    events: bool
    weather: bool
    other: bool
    sleep_hours: Optional[str] = None
    note: Optional[str] = None
    datetime: Optional[str] = None


@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/save")
async def save_entry(payload: DiaryEntry):
    logger.info(
        f'''
        Дані збережено:
        nastrii: {payload.nastrii}
        work: {payload.work}
        health: {payload.health}
        study: {payload.study}
        money: {payload.money}
        partner: {payload.partner}
        family: {payload.family}
        friends: {payload.friends}
        society: {payload.society}
        date: {payload.date}
        events: {payload.events}
        weather: {payload.weather}
        other: {payload.other}
        sleep_hours: {payload.sleep_hours}
        note: {payload.note}
        datetime: {payload.datetime}

        '''
    )
    cursor.execute(
        '''
        INSERT INTO diary (
            nastrii, work, health, study, money, partner, family, friends,
            society, date, events, weather, other, sleep_hours, note, datetime
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (
            payload.nastrii, payload.work, payload.health, payload.study,
            payload.money, payload.partner, payload.family, payload.friends,
            payload.society, payload.date, payload.events, payload.weather,
            payload.other, payload.sleep_hours, payload.note, payload.datetime
        )
    )
    conn.commit()
    return {"status": "saved"}

@app.get('/db')
async def fetch_data():
    cursor.execute('SELECT * FROM diary')
    rows = cursor.fetchall()
    data = [dict(row) for row in rows]
    return data