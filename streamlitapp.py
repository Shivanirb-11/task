#Edit the 8th to 12th line code before upload to gihub
# Import necessary libraries
import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd


# --- Title and Introduction ---
st.title("Interactive Visualizations with Plotly and Streamlit")


# --- Input for Author Information ---
st.sidebar.header("Visualization skill workshop - Plotly")
name = st.sidebar.text_input("Enter your name")
usn = st.sidebar.text_input("Enter your roll no.")
instructor_name = st.sidebar.text_input("Course Intructor Name")


# Display author information if provided
if name and usn and instructor_name:
    st.markdown(
        f"<h5 style='color: teal;'>Created by:</h5>"
        f"<p style='color: white;'>{name} (USN: {usn})</p>"
        f"<p style='color: white;'>Instructor: {instructor_name}</p>",
        unsafe_allow_html=True
    )


# --- Load Dataset ---
tips = sns.load_dataset('tips')  # Loading the tips dataset


# Display the first few rows of the dataset
st.write("## Dataset Overview")
st.write(tips.head())


# --- Task 2: Interactive Bar Chart ---
st.subheader("Task 2: Bar Chart - Average Tip by Day")
# Bar Chart: Average Tip by Day with color for each day
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
st.plotly_chart(fig2)  # Display the chart in Streamlit
fig4 = px.scatter(
    dataset, x='total_bill', y='tip', color='sex',
    title='total bill vs tip (colored by gender)',
    labels={'total_bill':'total bill($)', 'tip':'tip($)'},
    template='plotly_dark', #using a cool dark theme
    size='size' #the size of points based on the size of the group
)
fig4.show()

fig5 = px.box(
    dataset, x='day' , y='total_bill', color='time',
    title='Total Bill by day',
    labels={'tip': 'Total bill ($)', 'day':'Day of the week'},
    template='plotly_white', #clean white background
)
fig5.show()
fig6 = px.histogram(
    dataset, x='day' , y='tip', color='day',
    title=' Tip distribution by day',
    labels={'tip': 'Average Tip ($)', 'day':'Day of the week'},
    template='plotly_white', #clean white background
)
fig6.show()
