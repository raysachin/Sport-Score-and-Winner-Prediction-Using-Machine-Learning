# streamlit is a library by which we can easily make web application
import streamlit
import streamlit as st
import pickle
import pandas as pd
from PIL import Image

teams = ['Select','Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals',
 'Gujarat Titans',
 'Lucknow Super Giants']

cities = ['Hyderabad', 'Rajkot', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata',
       'Delhi', 'Chandigarh', 'Kanpur', 'Jaipur', 'Chennai', 'Cape Town',
       'Port Elizabeth', 'Durban', 'Centurion', 'East London',
       'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad',
       'Dharamsala', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah',
       'Cuttack', 'Visakhapatnam', 'Mohali', 'Bengaluru']

# import the model
pipe_ipl = pickle.load(open('pipe_ipl.pkl', 'rb'))

st.title('IPL WIN PREDICTION')

# take input from users as batting and bowling team

col1, col2 = st.columns(2)    # here we take two column

with col1:
    batting_team = st.selectbox('Select the batting team', teams)    # here we give a dropdown

with col2:
    bowling_team = st.selectbox('Select the bowling team', teams)

# Image set
if batting_team == 'Select':
    batting_team_img = Image.open('BLANK.jpg')
if bowling_team == 'Select':
    bowling_team_img = Image.open('BLANK.jpg')

if batting_team == 'Chennai Super Kings':
    batting_team_img = Image.open('CSK.jpg')
if bowling_team == 'Chennai Super Kings':
    bowling_team_img =  Image.open('CSK.jpg')

if batting_team == 'Sunrisers Hyderabad':
    batting_team_img = Image.open('SRH.jpg')
if bowling_team == 'Sunrisers Hyderabad':
    bowling_team_img = Image.open('SRH.jpg')

if batting_team == 'Mumbai Indians':
    batting_team_img = Image.open('MI.jpg')
if bowling_team == 'Mumbai Indians':
    bowling_team_img = Image.open('MI.jpg')

if batting_team == 'Royal Challengers Bangalore':
    batting_team_img = Image.open('RCB.jpg')
if bowling_team == 'Royal Challengers Bangalore':
    bowling_team_img = Image.open('RCB.jpg')

if batting_team == 'Kolkata Knight Riders':
    batting_team_img = Image.open('KKR.jpg')
if bowling_team == 'Kolkata Knight Riders':
    bowling_team_img = Image.open('KKR.jpg')

if batting_team == 'Kings XI Punjab':
    batting_team_img = Image.open('PK.jpg')
if bowling_team == 'Kings XI Punjab':
    bowling_team_img = Image.open('PB.jpg')

if batting_team == 'Rajasthan Royals':
    batting_team_img = Image.open('RR.jpg')
if bowling_team == 'Rajasthan Royals':
    bowling_team_img = Image.open('RR.jpg')

if batting_team == 'Delhi Capitals':
    batting_team_img = Image.open('DC.jpg')
if bowling_team == 'Delhi Capitals':
    bowling_team_img = Image.open('DC.jpg')

if batting_team == 'Gujarat Titans':
    batting_team_img = Image.open('GT.jpg')
if bowling_team == 'Gujarat Titans':
    bowling_team_img = Image.open('GT.jpg')

if batting_team == 'Lucknow Super Giants':
    batting_team_img = Image.open('LSG.jpg')
if bowling_team == 'Lucknow Super Giants':
    bowling_team_img = Image.open('LSG.jpg')
col8, col9 = st.columns(2)

with col8:
    st.image(batting_team_img)

with col9:
    st.image(bowling_team_img)

select_city = st.selectbox('select host city', sorted(cities))

# for target
target = st.number_input('Target')

# for situation of match we will ask three things
# runs scored till now, over played, number of out

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score')

with col4:
    overs = st.number_input('Overs completed')

with col5:
    wickets = streamlit.number_input('Wickets Out')

# for buttons
if st.button('predict probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wicket_left = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    # give all things a dorm of data frame
    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [select_city],
                             'runs_left': [runs_left], 'balls_left': [balls_left], 'wicket_left': [wicket_left],
                             'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]})

    if batting_team == bowling_team:
        st.header("Alert: Batting and Bowling team should not be same!!")
    else:
        if wicket_left <= 0:
            st.header(" --All Out...!!")
        else:
            st.table(input_df)
            result = pipe_ipl.predict_proba(input_df)
            loss = result[0][0]
            win = result[0][1]
            st.header(batting_team + "- " + str(round(win * 100)) + "%")
            st.header(bowling_team + "- " + str(round(loss * 100)) + "%")


    # st.table(input_df)
    # result = pipe.predict_proba(input_df)
    # loss = result[0][0]
    # win = result[0][1]
    # st.header(batting_team + "- " + str(round(win*100)) + "%")
    # st.header(bowling_team + "- " + str(round(loss*100)) + "%")





