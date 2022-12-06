import streamlit as st
import pandas as pd
import numpy as np

st.title("App Football Data - By MestreAlex")

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League',['EnglandA','EnglandB','GermanyA','GermanyB','ItalyA','ItalyB','SpainA','SpainA','FranceA','FranceB','Holanda','Portugal','Turquia','Belgica','Grecia','Escocia'])

st.sidebar.header("Season")
selected_season = st.sidebar.selectbox('Season',['2022/2023','2021/2022','2020/2021','2019/2020','2018/2019','2017/2018','2016/2017','2015/2016','2014/2015','2013/2014','2012/2013','2011/2012'])

# WebScraping Football Data
def load_data(league, season):
  
  if selected_league == 'EnglandA':
    league = 'E0'
  if selected_league == 'EnglandB':
    league = 'E1'
  if selected_league == 'GermanyA':
    league = 'D1'
  if selected_league == 'GermanyB':
    league = 'D1'
  if selected_league == 'ItalyA':
    league = 'I1'
  if selected_league == 'ItalyB':
    league = 'I2'
  if selected_league == 'SpainA':
    league = 'SP1'
  if selected_league == 'SpainB':
    league = 'SP2'
  if selected_league == 'FranceA':
    league = 'F1'
  if selected_league == 'FranceB':
    league = 'F2'
  if selected_league == 'Holanda':
    league = 'N1'
  if selected_league == 'Portugal':
   league = 'P1'
  if selected_league == 'Turquia':
   league = 'T1'
  if selected_league == 'Belgica':
   league = 'B1'
  if selected_league == 'Grecia':
   league = 'G1'    
  if selected_league == 'Escocia':
   league = 'SC0'    
    
    
    
  if selected_season == '2022/2023':
    season = '2223'    
  if selected_season == '2021/2022':
    season = '2122'
  if selected_season == '2020/2021':
    season = '2021'
  if selected_season == '2019/2020':
    season = '1920'
  if selected_season == '2018/2019':
    season = '1819'
  if selected_season == '2017/2018':
    season = '1718' 
  if selected_season == '2016/2017':
    season = '1617'
  if selected_season == '2015/2016':
    season = '1516'
  if selected_season == '2014/2015':
    season = '1415'
  if selected_season == '2013/2014':
    season = '1314'
  if selected_season == '2012/2013':
    season = '1213'
  if selected_season == '2011/2012':
    season = '1112'    
    
  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  return data

df = load_data(selected_league, selected_season)

st.subheader("Dataframe: "+selected_league)
st.dataframe(df)

 

