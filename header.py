import streamlit as st
from PIL import Image
from gorq_function import Gorq_function

st.set_page_config(page_title='Groq Chatbot', layout="wide", page_icon = 'Image1/a3.jpg', initial_sidebar_state = 'auto')

st.markdown("""
<style>
.big-font-1 {
    font-size:20px !important;
    text-align: center; 
    color: yellow
}
</style>
""", unsafe_allow_html=True)


def main(): 
    st.sidebar.markdown('<p class="big-font-1">Groq</p>', unsafe_allow_html = True)
    
    st.sidebar.image("Image1/17.png")
   
    model_name_check = st.sidebar.selectbox(""":blue[**Choose Model**]""", ("Llama3-70B", "Llama3-8B", "Mixtral-7B", "Gemma-7B"))

    model_name = "llama3-70b-8192"
    if model_name_check == "Llama3-70B" :
        model_name = "llama3-70b-8192"
    elif model_name_check == "Llama3-8B" :
        model_name = "llama3-8b-8192"
    elif model_name_check == "Mixtral-7B" :
        model_name = "mixtral-8x7b-32768"
    elif model_name_check == "Gemma-7B" :
        model_name = "gemma-7b-It"

    Gorq_function(model_name = model_name)

    show_advanced_info_1 = st.sidebar.toggle(":blue[*Show Application Details*]", value = True)
    
    if show_advanced_info_1:
        st.sidebar.info("""

                    **Generative AI application**

                    - **About:** *Chatbot with Groq*
                    
                    - **Model:** *Llama3, Llama2, Mixtral, Gemma with Groq backend*
                    
                    - **Language:** *English*
                    
                    - **Release Date:** *April, 2024*
                    
                    """)
        
    show_advanced_info_2 = st.sidebar.toggle(":blue[*Show Developer Details*]", value = False)
    
    if show_advanced_info_2:
        st.sidebar.info("""
                    
                    *This appplication has been created by [:blue[Dipankar Porey]](https://www.linkedin.com/in/dipankar-porey-403320259/), 
                    Technology Consultant, Senior at Ernst & Young LLP.* 
                    
                    """)

       
if __name__ == '__main__':
    main()
