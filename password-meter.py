import streamlit as st
import re 

st.set_page_config(page_title='Password Strength Meter',page_icon='🔏')

st.title('Password Strength Meter 🔏')
st.write('**This app will check the strength of your password and provide a score based on the following**')


password = st.text_input("Enter your Password here 🔏",type='password')

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append('❌ Password should be at least 8 characters long')
    if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password):
        score += 1
    else:
       feedback.append('❌ Password should have at least one upper case and one lower case')    
    if re.search(r'\d',password):
           score +=1
    else:
        feedback.append('❌ Password should have at least one digit')
    if re.search(r'[!@#$%&]', password):
        score += 1
    else:
        feedback.append('❌ Password should contain atleast one special character(!@#$%&)')

    if score == 4:
        feedback.append("✅ Password is strong!")
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Try to make strong password.")
    else:
        feedback.append("🔴 Weak Password - Improve it by the given suggestions.")


    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
else:
        st.info("Please Enter your password to get started ")            
           