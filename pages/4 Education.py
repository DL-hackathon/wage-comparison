from helper_functions import *

df_sal_inf = read_data('table_3')
idx = 2 # choose an industry for analysis
st.title(f'Реальные заработные платы: {df_sal_inf["ВЭД"].values[idx]}')

method = '''
### [Методика расчета](https://fedstat.ru/indicator/43245#)

Реальная начисленная заработная плата характеризует покупательную способность
заработной платы в отчетном периоде в связи с изменением цен на потребительские
товары и услуги по сравнению с базисным периодом. Для этого рассчитывается индекс
реальной начисленной заработной платы путем деления индекса номинальной начисленной
заработной платы на индекс потребительских цен за один и тот же временной период.
'''
st.markdown(method)

st.subheader('Cредние зарплаты с учетом уровня инфляции по сравнению с предыдущим годом')
st.write('Для расчёта воспользуемся данными о номинальной заработной плате и',
         'инфляции из таблицы 3, полученной в разделе "General analysis".')
st.dataframe(df_sal_inf[(df_sal_inf["ВЭД"] == df_sal_inf["ВЭД"].values[idx]) |
                        (df_sal_inf["ВЭД"] == "Инфляция, %")], hide_index=True)

st.write('Пример пересчёта номинальной заработной платы в 2001 с учётом инфляции в 2000 г.',
         'Зпл_реал_2001 = Зпл_ном_2001 / (1 + Инфл_2000) =',
         f'{df_sal_inf.iloc[idx]["2001"]} / (1 + {(df_sal_inf.iloc[-1]["2000"] / 100).round(3)}) =',
         f'{int(df_sal_inf.iloc[idx]["2001"] / (1 + (df_sal_inf.iloc[-1]["2000"] / 100).round(3)))} руб.')

st.write('После пересчёта номинальных заработных плат с учётом инфляции',
         'построим графики изменения номинальной и реальной заработной платы.')

years = df_sal_inf.columns[1:].map(int)
inflation = df_sal_inf[df_sal_inf['ВЭД'] == 'Инфляция, %'].squeeze().values[1:]
industry, salary = df_sal_inf.iloc[idx].values[0], df_sal_inf.iloc[idx].values[1:]
real_salary = RealSalary(salary, inflation)
#plot a graph
plot_graph(years, real_salary, industry)
# print note
st.write(note())

# print conclusion
st.write(conclusion(industry))

print(real_salary.calc()[5:20])