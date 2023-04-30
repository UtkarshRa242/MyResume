import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie



st.set_page_config(page_title='Welcome',page_icon='😎',layout='wide')

def load_lottie(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

#assets
lottie_code = load_lottie('https://assets4.lottiefiles.com/private_files/lf30_mvninbvf.json')
my_face = (Image.open('images/miphoto.png')).resize((300,300))
enquero = Image.open('images/Enquero.png')
triponzy = Image.open('images/triponzy.png')
enr = Image.open('images/enr.png')


#header seccion

with st.container():
    lftclm,ritclm=st.columns(2)
    with lftclm:
        st.subheader("Hola!, Me llamo Utkarsh Rastogi :wave:")
        st.title("I am an SDE Intern at Enquero Global")
        st.write("You are here, that means you are interested in me(or my skills)")
        st.write('[Wanna know more?](https://www.linkedin.com/in/amazingrastogi/)')
    with ritclm:
        st.image(my_face,caption='Beware of fakes, this is how I look 😅')


# wtf I do?
with st.container():
    st.write("----")
    lftclm,ritclm=st.columns(2)
    with lftclm:
        st.header("What I do(or atleast try)")
        st.write("##")
        st.write(
            """
            I do python and sometimes python does me 😏.
            I am always interested in watching creative ads and listening to music.
    
            """
        )
    with ritclm:
        st_lottie(lottie_code,height=300,key='gayming')

 # achievements
 
with st.container():
    st.write('----')
    st.header("Work Experience")
    st.write("##")
    imgclm, txtclm = st.columns((1,2))
    #with imgclm:
        #insert shit
    with txtclm:
        st.subheader("GET at Enquero Global")
        st.write(
            """
            Learning many things at the same time like Python, HTML, bureaucracy, project management, money management
            """
        )
    with imgclm:
        st.image(enquero)
with st.container():
    imgclm,txtclm = st.columns((1,2))
    with txtclm:
        st.subheader("Content Writing Intern at EnR Consultancy Services")
        st.write(
            """
            Wrote LinkedIn, Facebook posts, tech blogs, rewrote NDA and LOR documents
            """
        )
    with imgclm:
        st.image(enr)
with st.container():
    imgclm,txtclm = st.columns((1,2))
    with txtclm:
        st.subheader("Content Writing Intern at Triponzy")
        st.write(
            """
            Wrote long articles related to travel and stuff
            """
        )
    with imgclm:
        st.image(triponzy)
# Contact Me!!!!
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/utkarshrastogimrt@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
