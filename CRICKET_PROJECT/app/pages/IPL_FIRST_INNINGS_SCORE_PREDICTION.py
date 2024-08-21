import streamlit as st
import pickle
import pandas as pd
from PIL import Image
import os

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

# img_batting_team = Image.open('../assets/IPL.jpg')
# rcb_img = Image.open('../assets/RCB.jpg')
# csk_img = Image.open('../assets/CSK.jpg')
# mi_img = Image.open('../assets/MI.jpg')
# lsg_img = Image.open('../assets/LSG.jpg')
# gt_img = Image.open('../assets/GT.jpg')
# srh_img = Image.open('../assets/SRH.jpg')
# kkr_img = Image.open('../assets/KKR.jpg')
# rr_img = Image.open('../assets/RR.jpg')
# pk_img = Image.open('../assets/PK.jpg')
# dc_img = Image.open('../assets/DC.jpg')



# import the model
#Get the absolute path based on the current file's location
file_path = os.path.join(os.path.dirname(__file__), '../savedModel/ipl-first-innings-score-prediction-model.pkl')

regressor = pickle.load(open(file_path, 'rb'))

st.title('IPL FIRST INNINGS SCORE PREDICTION')

# take input from users as batting and bowling team

col1, col2 = st.columns(2)    # here we take two column

with col1:
    batting_team = st.selectbox('Select the batting team', teams)    # here we give a dropdown

with col2:
    bowling_team = st.selectbox('Select the bowling team', teams)

# st.image([rcb_img, img_batting_team])

# Define the base directory relative to the current file's location
base_dir = os.path.join(os.path.dirname(__file__), '../assets')

# Function to get the correct image path
def get_image_path(filename):
    return os.path.join(base_dir, filename)

# Image set
if batting_team == 'Select':
    batting_team_img = Image.open(get_image_path('BLANK.jpg'))
if bowling_team == 'Select':
    bowling_team_img = Image.open(get_image_path('BLANK.jpg'))

if batting_team == 'Chennai Super Kings':
    batting_team_img = Image.open(get_image_path('CSK.jpg'))
if bowling_team == 'Chennai Super Kings':
    bowling_team_img = Image.open(get_image_path('CSK.jpg'))

if batting_team == 'Sunrisers Hyderabad':
    batting_team_img = Image.open(get_image_path('SRH.jpg'))
if bowling_team == 'Sunrisers Hyderabad':
    bowling_team_img = Image.open(get_image_path('SRH.jpg'))

if batting_team == 'Mumbai Indians':
    batting_team_img = Image.open(get_image_path('MI.jpg'))
if bowling_team == 'Mumbai Indians':
    bowling_team_img = Image.open(get_image_path('MI.jpg'))

if batting_team == 'Royal Challengers Bangalore':
    batting_team_img = Image.open(get_image_path('RCB.jpg'))
if bowling_team == 'Royal Challengers Bangalore':
    bowling_team_img = Image.open(get_image_path('RCB.jpg'))

if batting_team == 'Kolkata Knight Riders':
    batting_team_img = Image.open(get_image_path('KKR.jpg'))
if bowling_team == 'Kolkata Knight Riders':
    bowling_team_img = Image.open(get_image_path('KKR.jpg'))

if batting_team == 'Kings XI Punjab':
    batting_team_img = Image.open(get_image_path('PK.jpg'))
if bowling_team == 'Kings XI Punjab':
    bowling_team_img = Image.open(get_image_path('PK.jpg'))

if batting_team == 'Rajasthan Royals':
    batting_team_img = Image.open(get_image_path('RR.jpg'))
if bowling_team == 'Rajasthan Royals':
    bowling_team_img = Image.open(get_image_path('RR.jpg'))

if batting_team == 'Delhi Capitals':
    batting_team_img = Image.open(get_image_path('DC.jpg'))
if bowling_team == 'Delhi Capitals':
    bowling_team_img = Image.open(get_image_path('DC.jpg'))

if batting_team == 'Gujarat Titans':
    batting_team_img = Image.open(get_image_path('GT.jpg'))
if bowling_team == 'Gujarat Titans':
    bowling_team_img = Image.open(get_image_path('GT.jpg'))

if batting_team == 'Lucknow Super Giants':
    batting_team_img = Image.open(get_image_path('LSG.jpg'))
