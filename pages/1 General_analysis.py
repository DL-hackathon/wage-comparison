from helper_functions import *
from bokeh.plotting import figure


# read the data about salary
df_salary = read_data('salary_excerpt')

# obtain period for analysis
years = df_salary.columns[1:].map(int)

# print info for the user
st.title(f'Номинальные заработные платы и Уровень инфляции в России в {years[0]}-{years[-1]} гг.')
st.header(f'1. Анализ номинальных заработных плат')
st.write(f'Для анализа выбраны следующие ВЭД: {", ".join(df_salary["ВЭД"].values)}.')
st.write('Номинальные заработные платы (в рублях) представлены в таблице 1.')
st.dataframe(df_salary.head(), hide_index=True)

# plot a graph of nominal wages
st.subheader('Динамика номинальных заработных плат')
st.write('По данным таблицы 1 построим графики изменения номинальных заработных плат')

colors = ['blue', 'orange', 'green']
TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"
p = figure(
    title=f'Номинальные заработные платы по видам экономической деятельности в России в {years[0]}-{years[-1]} гг',
    width=1000, height=500,
    tools=TOOLS)
p.background_fill_color = "#fafafa"

for i in range(df_salary.shape[0]):
    p.scatter(years, df_salary.iloc[i].values[1:],
              legend_label=df_salary.iloc[i].values[0], color=colors[i],
              alpha=0.8, muted_color=colors[i], muted_alpha=0.0)
    p.line(years, df_salary.iloc[i].values[1:],
           legend_label=df_salary.iloc[i].values[0], line_color=colors[i],
           line_width=2, alpha=1.0, muted_color=colors[i], muted_alpha=0.0)

p.x_range.start = 2000
p.y_range.start = 0
p.xaxis.axis_label = "Год"
p.yaxis.axis_label = "Заработная плата, руб."
p.legend.location = "top_left"
p.legend.click_policy="mute"
st.bokeh_chart(p, use_container_width=True)

# print note
st.write(note())
# print conclusion
st.markdown(conclusion('nominal_salary'))

# print info for the user
st.header(f'2. Уровень инфляции')
st.write('Таблица 2: Уровень инфляции по месяцам в годовом исчислении')

df_inflation = read_data('inflation_by_month')
df_inflation = df_inflation[(df_inflation['Год'] > 1999) & (df_inflation['Год'] < 2024)]
st.dataframe(df_inflation, hide_index=True)

# obtain an array with inflation values, sorted from 2000 to 2023
inflation = df_inflation['Всего'].values[::-1]
st.write('Для упрощения расчётов поместим величину годовой инфляции '
         '(таблица 2, столбец "Всего") отдельной строкой в таблицу 1.')
st.write('Таблица 3: Номинальные заработные платы (в рублях) и уровень инфляции (%)')
df_salary.loc[len(df_salary.index)] = ['Инфляция, %', *inflation]
st.dataframe(df_salary, hide_index=True)

# plot a graph og inflation
st.write('По данным таблицы 3 построим график изменения инфляции')

z = np.polyfit(years, inflation, 1)
trend_line = np.poly1d(z)

TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"
p = figure(
    title=f'Уровень инфляции в РФ в {years[0]}-{years[-1]} гг.',
    width=1000, height=500,
    tools=TOOLS)
p.background_fill_color = "#fafafa"

p.scatter(years, df_salary.iloc[3].values[1:],
          legend_label='Инфляция', color='coral',
          alpha=1.0, muted_alpha=0.0)
p.line(years, df_salary.iloc[3].values[1:],
          legend_label='Инфляция', color='coral',
          line_width=2, alpha=1.0, muted_alpha=0.0)

p.scatter(years, trend_line(years), marker='triangle_pin',
       legend_label='Линия тренда', color='palegreen',
       alpha=1.0, muted_alpha=0.0)

p.line(years, trend_line(years),
       legend_label='Линия тренда', color='palegreen',
       line_width=2, alpha=1.0, muted_alpha=0.0)

p.line(years, np.ones_like(years) * np.mean(df_salary.iloc[3].values[1:]),
          legend_label='Среднее значение', color='brown', line_dash='dotdash',
          line_width=2, alpha=1.0, muted_alpha=0.0)

p.x_range.start = 2000
p.y_range.start = 0
p.xaxis.axis_label = "Год"
p.yaxis.axis_label = "Инфляция, %"
p.legend.location = "top_right"
p.legend.click_policy="mute"
st.bokeh_chart(p, use_container_width=True)

# print note
st.write(note())

# print conclusion
st.markdown(conclusion('inflation'))

# save obtained data into csv-file
save_data(df_salary, 'table_3')