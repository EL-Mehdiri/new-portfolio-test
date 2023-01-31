from PIL import Image
import requests 
import streamlit as st
from streamlit_lottie import st_lottie

# find more emojis her : https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Portfolio", page_icon=":tada:")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# use local css file 
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")


# load assets
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_3rwasyjy.json")
img_contact_form = Image.open("images/Program-Code-Feature-Image.jpg")
img_lottie_animation = Image.open("images/téléchargement.jpg")


# header section
with st.container():
    st.subheader("Hi, I am Mehdi :wave:")
    st.title("A Full Stack Devloper from Maroc")
    st.write("There's no need to spend days or weeks building a website anymore. In this video, I'm going to show you how to build a website with a blog and a contact page in only 12 minutes using Python, Streamlit and other open-source tools.")
    st.write("[Learn More >](https://www.webfx.com)")


# what i do 
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(""" There's no need to spend days or weeks building a website anymore. In this video, I'm going to show you how to build a website with a blog and a contact page in only 12 minutes using Python, Streamlit and other open-source tools.""")
        st.write("[Github Acounte](https://github.com/EL-Mehdiri)")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        #insert image
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie files in streamlite Portfolio")
        st.write(
            """
            learn how to use lottie 1files in streamlit!
            animations make our web app mor engaging and fun, and lottie files are the easiest way to do 
            In this Tutorial I'll show you exactly how to do it 
            """
        )
        st.markdown("[Watch Video ...](htttps://youtube.com)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        #insert image
        st.image(img_contact_form)
    with text_column:
        st.subheader("Integrate Lottie files in streamlite Portfolio")
        st.write(
            """
            learn how to use lottie 1files in streamlit!
            animations make our web app mor engaging and fun, and lottie files are the easiest way to do 
            In this Tutorial I'll show you exactly how to do it 
            """
        )
        st.markdown("[Watch Video ...](htttps://youtube.com)")


# contact form

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # https://formsubmit.co/

    contact_form = """
    <form action="https://formsubmit.co/mehdiridmani@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email" placeholder="your email"  required>
     <textarea name="message" placeholder="your message her" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()