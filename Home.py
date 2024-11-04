import streamlit as st
import pandas

csv = pandas.read_csv("data/data.csv", sep=";")
st.set_page_config(layout="wide", page_title="Jack Killelea - Portfolio")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png", width=700)

with col2:
    st.title("Jack Killelea")
    about_me = """I’m a mobile application developer with a passion for crafting engaging user experiences. 
    My background spans various roles, from developing enterprise-level software at Chubb Fire and Security to contributing to the Next Retail app at Next PLC. 
    Currently, I’m part of the Android development team at TouchStar, where I specialize in C# using Xamarin and .NET MAUI.
    Beyond mobile development, I enjoy exploring other areas of software and game development. 
    I’ve built several console games, experimented with VR projects, and even dabbled in web scraping. 
    I’m always eager to learn new technologies and tackle challenging projects. Outside of work, 
    I’m a gaming enthusiast, snowboarder, and enjoy 3D printing and model painting."""
    st.info(about_me)

col3, spacing, col4 = st.columns([1.5, 0.5, 1.5])
with col3:
    for index, row in csv.iterrows():
        if index % 2:
            st.header(row["title"])
            st.write(row["description"])
            st.image(f"images/{row['image']}")
            st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in csv.iterrows():
        if index % 2 == 0:
            st.header(row["title"])
            st.write(row["description"])
            st.image(f"images/{row['image']}")
            st.write(f"[Source Code]({row['url']})")
