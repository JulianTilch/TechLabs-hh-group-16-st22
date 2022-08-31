import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('final_model2.sav', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

st.title("loc[AI]tion")

st.write("""### You choose your preferences - We predict your rent""")

state_list = ['state_Baden_Württemberg', 'state_Bayern', 'state_Berlin',
       'state_Brandenburg', 'state_Bremen', 'state_Hamburg', 'state_Hessen',
       'state_Mecklenburg_Vorpommern', 'state_Niedersachsen',
       'state_Nordrhein_Westfalen', 'state_Rheinland_Pfalz', 'state_Saarland',
       'state_Sachsen', 'state_Sachsen_Anhalt', 'state_Schleswig_Holstein',
       'state_Thüringen']

for i in state_list:
       exec("%s = %d" % (i,0)) # The exec() command makes a value as the variable name
               

# Enter data for prediction 
state = st.selectbox('State',
                              ('Baden Württemberg', 'Bayern', 'Berlin',
                               'Brandenburg', 'Bremen', 'Hamburg', 'Hessen',
                               'Mecklenburg Vorpommern', 'Niedersachsen',
                               'Nordrhein Westfalen', 'Rheinland Pfalz', 'Saarland',
                               'Sachsen', 'Sachsen Anhalt', 'Schleswig Holstein',
                               'Thüringen'))
               
if state=='Baden Württemberg':
    state_Baden_Württemberg =1
elif state=='Bayern':
    state_Bayern =1
elif state=='Berlin':
    state_Berlin =1
elif state=='Brandenburg':
    state_Brandenburg =1
elif state=='Bremen':
    state_Bremen =1
elif state=='Hamburg':
    state_Hamburg =1
elif state=='Hessen':
    state_Hessen =1
elif state=='Mecklenburg Vorpommern':
    state_Mecklenburg_Vorpommern =1
elif state=='Niedersachsen':
    state_Niedersachsen =1
elif state=='Nordrhein Westfalen':
    state_Nordrhein_Westfalen =1
elif state=='Rheinland Pfalz':
    state_Rheinland_Pfalz =1
elif state=='Saarland':
    state_Saarland =1
elif state=='Sachsen':
    state_Sachsen =1
elif state=='Sachsen Anhalt':
    state_Sachsen_Anhalt =1
elif state=='Schleswig Holstein':
    state_Schleswig_Holstein =1
elif state=='Thüringen':
    state_Thüringen =1
else: 
    pass

living_space = st.slider("Living Space [sq m]", 1, 300, 40)

num_rooms = st.slider("Number of Rooms", 1, 20, 2)

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

balcony = st.radio("Balcony",('yes', 'no'))
if balcony == "yes":
    balcony = 1
else:
    balcony = 0
    
kitchen = st.radio("Kitchen",('yes', 'no'))
if kitchen == "yes":
    kitchen = 1
else:
    kitchen = 0
    
lift = st.radio("Lift",('yes', 'no'))
if lift == "yes":
    lift = 1
else:
    lift = 0

newly_constructed = st.radio("Newly Constructed",('yes', 'no'))
if newly_constructed == "yes":
    newly_constructed = 1
else:
    newly_constructed = 0
    
year_constructed = st.slider("Year of Construction", 1900, 2022, 1980)


ok = st.button("Calculate Rent")
if ok:
    X = np.array([[newly_constructed, balcony, year_constructed, kitchen, living_space, lift, num_rooms, state_Baden_Württemberg,
                   state_Bayern, state_Berlin, state_Brandenburg, state_Bremen, state_Hamburg, state_Hessen,
                   state_Mecklenburg_Vorpommern,state_Niedersachsen, state_Nordrhein_Westfalen, state_Rheinland_Pfalz, state_Saarland,
                   state_Sachsen, state_Sachsen_Anhalt, state_Schleswig_Holstein, state_Thüringen]])
                   
                   
    X = X.astype(float)

    rent = data.predict(X)
    st.subheader(f"The estimated rent is {rent[0]:.2f}€")