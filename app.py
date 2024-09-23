import streamlit as st
import pandas as pd
import plotly.express as px
data=pd.read_csv('/workspaces/Super_sale/mentornow/superSales.csv')

st.write(data)
st.header('Super Store DATA')
a=data['Product_line'].unique()
s= st.sidebar.selectbox("Product Name",(a))
st.write('Top Stats')    

#c=st.container(border=True)

c1,c2,c3=st.columns(3)

b=data[data['Product_line']==s]
c1.metric(label='Total Invoice', value=b['Invoice_ID'].size)

c2.metric(label='Average Rating', value=round(b['Rating'].mean(), 2))

c3.metric(label='Total Price', value=round(b['Total_price'].sum(),2))

cl1,cl2,cl3=st.columns(3)
inc=round(b['Total_price'].sum(),2)

cl1.metric(label='Total Price', value=inc)

cost=round(b['costs'].sum(),2)
cl2.metric(label='Total Cost', value=cost)

d=(inc-cost)
cl3.metric(label='Profit',value=d)

b['Order_date']=pd.to_datetime(b['Order_date'])
st.write(b)
df1=b[b['Order_date'].dt.month==3]
st.write(df1)

df1['date']=df1['Order_date'].dt.day
st.write(df1)

result=df1.groupby('date')['Quantity'].sum().reset_index()

st.write(result)

fig=px.line(result, y='Quantity', x='date')
st.write(fig)