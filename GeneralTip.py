## Importing Libraries
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

## loading data
df = pd.read_csv('tips.csv')
st.set_page_config(page_title='General Graphing Dashboard - لوحة معلومات الرسوم البيانية العامة',page_icon=None,
                   layout='wide',initial_sidebar_state='auto', menu_items=None)
st.title('General Graphing Dashboard - لوحة معلومات الرسوم البيانية العامة')
st.subheader('Tips Data Set - مجموعة بيانات البقشيس')
## Sidebar
st.sidebar.header('Filters - قوائم الاختيار')
st.sidebar.write('')
figure_type = st.sidebar.selectbox('Select figure type - اختر نوع الرسم البياني',['px.scatter','px.bar','px.pie','px.donut'])
x_data = st.sidebar.selectbox('Select X axis data - اختر بيانات محور السينات',['sex','smoker','day','time','Payer Name'])
y_data = st.sidebar.selectbox('Select Y axis data - اختر بيانات محور الصادات',['total_bill','tip','size','price_per_person'])
st.sidebar.write('')
st.sidebar.markdown('Made with :heart: by: [Suhail Sallam](https://www.youtube.com/@suhailsallam)')
st.sidebar.markdown('[Suhail Sallam](https://www.youtube.com/@suhailsallam) تم انشاؤه مع  :heart: من قبل : ')

## body
# row 1
st.subheader('Numaric Values')
st.write('')

st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: rgba(28, 131, 225, 0.1);
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 5% 5% 5% 10%;
   border-radius: 5px;
   color: rgb(30, 103, 119);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: red;
}
</style>
"""
, unsafe_allow_html=True)

col_11, col_12, col_13, col_14 = st.columns(4)
col_11.metric('Sum of  Total Bills مجموع قيم الفواتير',df['total_bill'].sum().round(2))
col_12.metric('Average Total Bills معدل قيم الفواتير',df['total_bill'].mean().round(2))
col_13.metric('Minimum Total Bills قيمة أقل فاتورة',df['total_bill'].min().round(2))
col_14.metric('Maximum Total Bills قيمة أعلى فاتورة',df['total_bill'].max().round(2))
# row 2
col_21, col_22, col_23, col_24 = st.columns(4)
col_21.metric('sum of  Tips مجموع قيم البقشيش',df['tip'].sum().round(2))
col_22.metric('Average Tips معدل قيمة البقشيش',df['tip'].mean().round(2))
col_23.metric('Minimum Tip أقل قيمة بقشيش',df['tip'].min().round(2))
col_24.metric('Maximum Tip أعلى قيمة بقشيش',df['tip'].max().round(2))

#row 3

if figure_type == 'px.scatter':
    fig = px.scatter(data_frame = df,
                 x=x_data,
                 y=y_data,
                 color = x_data,
                 size = y_data,
                 facet_col = 'size',
                 facet_row = 'size')
    st.plotly_chart(fig,use_container_width=True)
elif figure_type == 'px.bar':
    fig = px.bar(data_frame = df,
                 x=x_data,
                 y=y_data,
                 color = x_data)
    st.plotly_chart(fig,use_container_width=True)
elif figure_type == 'px.pie':
    fig = px.pie(data_frame=df,
                 names=x_data,
                 values=y_data,
                 color=x_data )
    st.plotly_chart(fig,use_container_width=True)
elif figure_type == 'px.donut':
    fig = px.pie(data_frame=df,
                 names=x_data,
                 values=y_data,
                 color=x_data,
                 hole=0.4)
    st.plotly_chart(fig,use_container_width=True)
else:
    st.write('No Graph Selected')
    
