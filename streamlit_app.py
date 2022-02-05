from collections import namedtuple
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

#Homework 1: Deleted the starter code and am now writing my own code below

st.title('Homework 1 Github and Streamlit')
st.write('By Mariya Tasnim')

st.write('I was thinking of a project where we help students create the best school class-free time schedule for themselves')
#st.write('Below is a sample schedule students may have')

st.metric(label="Student 1", value="8-8:50 AM", delta="10% likelihood to attend")
col1, col2, col3 = st.columns (3)
col1.metric("Student 1", "8-8:50AM", "10% likelihood to attend")
col2.metric("Student 2", "8-8:50AM", "30% likelihood to attend")
col3.metric("Student 3", "8-8:50AM", "50% likelihood to attend")

#array=np.array
#columns=('student $d' %for i in range (3))
#st.table()