import openai
import streamlit as st
from PIL import Image

def load_image(img):
    im=Image.open(img)
    return im
size=20

st.markdown("<h1 style='text-align: center; color: white;'>OpenFact 💬</h1>", unsafe_allow_html=True)
st.markdown("---")
with st.sidebar:
    st.title("OpenFact")
    st.caption('''
    OpenFact aims to provide solution to verify whether the fact is true or not. In this new world, we are surrounded with lots of information but all the facts on the web are not always true.  OpenFact keeps you safe from the rumours and makes you always stand for the correct.
    ''', unsafe_allow_html=False)
 


ques=st.text_area("Input the fact Here")
button=st.button("Generate")



def gen_auto_response(ques):
    openai.api_key=st.secrets["api"]
    
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Fact is provided below\nFact:{ques}\nWhether the Fact is correct or not:\n\nNo, the fact is not correct. Mark Zuckerburg is the founder of the social media platform Facebook, but he did not build a computer.",
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    print(response)
    return response.choices[0].text

if ques and button:
    with st.spinner("-------Checking the Fact------"):
        reply=gen_auto_response(ques)
        st.write(reply)
        
      

