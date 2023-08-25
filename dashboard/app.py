from http import HTTPStatus
import numpy as np
import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import os 
import datetime
import matplotlib.dates as mdates
url = "https://www.floatrates.com/"
usd_df = pd.read_json("https://www.floatrates.com/daily/usd.json")
euro_df = pd.read_json("https://www.floatrates.com/daily/eur.json")
uk_df = pd.read_json("https://www.floatrates.com/daily/gbp.json")
egy_df = pd.read_json("https://www.floatrates.com/daily/egp.json")

st.set_page_config(
    page_title= 'Currency rate dashboard',
    layout= 'wide'
)
st.title(":bar_chart: Currency rate / live data dashboard")
st.markdown("##")

options = st.sidebar.selectbox("Chose the Currency",('U.S Dollar','Euro','U.K Pound Sterling','Egyptian Pound'))
st.header(options)

placeholder = st.empty()

if options == 'U.S Dollar':
    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric(label="Euro €", value=round(usd_df.loc['rate']['eur'],2))
        kpi2.metric(label="Egyptian Pound E£", value=round(usd_df.loc['rate']['egp'] ,2))
        kpi3.metric(label="U.K. Pound Sterling  £", value=round(usd_df.loc['rate']['gbp'],2))


    st.markdown("""---""")
    st.subheader(" Daily Foreign Exchange Rates for" + options +" in 80 currencies ")

    st.write(st.dataframe(usd_df))
    st.markdown("""---""")
    st.subheader(" live data source ")
    st.write(" live data source (%s)" % url)
if options == 'Euro':
    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric(label="U.S Dollar $", value=round(euro_df.loc['rate']['usd'],2))
        kpi2.metric(label="Egyptian Pound E£", value=round(euro_df.loc['rate']['egp'] ,2))
        kpi3.metric(label="U.K. Pound Sterling  £", value=round(euro_df.loc['rate']['gbp'],2))
    st.markdown("""---""")
    st.subheader("Exchange Rates History Of " + options + " For 1 USD")
    df_plot = pd.read_csv("EUR_European-Euro.csv")
    df_plot["Date"] = pd.to_datetime(df_plot["Date"])

    formatter = mdates.DateFormatter("%Y")
    locator = mdates.YearLocator()
    plot_df = df_plot.filter(df_plot['Date'].dt.to_period('M').drop_duplicates().index, axis = 0)
    fig, ax = plt.subplots(figsize=(15,2))
    ax.plot(df_plot["Date"], df_plot["Close"])
    ax.set_xlabel("Years" , color = "RED")
    ax.set_ylabel("Value for 1 USD" , color = "RED")
    plt.grid()
    start, end = ax.get_xlim()
    ax.xaxis.set_major_formatter(formatter) 
    ax.xaxis.set_major_locator(locator) 
    
    st.pyplot(fig)
    st.markdown("""---""")
    st.subheader(" Daily Foreign Exchange Rates for " + options +" in 80 currencies ")
    st.write(" live data source (%s)" % url)
    st.write(st.dataframe(euro_df.head()))

if options == 'Egyptian Pound':
    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric(label="U.S Dollar $", value=round(egy_df.loc['rate']['usd'],3))
        kpi2.metric(label="Euro €", value=round(egy_df.loc['rate']['eur'],3))
        kpi3.metric(label="U.K. Pound Sterling  £", value=round(egy_df.loc['rate']['gbp'],3))

    st.markdown("""---""")
    st.subheader("Exchange Rates History Of " + options + " For 1 USD")
    df_plot = pd.read_csv("EGP_Egyptian-Pound.csv")
    df_plot["Date"] = pd.to_datetime(df_plot["Date"])
    formatter = mdates.DateFormatter("%Y")
    locator = mdates.YearLocator()
    plot_df = df_plot.filter(df_plot['Date'].dt.to_period('M').drop_duplicates().index, axis = 0)
    fig, ax = plt.subplots(figsize=(15,2))
    ax.plot(df_plot["Date"], df_plot["Close"])
    ax.set_xlabel("Years" , color = "RED")
    ax.set_ylabel("Value for 1 USD" , color = "RED")
    plt.grid()
    start, end = ax.get_xlim()
    ax.xaxis.set_major_formatter(formatter) 
    ax.xaxis.set_major_locator(locator) 
    
    st.pyplot(fig)
    st.markdown("""---""")
    st.subheader(" Daily Foreign Exchange Rates for " + options +" in 80 currencies ")
    st.write(" live data source (%s)" % url)
    st.write(st.dataframe(egy_df.head()))
 

if options == 'U.K Pound Sterling':
    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric(label="U.S Dollar $", value=round(uk_df.loc['rate']['usd'],2))
        kpi2.metric(label="Euro €", value=round(uk_df.loc['rate']['eur'],2))
        kpi3.metric(label="Egyptian Pound E£", value=round(uk_df.loc['rate']['egp'] ,2))
    st.markdown("""---""")
    st.subheader("Exchange Rates History Of " + options + " For 1 USD")
    df_plot = pd.read_csv("GBP_Pound-Sterling.csv")
    df_plot["Date"] = pd.to_datetime(df_plot["Date"])

    formatter = mdates.DateFormatter("%Y")
    locator = mdates.YearLocator()
    plot_df = df_plot.filter(df_plot['Date'].dt.to_period('M').drop_duplicates().index, axis = 0)
    fig, ax = plt.subplots(figsize=(15,2))
    ax.plot(df_plot["Date"], df_plot["Close"])
    ax.set_xlabel("Years" , color = "RED")
    ax.set_ylabel("Value for 1 USD" , color = "RED")
    plt.grid()
    start, end = ax.get_xlim()
    ax.xaxis.set_major_formatter(formatter) 
    ax.xaxis.set_major_locator(locator) 
    
    st.pyplot(fig)
    st.markdown("""---""")
    st.subheader(" Daily Foreign Exchange Rates for " + options +" in 80 currencies ")
    st.write(" live data source (%s)" % url)
    st.write(st.dataframe(egy_df.head()))
    