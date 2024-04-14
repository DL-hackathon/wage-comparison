from helper_functions import *

# to start streamlit app use the command in terminal: streamlit run .\Main_page.py

# declare streamlit template
st.set_page_config(
    page_title="DL_Final_project",
    page_icon="\U0001F609",
)

st.header('Анализ зарплат в России')
st.markdown(
    '''
### В проекте использованы открытые данные из официальных источников:
#### - [_Среднемесячная номинальная начисленная заработная плата за 2000-2023 гг;_]\
(https://rosstat.gov.ru/labor_market_employment_salaries)

#### - [_Уровень инфляции._]\
(https://уровень-инфляции.рф/%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D1%8B-%D0%B8%D0%BD%D1%84%D0%BB%D1%8F%D1%86%D0%B8%D0%B8)

### Методика расчёта реальной заработной платы:
#### - [_Официальный источник "ЕМИСС государственная статистика"_]\
(https://fedstat.ru/indicator/43245#)
#### - [_Реальная и номинальная заработная плата: отличия, формула расчета_]\
(https://1c-wiseadvice.ru/company/blog/realnaya-i-nominalnaya-zarabotnaya-plata-otlichiya-formula-rascheta/)
    ''')

st.markdown(
    '''
    ### _Задание_: проанализировать динамику уровня средних зарплат в разрезе по  \
     видам экономической деятельности (ВЭД) в России.   
    '''
)