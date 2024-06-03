import time
from PIL import Image
import streamlit as st
from excuses import Excuses
from prompts import PromptCls
from gorqKey import GorqKey
from groq import Groq
from streamlit_chat import message


def Gorq_function(model_name = "llama3-70b-8192"):
    
    ################################################
    
    client = Groq(api_key = str(GorqKey()))
    
    ################################################
    col1, col2 = st.columns((1, 2.5))

    original = Image.open("Image1/tony.jpg")
    col1.image(original, use_column_width=True)
    col1.info(":blue[Hey, I'm from groq! Happy to help you!] 😊")
    container_11 = col2.container(height = 350, border = False)
    
    ################################################
    
    ################################################
        
    if "messages_temp_F" not in st.session_state:
        st.session_state.messages_temp_F = []


    k = 1
    with container_11:

        for message_s in st.session_state.messages_temp_F:
            if message_s["role"] == "Dipankaruser":
                message(message_s["content"], is_user = True, key = str(k) + '_user', avatar_style = "initials", seed = "Dipankar Porey")
            elif message_s["role"] == "Gorqassistant":
                message(message_s["content"], key = str(k), avatar_style = "initials", seed = "Tony", allow_html = True)
            k += 1

    def clear_chat_history():
        
        st.session_state.messages_temp_F = []
        
    st.sidebar.button(':green[*Clear chat*]', on_click = clear_chat_history)
            
    if prompt := st.chat_input("Ask me !"):
        
        with container_11:
            
            st.session_state.messages_temp_F.append({"role": str("Dipankar")+"user", "content": prompt})
            

            message(prompt, is_user = True, key = str(k) + '_user', avatar_style = "initials", seed = "Dipankar Porey")

            k += 1
            full_response = ""
            with st.spinner(":green[Thinking . . .]"):
                try: 
                    
                    # prompt = PromptCls.GorqPromptStyle(prompt)
                    # prompt = PromptCls.GorqPromptStyleVanilla(prompt)
                    chat_completion = client.chat.completions.create(
                        messages = [{"role": "user",
                                    "content": prompt,}],
                                    model = model_name,
                        )

                    full_response = chat_completion.choices[0].message.content
                    message(full_response , key = str(k), avatar_style = "initials", seed = "Tony", allow_html=True)
                
                except Exception as e:
                    
                    full_response = Excuses.listofExcuses()
                    message(full_response, key = str(k), avatar_style = "initials", seed = "Tony", allow_html=True)
                
            st.session_state.messages_temp_F.append({"role": str("Gorq")+"assistant", "content": full_response})
