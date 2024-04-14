from helper_functions import *

st.title('Корреляция между реальной заработной платой в Образовании и индексом счастья')
st.markdown("#### [Индекс счастья планеты]('https://happyplanetindex.org/countries/')")

r_s_edu = [6296, 8053, 10116, 11735, 12936, 14533, 17902, 22009, 24294, 24181, 24876, 28713, 33516, 35553, 38392]
df_hpi = read_data('hpi')

st.write("Индекс счастья (Happy Planet Index) - показатель, зависящий от ожидаемой продолжительности жизни, "
         "уровня жизни и экологического состояния страны. Диапазон от 0 до 100. "
         f"Данные доступны за период {df_hpi.columns[1]}-{df_hpi.columns[-1]} гг.")

st.dataframe(df_hpi, hide_index=True)
hpi = df_hpi.iloc[0].values[1:].astype('float')

# plot a graph
years = [*range(2006, 2021)]
TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"
p = figure(
    title=f'Вид экономической деятельности: Образование',
    width=1200, height=600,
    tools=TOOLS)
p.background_fill_color = "#fafafa"

p.scatter(years, r_s_edu,
          legend_label='Реальная заработная плата', color='brown',
          alpha=1.0, muted_alpha=0.0)
p.line(years, r_s_edu,
       legend_label='Реальная заработная плата', color='brown',
       line_width=2, alpha=1.0, muted_alpha=0.0)

p.yaxis.axis_label = "Заработная плата, руб."

p.extra_y_ranges['foo'] = Range1d(30, 40)
p.line(years, hpi,
       legend_label='Индекс счастья', color='green', line_dash='dotted',
       line_width=2, alpha=1.0, muted_alpha=0.0, y_range_name="foo")

ax2 = LinearAxis(y_range_name="foo", axis_label="Индекс счастья")
ax2.axis_label_text_color = "green"
p.add_layout(ax2, 'right')
p.y_range.start = 0
p.xaxis.axis_label = "Год"
p.legend.location = "top_center"
p.legend.click_policy = "mute"
st.bokeh_chart(p, use_container_width=True)

# print conclusion
st.write(f'Коэффициент корреляции между реальной '
         f'заработной платой в Образовании и индексом счастья для России равен '
         f"`{np.corrcoef(r_s_edu, hpi)[1][0].round(2)}`.")
st.write(conclusion('hpi'))