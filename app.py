import streamlit as st

st.title(" Tool for detecting defects in software requirement specification")
x=st.text_input("write your Non-funcationl requriment", value="")

weakWords=['fast','quickly', 'easy', 'timely', 'before', 'after', 'user-friendly', 'effective', 'multiple', 'as possible', 'appropriate', 'normal', 'capability', 'reliable', 'state-of-the-art', 'effortless', 'multi']
unboundedList=['at least','more than','less than','not less than','no less than','at the minimum','always']
ambiguity=['should','may','if possible','when','when appropriate','detail','details','analyse','respond','verified']
ambiguityWeakWords=['support','relevant information','needed information']
button=st.button("click",on_click=None)

if button:
    count=0
    x=x.split(" ")
    for word in x:
        #st.write(word)
        if word in weakWords:         
            st.text("The requirement classified as: Bad\nThe wrong word: " +word+"\ncategory: Weak Words")
            count+=1
        elif word in unboundedList:        
            st.text("The requirement classified as: Bad\nThe wrong word: " +word+"\ncategory: Unbounded List")
            count+=1
        elif word in ambiguity:         
            st.text("The requirement classified as: Bad\nThe wrong word: " +word+"\ncategory: Ambiguity")
            count+=1
        elif word in ambiguityWeakWords:         
            st.text("The requirement classified as: Bad\nThe wrong word: " +word+"\ncategory: Ambiguity & WeakWords")
            count+=1
    if count==0:
        st.text("The requirement classified as: Good")

