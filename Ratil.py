import random
import requests
import streamlit as st
##############################################################################################################
def get_random_verse(num=1):
    result = [{} for _ in range(num)]
    verse = random.randint(1, 6237)
    url = []
    json_data = []
    for i in range(num):
        url.append('http://api.alquran.cloud/ayah/'+str(verse+i)+'/editions/quran-uthmani,en.pickthall')
        json_data.append(requests.get(url[i]).json())
    i = 0
    for json_data in json_data:
        result[i]["verse_a"] = json_data['data'][0]['text']
        result[i]["verse_en"] = json_data['data'][1]['text']
        result[i]["sura"] = json_data['data'][0]['surah']['englishName'] + \
               '(' + str(json_data['data'][0]['surah']['number']) + '):' + \
               str(json_data['data'][0]['numberInSurah'])
        i+=1
    return result
##############################################################################################################
st.set_page_config(page_title="Ratil", page_icon="🕋", layout="centered", initial_sidebar_state="collapsed")
st.set_option('deprecation.showPyplotGlobalUse', False)
##############################################################################################################
##add png image as markdown
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("assets/Ratil.png", use_column_width=True)
st.markdown('---')
##############################################################################################################
left_col,right_col = st.columns(2)
with left_col:
    verses_num = st.number_input("Number of Verses", min_value=1, max_value=10, value=1)
with right_col:
    generate = st.button("Generate Random Verse")
if generate:
    verse = get_random_verse(verses_num)
    for i in range(verses_num):
        st.write(verse[i-1]['verse_a'])
        st.write(verse[i-1]['verse_en'])
        st.write(verse[i-1]['sura'])