if bowling_team == 'Lucknow Super Giants':
    bowling_team_img = Image.open(get_image_path('LSG.jpg'))


col8, col9 = st.columns(2)

with col8:
    st.image(batting_team_img)

with col9:
    st.image(bowling_team_img)
    # st.image(csk_img, width=350)


# for situation of match we will ask three things
# runs scored till now, over played, number of wicket

col3, col4, col5 = st.columns(3)

with col3:
    overs = st.number_input('Overs Completed')

with col4:
    runs = st.number_input('Runs')

with col5:
    wickets = streamlit.number_input('Wickets Out')

col6, col7 = st.columns(2)

with col6:
    run_last_5 = st.number_input('Run Scored in prv. 5 overs')

with col7:
    wicket_last_5 = st.number_input('Wicket Taken in prv. 5 overs')

list = ['bat_team_Chennai_Super_Kings', 'bat_team_Delhi_Capitals', 'bat_team_Gujarat_Titans',
       'bat_team_Kings_XI_Punjab', 'bat_team_Kolkata_Knight_Riders', 'bat_team_Lucknow_Super_Giants',
       'bat_team_Mumbai_Indians', 'bat_team_Rajasthan_Royals',
       'bat_team_Royal_Challengers_Bangalore', 'bat_team_Sunrisers_Hyderabad',
       'bowl_team_Chennai_Super_Kings', 'bowl_team_Delhi_Capitals', 'bowl_team_Gujarat_Titans',
       'bowl_team_Kings_XI_Punjab', 'bowl_team_Kolkata_Knight_Riders', 'bowl_team_Lucknow_Super_Giants',
       'bowl_team_Mumbai_Indians', 'bowl_team_Rajasthan_Royals',
       'bowl_team_Royal_Challengers_Bangalore',
       'bowl_team_Sunrisers_Hyderabad', 'overs', 'runs', 'wickets',
       'runs_last_5', 'wickets_last_5']

