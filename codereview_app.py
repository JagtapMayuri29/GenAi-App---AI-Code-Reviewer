import streamlit as st
import google.generativeai as genai

#setting up the API key
genai.configure(api_key = "Replace with your valid API Key")

#setting up the headers
st.title("👨‍💻:violet[AI Python Code Reviewer..!!]💭")
st.subheader(':green[***Issues with your python code? Review your codebase now!***]🧐')

#taking user input
user_prompt = st.text_area("Enter your Python code here...!",placeholder="Paste your code here.....",height=200)

#prompt is provided
sys_prompt=("""You are a friendly AI assistant.
                                                    Given a python code to review, analyze the submitted code and identify bugs, errors or areas of improvement.
                                                    Provide the fixed code snippets.
                                                    Explain the reasoning behind code corrections or suggestions. 
                                                    If the code is not in python politely 
                                                    remind the user that you are a python code review assistant.
                                                   """)

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash",system_instruction=sys_prompt)

#if the button is clicked, generate responses
button = st.button(":red[Generate Review]")
if button:
    response = model.generate_content([user_prompt,sys_prompt])
    st.title(":red[Corrected Bug...🧐]")

 #printing the response on the webpage
    st.write(response.text)
    
