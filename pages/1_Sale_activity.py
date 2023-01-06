import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="📊 Overview (💸 Sale activity)",
    layout= "wide",
    page_icon="📊",
)
st.title("📊 Overview (💸 Sale activity)")
st.sidebar.success("📊 Overview (💸 Sale activity)")
@st.cache(ttl=600)
def get_data(query):
    if query == 'Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4eb048ce-58e3-4519-a347-02ad3b93e4ed/data/latest')
    elif query == 'Total':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a637cadf-ab8c-4e83-9f6a-92f997d65a1e/data/latest')
    elif query == 'Catc':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/93f7c5e4-a3c6-4ffb-b16f-333af34eb9ba/data/latest')
    elif query == 'Catv':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e50994b0-7079-44fd-9b47-8c0fd4617418/data/latest')
    elif query == 'Topcc':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c83bb9f6-e64d-413d-9e00-c5e259f95f15/data/latest')
    elif query == 'Topcv':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4d8aa8c1-5c11-4589-b557-2a162ec342b0/data/latest')
    elif query == 'Topuc':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/42dbbbdf-c32f-41a6-a616-5ac35bd22d77/data/latest')
    elif query == 'Topuv':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ac5c94b0-2f1d-476e-af45-8eeaabd6570f/data/latest')
    return None
df1 = get_data('Daily')
df2 = get_data('Total')
df3 = get_data('Catc')
df4 = get_data('Catv')
df5 = get_data('Topcc')
df6 = get_data('Topcv')
df7 = get_data('Topuc')
df8 = get_data('Topuv')

options = st.multiselect(
    '**Select your desired marketplace:**',
    options=df1['MARKETPLACE'].unique(),
    default=df1['MARKETPLACE'].unique(),
    key='Marketplace'
)