# for buttons
if st.button('predict probability'):
    # if batting_team == 'Chennai Super Kings' or bowling_team == 'Chennai Super Kings':
    #     bat_team_Chennai_Super_Kings = 1
    #     if bowling_team == 'Delhi Capitals':
    #         bowl_team_Delhi_Capitals = 1
    #     else:
    #         bowl_team_Delhi_Capitals = 0
    #
    #     if bowling_team == 'Kings_XI_Punjab':
    #         bowl_team_Kings_XI_Punjab= 1
    #     else:
    #         bowl_team_Kings_XI_Punjab = 0

    bat_team_Chennai_Super_Kings = 0
    bat_team_Delhi_Capitals = 0
    bat_team_Gujarat_Titans = 0
    bat_team_Kings_XI_Punjab = 0
    bat_team_Kolkata_Knight_Riders = 0
    bat_team_Lucknow_Super_Giants = 0
    bat_team_Mumbai_Indians = 0
    bat_team_Rajasthan_Royals = 0
    bat_team_Royal_Challengers_Bangalore = 0
    bat_team_Sunrisers_Hyderabad = 0
    bowl_team_Chennai_Super_Kings = 0
    bowl_team_Delhi_Capitals = 0
    bowl_team_Gujarat_Titans = 0
    bowl_team_Kings_XI_Punjab = 0
    bowl_team_Kolkata_Knight_Riders = 0
    bowl_team_Lucknow_Super_Giants = 0
    bowl_team_Mumbai_Indians = 0
    bowl_team_Rajasthan_Royals = 0
    bowl_team_Royal_Challengers_Bangalore = 0
    bowl_team_Sunrisers_Hyderabad = 0


    if batting_team == 'Chennai Super Kings':
        bat_team_Chennai_Super_Kings += 1
    if bowling_team == 'Chennai Super Kings':
        bowl_team_Chennai_Super_Kings += 1

    if batting_team == 'Sunrisers Hyderabad':
        bat_team_Sunrisers_Hyderabad += 1
    if bowling_team == 'Sunrisers Hyderabad':
        bowl_team_Chennai_Super_Kings += 1

    if batting_team == 'Mumbai Indians':
        bat_team_Mumbai_Indians += 1
    if bowling_team == 'Mumbai Indians':
        bowl_team_Mumbai_Indians += 1

    if batting_team == 'Royal Challengers Bangalore':
        bat_team_Royal_Challengers_Bangalore += 1
    if bowling_team == 'Royal Challengers Bangalore':
        bowl_team_Royal_Challengers_Bangalore += 1

    if batting_team == 'Kolkata Knight Riders':
        bat_team_Kolkata_Knight_Riders += 1
    if bowling_team == 'Kolkata Knight Riders':
        bowl_team_Kolkata_Knight_Riders += 1

    if batting_team == 'Kings XI Punjab':
        bat_team_Kings_XI_Punjab += 1
    if bowling_team == 'Kings XI Punjab':
        bowl_team_Kings_XI_Punjab += 1

    if batting_team == 'Rajasthan Royals':
        bat_team_Rajasthan_Royals += 1
    if bowling_team == 'Rajasthan Royals':
        bowl_team_Rajasthan_Royals += 1

    if batting_team == 'Delhi Capitals':
        bat_team_Delhi_Capitals += 1
    if bowling_team == 'Delhi Capitals':
        bowl_team_Delhi_Capitals += 1

    if batting_team == 'Gujarat Titans':
        bat_team_Gujarat_Titans += 1
    if bowling_team == 'Gujarat Titans':
        bowl_team_Gujarat_Titans += 1

    if batting_team == 'Lucknow Super Giants':
        bat_team_Lucknow_Super_Giants += 1
    if bowling_team == 'Lucknow Super Giants':
        bowl_team_Lucknow_Super_Giants += 1











    input_df = pd.DataFrame({'bat_team_Chennai_Super_Kings': [bat_team_Chennai_Super_Kings],
                             'bat_team_Delhi_Capitals': [bat_team_Delhi_Capitals],
                             'bat_team_Gujarat_Titans': [bat_team_Gujarat_Titans],
                             'bat_team_Kings_XI_Punjab': [bat_team_Kings_XI_Punjab],
                             'bat_team_Kolkata_Knight_Riders': [bat_team_Kolkata_Knight_Riders],
                             'bat_team_Lucknow_Super_Giants': [bat_team_Lucknow_Super_Giants],
                             'bat_team_Mumbai_Indians': [bat_team_Mumbai_Indians],
                             'bat_team_Rajasthan_Royals': [bat_team_Rajasthan_Royals],
                             'bat_team_Royal_Challengers_Bangalore': [bat_team_Royal_Challengers_Bangalore],
                             'bat_team_Sunrisers_Hyderabad': [bat_team_Sunrisers_Hyderabad],
                             'bowl_team_Chennai_Super_Kings': [bowl_team_Chennai_Super_Kings],
                             'bowl_team_Delhi_Capitals': [bowl_team_Delhi_Capitals],
                             'bowl_team_Gujarat_Titans': [bowl_team_Gujarat_Titans],
                             'bowl_team_Kings_XI_Punjab': [bowl_team_Kings_XI_Punjab],
                             'bowl_team_Kolkata_Knight_Riders': [bowl_team_Kolkata_Knight_Riders],
                             'bowl_team_Lucknow_Super_Giants': [bowl_team_Lucknow_Super_Giants],
                             'bowl_team_Mumbai_Indians': [bowl_team_Mumbai_Indians],
                             'bowl_team_Rajasthan_Royals': [bowl_team_Rajasthan_Royals],
                             'bowl_team_Royal_Challengers_Bangalore': [bowl_team_Royal_Challengers_Bangalore],
                             'bowl_team_Sunrisers_Hyderabad': [bowl_team_Sunrisers_Hyderabad],
                             'overs': [overs],
                             'runs': [runs],
                             'wickets': [wickets],
                             'run_last_5': [run_last_5],
                             'wicket_last_5': [wicket_last_5]})


    if batting_team == bowling_team:
        st.header("Alert: Batting and Bowling team should not be same!!")
    else:
        if wickets >=10:
            st.header("Projected Score: " + str(int(runs))  + " --All Out...!!")
        else:
            # st.table(input_df)
            result = regressor.predict(input_df)
            st.header("Projected Score: " + str(result))
    # st.table(input_df)
    # result = regressor.predict(input_df)
    # st.header("Projected Score: " + str(result))
