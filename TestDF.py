import pandas as pd
import streamlit as st 


df = pd.DataFrame({'A' : [4,None], 'B' : [10,20],
                   'C' : [100,50], 'D' : [-30,-50],
                   'E' : [1500,800], 'F' : [0.258,1.366]})

# Apply styler so that the A column will be displayed with integer value because there is None in it.
df_style = df.style.format(precision=2, na_rep='MISSING', thousands=",", formatter={('A'): "{:.0f}"})

st.write('Current dataframe')
st.dataframe(df_style)

# We use a form to wait for the user to finish selecting columns.
# The user would press the submit button when done.
# This is done to optimize the streamlit application performance.
# As we know streamlit will re-run the code from top to bottom
# whenever the user changes the column selections.
with st.form('form'):
    sel_column = st.multiselect('Select column', df.columns,
       help='Select a column to form a new dataframe. Press submit when done.')
    drop_na = st.checkbox('Drop rows with missing value', value=True)
    submitted = st.form_submit_button("Submit")
    
if submitted:
    dfnew = df[sel_column]
    if drop_na:
        dfnew = dfnew.dropna()

    st.write('New dataframe')
    dfnew_style = dfnew.style.format(precision=2, na_rep='MISSING', thousands=",", formatter={('A'): "{:.0f}"})
    st.dataframe(dfnew_style)
