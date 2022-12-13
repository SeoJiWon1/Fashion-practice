import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cj.csv', encoding = 'cp949')
# 파일 저장할 때(저장할 데이터프레임 df로 지정)
# df.to_csv('파일이름',encoding='cp949')
# 파일 불러올때
# pd.read_csv('파일이름',encoding='cp949')