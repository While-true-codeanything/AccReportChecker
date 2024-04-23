import streamlit as st
import pandas as pd

from main import caluclate_errors


def compare_files(file1, file2):
    df = pd.read_excel(file1, header=None, skipfooter=1)
    df2 = pd.read_excel(file2, header=None, skipfooter=1)
    wrong_ids, total_difference = caluclate_errors(df, df2)
    return wrong_ids, total_difference


st.title("Обнаружение несовпадений в XLS отчетах")
st.sidebar.header("Загрузка файлов")
file1 = st.sidebar.file_uploader("Выберите первый Excel файл", type=['xls'])
file2 = st.sidebar.file_uploader("Выберите второй Excel файл", type=['xls'])

# Кнопка для запуска сравнения
if st.sidebar.button("Сравнить"):
    if file1 is not None and file2 is not None:
        wrong_ids_res, total_difference_res = compare_files(file1, file2)
        st.write(wrong_ids_res)
        st.metric(label="Общая разница без учета знака", value=total_difference_res)
    else:
        st.sidebar.warning("Пожалуйста, загрузите оба файла для сравнения.")
