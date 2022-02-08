from collections import namedtuple
from lib2to3.pgen2.pgen import DFAState
import altair as alt 
import numpy as np
import pandas as pd
import streamlit as st
import graphviz as graphviz
import datetime as datetime

#Homework 1: Deleted the starter code and am now writing my own code below
#I want to make it clear that only the Streamlit documentation was used to complete this portion of the assignment
#The examples provided in the documentation helped me complete this homework and the code provided was used to help me write the code below!
#docs.streamlit.io was used to complete this part of the homework assignment

st.set_page_config(
     page_title="Get to know Mariya: Homework 1",
     page_icon="🧊",
     layout="centered",
     initial_sidebar_state="auto",
     menu_items=None
 )

#  # Initialization
# if 'key' not in st.session_state:
#     st.session_state['key'] = 'value'

# # Session State also supports attribute based syntax
# if 'key' not in st.session_state:
#     st.session_state.key = 'value'
# # Reads
# st.write(st.session_state.key)

# # Outputs: value

st.title('Homework 1 Github and Streamlit')
st.write('By Mariya Tasnim')

st.header('Get to know me')
st.write('Hi! My name is Mariya and I will introduce myself through this homework assignment.')
with st.expander("Some facts about me"):
    st.write('I am a Systems MEng student graduating in May 2022. I just received my BS in MechE from Cornell')
    st.write('I was born and raised in Brooklyn, NY.')
    st.write('I am taking this class to learn about data science from a systems perspective.')

with st.container():
    st.write('I tend to stay up late at night working on assignments and prefer to wake up a bit later, which is why classes with later start times are very appealing to me.')
    st.write('Here is a fun example of how difficult it is for me to attend class early in the morning.')
    st.metric(label="Class time", value="8-8:50 AM", delta="10% likelihood to choose class")
    st.write('In other words, I will be picking a class with this start time only if it was required for my degree.')
    col1, col2, col3 = st.columns (3)
    col1.metric("Class 1", "8-8:50 AM", "30% likelihood to attend and be on time")
    col2.metric("Class 2", "9:05-9:55 AM", "50% likelihood to attend and be on time")
    col3.metric("Class 3", "10:10-11 AM", "100% likelihood to attend and be on time")
    #st.write('If I had the option of picking between these 3 classes, I would choose Class 3, since I would attend all lectures on time.')
    if st.button('Click'):
        st.write('Class 3')
    else:
        st.write('See which class I would pick')

st.write('Below is the typical schedule for a grad student:')
st.graphviz_chart('''
    digraph {
        wakeup -> shower
        shower -> eat
        eat -> work
        work -> class
        class -> meetings
        meetings -> work
        work -> eat
        eat -> sleep
    }
''')

#t = st.time_input('Currently the time is', datetime.time())
option = st.selectbox(
     'What are you currently doing?',
     ('Working', 'Eating','Waking up', 'Sleeping','Meeting'))

st.write('You selected:', option)

st.balloons()

with st.form("favorite number"):
    st.write("What is your favorite number?")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Have you moved the slider")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Your favorite number is", slider_val, "My favorite number is 4 and the checkbox is clicked", checkbox_val)


st.write('I used st.help here to understand how to use the st.image function')
from PIL import Image
st.help(st.image)
image=Image.open('grad pic 2.jpg')
st.image(image, caption='This is me during May 2021 Commencement at Cornell')
st.write('My favorite sport is hockey and I enjoy going to the Cornell mens hockey team games. Below is a video from the 2021 Cornell versus Yale game')
videofile=open('IMG-5582.mov','rb')
hockeyvideo=videofile.read()
st.video(hockeyvideo)
#st.video()


st.write('Below, I experiment with some of the features in Streamlit.')
#df=pd.DataFrame()
array1=np.array([[1. ,2. ,3.], [4. ,5. ,6.]])
array2=np.array([[4. ,5. ,6.], [7. ,8. ,9.]])
# my_df=st.dataframe(array1)
# my_df2=st.dataframe(array2)
# mytable=st.table(my_df)
my_df=pd.DataFrame(array1)
my_df2=pd.DataFrame(array2)
mytable=st.table(my_df)
mytable2=mytable.add_rows(my_df2)
#array3=my_df.add_rows(array2)
#rows are x coordinates and columns are y coordinates
st.line_chart(my_df)

st.success('You have reached the end. I hope you enjoyed going through this.')
#From each category, these functions were used
#used st.write. need to use magic.
#st.title an st.write
#st.dataframe, st.metric
#st.line_chart, st.graphviz_chart
#st.button, st.selectbox
#st.container, st. expander
#st.success, st.balloons()
#st.form, st.form_submit_button
#st.set_page_config, st.help
#Mutate charts did one
#State Management need to do
#Performance need to do
#st.image, st.video 


# st.write('I was thinking of a project where we help students create the best school class-free time schedule for themselves')
# #st.write('Below is a sample schedule students may have')

# st.metric(label="Student 1", value="8-8:50 AM", delta="10% likelihood to attend")
# col1, col2, col3 = st.columns (3)
# col1.metric("Student 1", "8-8:50AM", "10% likelihood to attend")
# col2.metric("Student 2", "8-8:50AM", "30% likelihood to attend")
# col3.metric("Student 3", "8-8:50AM", "50% likelihood to attend")

# st.write('A typical class schedule looks like this')
# df=pd.DataFrame()
# #array=np.array
# #columns=('student $d' %for i in range (3))
# #st.table()

