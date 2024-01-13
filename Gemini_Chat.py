import re
import google.generativeai as genai


API_KEY = ""  #Add API Key

genai.configure(api_key=API_KEY)

instructions = "*** YOUR NAME IS LEO YOU ARE A VIRTUAL FRIEND ***"  #Replace with Ur own instructions


#
settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},      
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]

clean = re.compile(r'[^a-zA-Z,\s]')
model = genai.GenerativeModel(model_name="gemini-pro", safety_settings=settings)




def gemini_chat(message:str):
    previous_response = ""
    chat = model.start_chat()
    full_prompt = f"{message}\n{previous_response}\n{instructions}"
    response = chat.send_message(full_prompt)
    cleaned_response = clean.sub('', response.text)
    previous_response = cleaned_response
    return cleaned_response


gemini_chat("Hello")


