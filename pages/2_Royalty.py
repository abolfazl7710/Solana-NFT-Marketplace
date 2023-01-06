import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="🪙 Royalty",
    layout= "wide",
    page_icon="🪙",
)
st.title("🪙 Royalty")
st.sidebar.success("🪙 Royalty")
@st.cache(ttl=600)
def get_data(query):
    if query == 'Total':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0d2f3f4c-34b3-4db0-b127-622397d0e7fc/data/latest')
    elif query == 'Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/972cbb91-7b61-4068-af93-c3ab6731945d/data/latest')
    elif query == 'Fee':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f9cec093-6c83-4bc2-b729-011ae97c0646/data/latest')
    return None
df1 = get_data('Total')
df2 = get_data('Daily')
df3 = get_data('Fee')
options = st.multiselect(
    '**Select your desired marketplace (Just one):**',
    options=df1['PLATFORM'].unique(),
    #default=df1[].unique(),
    key='PLATFORM'
)

if len(options) == 1:
 
 
 df1 = df1.query("PLATFORM == @options")
 df2 = df2.query("PLATFORM == @options")
 df3 = df3.query("PLATFORM == @options")
 st.write("""
 # Overal Nft sale activity at each royalty #

 The Daily Number of sellers , sale count metrics is a measure of how many wallets / transaction NFT selleing on Solana chain at each marketplace for each royalty.

 """
 )
 st.subheader('Total number of sale at each royalty')
 cc1, cc2= st.columns([1, 1])
 
 with cc1:
  st.caption('Total count of sale at each royalty')
  st.bar_chart(df1, x='ROYALTY', y = 'TX_COUNT', width = 400, height = 400)
 with cc2:
  fig = px.pie(df1, values='TX_COUNT', names='ROYALTY', title='Total count of sale at each royalty')
  fig.update_layout(legend_title=None, legend_y=0.5)
  fig.update_traces(textinfo='percent+label', textposition='inside')
  st.plotly_chart(fig, use_container_width=True, theme='streamlit')

 fig = px.area(df2, x='DATE', y='TX_COUNT',color='ROYALTY', title='Daily count of sale at each royalty')
 fig.update_layout(legend_title=None, legend_y=0.5)
 st.plotly_chart(fig, use_container_width=True, theme='streamlit')
 st.subheader('Total number of seller at each royalty')
 cc1, cc2= st.columns([1, 1])
 
 with cc1:
  st.caption('Total count of seller at each royalty')
  st.bar_chart(df1, x='ROYALTY', y = 'USER_COUNT', width = 400, height = 400)
 with cc2:
  fig = px.pie(df1, values='USER_COUNT', names='ROYALTY', title='Total count of seller at each royalty')
  fig.update_layout(legend_title=None, legend_y=0.5)
  fig.update_traces(textinfo='percent+label', textposition='inside')
  st.plotly_chart(fig, use_container_width=True, theme='streamlit')

 fig = px.area(df2, x='DATE', y='USER_COUNT',color='ROYALTY', title='Daily count of seller at each royalty')
 fig.update_layout(legend_title=None, legend_y=0.5)
 st.plotly_chart(fig, use_container_width=True, theme='streamlit')

 st.subheader('Daily platform fee per total transaction count')
 st.caption('Daily platform fee per total transaction count')
 st.bar_chart(df3, x='DATE', y = 'PLAT_FEE', width = 400, height = 400)
 st.write("""
 You can see my queries here:

 """)
 cc1, cc2,cc3= st.columns([1, 1,1])
 
 with cc1:
  st.info('**[Query1](https://app.flipsidecrypto.com/velocity/queries/f9cec093-6c83-4bc2-b729-011ae97c0646)**')
 with cc2:
  st.info('**[Query2](https://app.flipsidecrypto.com/velocity/queries/0d2f3f4c-34b3-4db0-b127-622397d0e7fc)**')
 with cc3:
  st.info('**[Query3](https://app.flipsidecrypto.com/velocity/queries/972cbb91-7b61-4068-af93-c3ab6731945d)**')