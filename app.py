import streamlit as st

st.title(" Tool for detecting defects in software requirement specification")
x=st.text_input("write your Non-funcationl requriment", value="")

weakWords=['fast','quickly', 'easy', 'timely', 'before', 'after', 'user-friendly', 'effective', 'multiple', 'as possible', 'appropriate', 'normal', 'capability', 'reliable', 'state-of-the-art', 'effortless', 'multi']
unboundedList=['at least','more than','less than','not less than','no less than','at the minimum','always']
ambiguity=['should','may','if possible','when','when appropriate','detail','details','analyse','respond','verified']
ambiguityWeakWords=['support','relevant information','needed information']
button=st.button("click",on_click=None)


if button:
    for word in weakWords:
        if (word in x): 
            st.text("The requrement classified as: Bad\nThe wrong word: " +word+"\ncategory: Weak Words")
    for word in unboundedList:
        if (word in x):
            st.text("The requrement classified as: Bad\nThe wrong word: " +word+"\ncategory: Unbounded List")

    for word in ambiguity: 
        if (word in x):
            st.text("The requrement classified as: Bad\nThe wrong word: " +word+"\ncategory: Ambiguity")
    for word in ambiguityWeakWords: 
        if (word in x):
            st.text("The requrement classified as: Bad\nThe wrong word: " +word+"\ncategory: Ambiguity & WeakWords")
        # elif(word not in x):
        #     st.text("The requrement classified as: Good")
