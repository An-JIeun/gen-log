import streamlit as st
import requests
import json

from dotenv import load_dotenv
import os
import datetime

import pandas as pd
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
import os
import gspread
load_dotenv()



api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
json_file_path = "dulcet-clock-286410-6def8608745b.json"
gc = gspread.service_account(json_file_path)
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1-sI_bCsNsW-cO7jRjMml02Mj_lETQ7-QZa67Q1R5DjM/edit?gid=0#gid=0"
doc = gc.open_by_url(spreadsheet_url)
df = pd.DataFrame(doc.sheet1.get_all_records())

rep = None
rep2 = None
text = ""
for i in range(len(df)):
    text += df['건의사항'][i]
    text += "\n"


st.title("도서관 피드백 모니터 🖥️")
st.write("오늘의 건의사항 개수 : ", len(df))
st.subheader("피드백 업데이트",divider="green")

refreash = st.button("건의사항 요약 업데이트")
if refreash:
    doc = gc.open_by_url(spreadsheet_url)
    df = pd.DataFrame(doc.sheet1.get_all_records())
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "당신은 도서관 서비스를 분석하는 AI 이고, 가장 시급하고 특이한 개선사항을 순서대로 개조식으로 10개 내외로 나열해야해"},
        {"role": "user", "content": text},
        ]
    )
    completion2 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "개선사항을 공간별로 정리하고 간단하게 설명하고 중요한 부분은 볼드처리하고 실현 가능한 수준만 작성해"},
        {"role": "user", "content": text},
    ]
    )
    rep2 = completion2.choices[0].message.content   
    rep = completion.choices[0].message.content
 
if (rep2 != None and rep != None):
    st.write("다음은 시설별 개선사항입니다.")
    st.markdown(rep2)

    st.write("다음은 접수된 건의사항의 요약입니다.")
    st.markdown(rep)

    st.write("마지막 업데이트: ", datetime.datetime.now())

st.subheader("건의사항 상세 보기", divider="green")
st.dataframe(df)