if len(options) > 0:
 
 
 df1 = df1.query("MARKETPLACE == @options")
 df2 = df2.query("MARKETPLACE == @options")
 df3 = df3.query("MARKETPLACE == @options")
 df4 = df4.query("MARKETPLACE == @options")
 df5 = df5.query("MARKETPLACE == @options")
 df6 = df6.query("MARKETPLACE == @options")
 df7 = df7.query("MARKETPLACE == @options")
 df8 = df8.query("MARKETPLACE == @options")
 
 st.write("""
 # Overal Nft sale activity #

 The Daily Number of sellers , sale count and sale volume (USD) metrics is a measure of how many wallets / transaction with how much volume (USD) NFT selleing on Solana chain at each marketplace.

 """
 )
 st.subheader('Total number of sale at each marketplace')
 cc1, cc2= st.columns([1, 1])
 
 with cc1:
  st.caption('Total count of sale at each marketplace')
  st.bar_chart(df2, x='MARKETPLACE', y = 'SALES_COUNT', width = 400, height = 400)
 with cc2:
  fig = px.pie(df2, values='SALES_COUNT', names='MARKETPLACE', title='Total count of sale at each marketplace')
  fig.update_layout(legend_title=None, legend_y=0.5)
  fig.update_traces(textinfo='percent+label', textposition='inside')
  st.plotly_chart(fig, use_container_width=True, theme='streamlit')

 fig = px.bar(df1, x='DATE', y='SALES_COUNT',color='MARKETPLACE', title='Daily count of sale at each marketplace')
 fig.update_layout(legend_title=None, legend_y=0.5)
 st.plotly_chart(fig, use_container_width=True, theme='streamlit')
 st.subheader('Total number of seller at each marketplace')
 cc1, cc2= st.columns([1, 1])
 
 with cc1:
  st.caption('Total count of seller at each marketplace')
  st.bar_chart(df2, x='MARKETPLACE', y = 'BUYER_COUNT', width = 400, height = 400)
 with cc2:
  fig = px.pie(df2, values='BUYER_COUNT', names='MARKETPLACE', title='Total count of seller at each marketplace')
  fig.update_layout(legend_title=None, legend_y=0.5)
  fig.update_traces(textinfo='percent+label', textposition='inside')
  st.plotly_chart(fig, use_container_width=True, theme='streamlit')

 fig = px.bar(df1, x='DATE', y='BUYER_COUNT',color='MARKETPLACE', title='Daily count of seller at each marketplace')
 fig.update_layout(legend_title=None, legend_y=0.5)
 st.plotly_chart(fig, use_container_width=True, theme='streamlit')

 st.subheader('Total volume of sale at each marketplace')
 cc1, cc2= st.columns([1, 1])
 
 with cc1:
  st.caption('Total count of seller at each marketplace')
  st.bar_chart(df2, x='MARKETPLACE', y = 'VOLUME', width = 400, height = 400)
 with cc2:
  fig = px.pie(df2, values='VOLUME', names='MARKETPLACE', title='Total volume of sale at each marketplace')
  fig.update_layout(legend_title=None, legend_y=0.5)
  fig.update_traces(textinfo='percent+label', textposition='inside')
  st.plotly_chart(fig, use_container_width=True, theme='streamlit')
  
 fig = px.bar(df1, x='DATE', y='VOLUME',color='MARKETPLACE', title='Daily volume of sale at each marketplace')
 fig.update_layout(legend_title=None, legend_y=0.5)
 st.plotly_chart(fig, use_container_width=True, theme='streamlit')

 st.write("""
 # User categorize by count and volume (USD) of NFT sale #

 Here the swappers are categorized based on the number and volume (USD) of the NFT sale at each marketplace.

 """
 )
 cc1, cc2 = st.columns([1, 1])

 with cc1:
  fig = px.bar(df3, x='TIER', y='COUNT_USER',color='MARKETPLACE', title='User categorize by rate of sale count at each marketplace')
  fig.update_layout(legend_title=None, legend_y=0.5)
  st.plotly_chart(fig, use_container_width=True, theme='streamlit')
 with cc2:
  fig = px.pie(df3, values='COUNT_USER', names='TIER', title='User categorize by rate of sale count at each marketplace')
  fig.update_layout(legend_title=None, legend_y=0.5)
  fig.update_traces(textinfo='percent+label', textposition='inside')
  st.plotly_chart(fig, use_container_width=True, theme=None)

 cc1, cc2 = st.columns([1, 1])

 with cc1:
  fig = px.bar(df4, x='TIER', y='COUNT_USER',color='MARKETPLACE', title='User categorize by rate of sale volume (USD) at each marketplace')
  fig.update_layout(legend_title=None, legend_y=0.5)
  st.plotly_chart(fig, use_container_width=True, theme='streamlit')
 with cc2:
  fig = px.pie(df4, values='COUNT_USER', names='TIER', title='User categorize by rate of sale volume (USD) at each marketplace')
  fig.update_layout(legend_title=None, legend_y=0.5)
  fig.update_traces(textinfo='percent+label', textposition='inside')
  st.plotly_chart(fig, use_container_width=True, theme=None)

 st.write("""
 # Top 10 collection #

 Top collection are based on the number and volume (USD) of the sale are:

 """
 )
 cc1, cc2 = st.columns([1,1])

 with cc1:
  fig = px.bar(df5, x='COLLECTION', y='SALES_COUNT',color='MARKETPLACE', title='Top 10 collection by count of sale')
  fig.update_layout(legend_title=None, legend_y=0.5)
  st.plotly_chart(fig, use_container_width=True, theme='streamlit')
 with cc2:
  fig = px.bar(df6, x='COLLECTION', y='VOLUME',color='MARKETPLACE', title='Top 10 collection by volume (USD) of sale')
  fig.update_layout(legend_title=None, legend_y=0.5)
  st.plotly_chart(fig, use_container_width=True, theme='streamlit')

 st.write("""
 # Top 10 User #

 Top users are based on the number and volume (USD) of the swap are:

 """
 )

 cc1, cc2 = st.columns([1, 1])

 with cc1:

  st.subheader('Top 10 seller by count of swap')
  st.caption('Top 10 seller by count of swap')
  st.bar_chart(df7, x='USER', y = 'SALES_COUNT', width = 400, height = 400)
 with cc2:
  st.subheader('Top 10 seller by volume (USD) of sale')
  st.caption('Top 10 seller by volume (USD) of sale')
  st.bar_chart(df8, x='USER', y = 'VOLUME', width = 400, height = 400)

 st.write("""
 You can see my queries here:

 """)
 
 cc1, cc2,cc3,cc4= st.columns([1, 1,1,1])
 
 with cc1:
  st.info('**[Query1](https://app.flipsidecrypto.com/velocity/queries/4eb048ce-58e3-4519-a347-02ad3b93e4ed)**')
 with cc2:
  st.info('**[Query2](https://app.flipsidecrypto.com/velocity/queries/a637cadf-ab8c-4e83-9f6a-92f997d65a1e)**')
 with cc3:
  st.info('**[Query3](https://app.flipsidecrypto.com/velocity/queries/93f7c5e4-a3c6-4ffb-b16f-333af34eb9ba)**')
 with cc4:
  st.info('**[Query4](https://app.flipsidecrypto.com/velocity/queries/e50994b0-7079-44fd-9b47-8c0fd4617418)**')

 cc1, cc2,cc3,cc4= st.columns([1, 1,1,1])
 
 with cc1:
  st.info('**[Query5](https://app.flipsidecrypto.com/velocity/queries/c83bb9f6-e64d-413d-9e00-c5e259f95f15)**')
 with cc2:
  st.info('**[Query6](https://app.flipsidecrypto.com/velocity/queries/4d8aa8c1-5c11-4589-b557-2a162ec342b0)**')
 with cc3:
  st.info('**[Query7](https://app.flipsidecrypto.com/velocity/queries/42dbbbdf-c32f-41a6-a616-5ac35bd22d77)**')
 with cc4:
  st.info('**[Query8](https://app.flipsidecrypto.com/velocity/queries/ac5c94b0-2f1d-476e-af45-8eeaabd6570f)**')