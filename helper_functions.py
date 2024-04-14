import numpy as np
import pandas as pd
import streamlit as st
from bokeh.models import LinearAxis, Range1d
from bokeh.plotting import figure


def help_info() -> None:
    return f'This file contains helper functions for main code of streamlit application'


@st.cache_data
def read_data(file_name: str) -> pd.DataFrame:
    return pd.read_csv(f'data/{file_name}.csv')


def save_data(data: pd.DataFrame, file_name: str) -> None:
    return data.to_csv(f'data/{file_name}.csv', index=False)


class RealSalary:

    def __init__(self, salary, inflation) -> None:
        if not isinstance(salary, np.ndarray):
            raise TypeError(f"Wrong Salary type: {type(salary)}. Only <np.ndarray> type is allowed.")
        if not isinstance(inflation, np.ndarray):
            raise TypeError(f"Wrong Inflation type: {type(inflation)}. Only <np.ndarray> type is allowed.")
        if not salary.size:
            raise Exception(f"Salary array cannot be empty.")
        if not inflation.size:
            raise Exception(f"Inflation array cannot be empty.")
        if not salary.size == inflation.size:
            raise Exception(f"Salary and Inflation array sizes must be equal.")
        self.salary = salary
        self.inflation = inflation

    def shape(self):
        return self.calc().shape

    def calc(self):
        return (self.salary[1:] / (self.inflation[:-1] / 100 + 1)).astype('int')


def plot_graph(years: np.ndarray,
               real_salary: np.ndarray,
               industry_name: str) -> None:

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"
    p = figure(
        title=f'Вид экономической деятельности: {industry_name}',
        width=1200, height=600,
        tools=TOOLS)
    p.background_fill_color = "#fafafa"

    p.scatter(years, real_salary.salary,
              legend_label='Номинальная заработная плата', color='green',
              alpha=1.0, muted_alpha=0.0)
    p.line(years, real_salary.salary,
           legend_label='Номинальная заработная плата', color='green',
           line_width=2, alpha=1.0, muted_alpha=0.0)

    p.scatter(years[1:], real_salary.calc(),
              legend_label='Реальная заработная плата', color='brown',
              alpha=1.0, muted_alpha=0.0)
    p.line(years[1:], real_salary.calc(),
           legend_label='Реальная заработная плата', color='brown',
           line_width=2, alpha=1.0, muted_alpha=0.0)

    p.yaxis.axis_label = "Заработная плата, руб."

    p.extra_y_ranges['foo'] = Range1d(2, 22)
    p.line(years, real_salary.inflation,
           legend_label='Инфляция', color='coral', line_dash='dotdash',
           line_width=2, alpha=1.0, muted_alpha=0.0, y_range_name="foo")

    ax2 = LinearAxis(y_range_name="foo", axis_label="Инфляция, %")
    ax2.axis_label_text_color = "coral"
    p.add_layout(ax2, 'right')
    p.x_range.start = 2000
    p.y_range.start = 0
    p.xaxis.axis_label = "Год"
    p.legend.location = "top_center"
    p.legend.click_policy = "mute"
    st.bokeh_chart(p, use_container_width=True)


def note() -> str:
    return (f'_*Примечание:*_\n1. Нажмите на ВЭД в легенде, чтобы скрыть линию;\n'
            f'2. Используйте панель справа для управления графиком.')


def conclusion(file_name: str) -> str:
    with open(f'conclusion/{file_name.lower()}.txt', encoding='utf8') as f:
        contents = f.read()
        return contents
