import streamlit as st

st.title("welcome to bar island")

st.write(f"we are introdusing two new drink in house .\n do vote tour fev.")

cl1,cl2=st.columns(2)
with cl1:
    st.subheader('Assam tea')
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSviWGcsJEPWsmeQTrrE57CBBULrXGATxZiUrIdmu7axg&s=10",width=200)
    v1=st.button("vote for assam tea")



with cl2:
    st.subheader('Mango Boba tea')
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgbfsSW_tY_dDP-sphRr3O1fLO3tSfCTvy5numnFe-rA&s=10",width=200)
    v2=st.button("vote for mango boba tea")



if v1:
    st.success("you are voted for assam tea")

if v2:
    st.success("you are voted for mango boba tea")



st.sidebar.subheader("customize your drink")
st.sidebar.write("tell me about you and your drink")
n=st.sidebar.text_input("your name")




c=st.sidebar.selectbox("select your base",['almond milk','goat milk','water','coconut milk'])
a=st.sidebar.slider("suger level in spoon",0,5,1)
s=st.sidebar.success(f"you want {a} spoon of suger")

b=st.sidebar.checkbox('would you like add cinnemon')
if b:
    st.success("adding cinnemon")
    st.balloons()

st.write(f'welcome {n} !! you have orderd tea with {c} as a base containing {a} tea spoon suger ')





