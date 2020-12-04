import os
from app.stat.stat_models import wbank
import pandas as pd
import altair as alt
import seaborn as sns


location = ["GBR","EUU","USA","CHN"]

def inflat_db():
    source = wbank(location)
    indicator = {"FP.CPI.TOTL.ZG":"InflationConsumerPrices"}
    db = source.API_to_db(indicator)
    db.fillna(0, inplace=True)
    return db

def gdp_db():
    source = wbank(location)
    indicator = {"NY.GDP.MKTP.KD.ZG":"GDP per capita growth (annual %)"}
    db = source.API_to_db(indicator)
    return db

def latest_date():
    source = wbank(location)
    db = inflat_db()
    date = source.latest(db)
    return date

def inflat_date():
    source = wbank(location)
    db = inflat_db()
    date = source.latest(db)
    latest_uk = round(db.loc[(db["country"] == "United Kingdom") & (db["date"] == date)])
    latest_uk_x= latest_uk.iloc[0]["InflationConsumerPrices"]  
    return latest_uk_x    

def gdp_date():
    source = wbank(location)
    db = gdp_db()
    db.dropna(inplace=True)
    # print(db)
    date = source.latest(db)
    # print(date)
    latest_uk = round(db.loc[(db["country"] == "United Kingdom") & (db["date"] == date)])
    # print(latest_uk)
    latest_uk_x= latest_uk.iloc[0]["GDP per capita growth (annual %)"]
    # print(type(latest_uk_x))
    # print(latest_uk_x)
    return latest_uk_x    

def chart(df,y_axis):
    # chart = sns.lineplot(x="date", y=y_axis, hue="country", data=df)
    # return chart
    chart =  alt.Chart(df,
    width=500,
    height=400    
    ).mark_line().encode(
        x="date",
        y=y_axis,
        color=alt.Color('country', scale=alt.Scale(scheme='dark2'))
        ).properties(
        title='GDP'
        ).configure_axis(
        labelFontSize=15,
        titleFontSize=15
        ).configure_legend( 
        gradientLength=600, 
        gradientThickness=60
        )
    return chart