import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor

pipe_t20 = pickle.load(open('pipe_t20.pkl','rb'))

teams = ['Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka']

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']

st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done(works for over>5)')
with col5:
    wickets = st.number_input('Wickets out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):

    batting_team_Afghanistan = 0
    batting_team_Australia = 0
    batting_team_Bangladesh = 0
    batting_team_England = 0
    batting_team_India = 0
    batting_team_New_Zealand = 0
    batting_team_Pakistan = 0
    batting_team_South_Africa = 0
    batting_team_Sri_Lanka = 0
    batting_team_West_Indies = 0
    bowling_team_Afghanistan = 0
    bowling_team_Australia = 0
    bowling_team_Bangladesh = 0
    bowling_team_England = 0
    bowling_team_India = 0
    bowling_team_New_Zealand = 0
    bowling_team_Pakistan = 0
    bowling_team_South_Africa = 0
    bowling_team_Sri_Lanka = 0
    bowling_team_WestIndies = 0

    if batting_team == 'India':
        batting_team_India += 1
    if bowling_team == 'India':
        bowling_team_India += 1

    if batting_team == 'Australia':
        batting_team_Australia += 1
    if bowling_team == 'Australia':
        bowling_team_Australia += 1

    if batting_team == 'Bangladesh':
        batting_team_Bangladesh += 1
    if bowling_team == 'Bangladesh':
        bowling_team_Bangladesh += 1

    if batting_team == 'New Zealand':
        batting_team_New_Zealand += 1
    if bowling_team == 'New Zealand':
        bowling_team_New_Zealand += 1

    if batting_team == 'South Africa':
        batting_team_South_Africa += 1
    if bowling_team == 'South Africa':
        bowling_team_South_Africa += 1

    if batting_team == 'England':
        batting_team_England += 1
    if bowling_team == 'England':
        bowling_team_England += 1

    if batting_team == 'West Indies':
        batting_team_West_Indies += 1
    if bowling_team == 'West Indies':
        bowling_team_WestIndies += 1

    if batting_team == 'Afghanistan':
        batting_team_Afghanistan += 1
    if bowling_team == 'Afghanistan':
        bowling_team_Afghanistan += 1

    if batting_team == 'Pakistan':
        batting_team_Pakistan += 1
    if bowling_team == 'Pakistan':
        bowling_team_Pakistan += 1

    if batting_team == 'Sri Lanka':
        batting_team_Sri_Lanka += 1
    if bowling_team == 'Sri Lanka':
        bowling_team_Sri_Lanka += 1








    balls_left = 120 - (overs*6)
    wickets_left = 10 - wickets
    crr = current_score/overs


    input_df = pd.DataFrame(
        {'current_score': [current_score],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'crr': [crr],
        'last_five': [last_five],
        'batting_team_Afghanistan': [batting_team_Afghanistan],
        'batting_team_Australia': [batting_team_Australia],
        'batting_team_Bangladesh': [batting_team_Bangladesh],
        'batting_team_England': [batting_team_England],
        'batting_team_India': [batting_team_India],
        'batting_team_New_Zealand': [batting_team_New_Zealand],
        'batting_team_Pakistan': [batting_team_Pakistan],
        'batting_team_South_Africa': [batting_team_South_Africa],
        'batting_team_Sri_Lanka': [batting_team_Sri_Lanka],
        'batting_team_West_Indies': [batting_team_West_Indies],
        'bowling_team_Afghanistan': [bowling_team_Afghanistan],
        'bowling_team_Australia': [bowling_team_Australia],
        'bowling_team_Bangladesh': [bowling_team_Bangladesh],
        'bowling_team_England': [bowling_team_England],
        'bowling_team_India': [bowling_team_India],
        'bowling_team_New_Zealand': [bowling_team_New_Zealand],
        'bowling_team_Pakistan': [bowling_team_Pakistan],
        'bowling_team_South_Africa': [bowling_team_South_Africa],
        'bowling_team_Sri_Lanka': [bowling_team_Sri_Lanka],
        'bowling_team_WestIndies': [bowling_team_WestIndies]
    })


    # input_df = pd.DataFrame(
    #  {'batting_team': [batting_team], 'bowling_team': [bowling_team],'city':city, 'current_score': [current_score],'balls_left': [balls_left], 'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five]})

    if batting_team == bowling_team:
        st.header("Alert: Batting and Bowling team should not be same!!")
    else:
        if wickets_left <= 0:
            st.header("Projected Score: " + str(int(current_score))  + " --All Out...!!")
        else:
            st.table(input_df)
            result = pipe_t20.predict(input_df)
            st.header("Projected Score: " + str(int(result[0])))

    # result = pipe.predict(input_df)
    # st.header("Predicted Score - " + str(int(result[0])))



