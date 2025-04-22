#sreamlit
import streamlit as st

st.set_page_config(page_title = "Growth Mindset Project", project_icon = "🌱")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your fill potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements!🌟")


#quote section
st.header("💡Today's Gowth Mindse Quote")
st.write("Sucess in not final, failure in not fatal: it in the courage to continue tha counts. - Winston Churchill")

st.header("🔧What's your challenge today?")
user_input = st.text_input("Describe a challenge tou're facing:")


#condition
if user_input:
    st.sucess(f"💪🏻you are facing: {user_input}. Keep pushing forward towords your goal!")
else:
    st.warning("Tell us about your challenge to get started!")


#reflexing
st.heade("Reflect on your learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.sucess(f"✨ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you to grow! Share your difficulties")


#achievements
st.header("🏆Celebrate your wins!")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"👏🏻Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now🤩")


#footer
st.write("- - -")
st.write("🤞Keep believing in yourself. Growth in a journey , not a destination!")
st.write("**Created by Salika Syed✍️**")
