import cv2
import google.ai.generativelanguage as glm
import google.generativeai as genai
import textwrap


    
GOOGLE_API_KEY_PATH = 'api/gemini.txt'
GOOGLE_API_KEY = open(GOOGLE_API_KEY_PATH).read().strip()

genai.configure(api_key=GOOGLE_API_KEY)

MODEL_NAME = 'gemini-pro-vision'

model = genai.GenerativeModel(MODEL_NAME)

def to_markdown(text):
    text = text.replace('*', ' ')
    print(textwrap.indent(text, '>', predicate=lambda _: True))


def detect(prompt):
    
    genai.configure(api_key=GOOGLE_API_KEY)
    MODEL_NAME = 'gemini-pro-vision'
    model = genai.GenerativeModel(MODEL_NAME)
    
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        print("Error reading from webcam")
    else:
        ret, jpeg = cv2.imencode('.jpg', frame)
        image_bytes = jpeg.tobytes()
        response = model.generate_content(
            glm.Content(
                parts=[
                    glm.Part(text=prompt+"Describe this image in short words what you see?"),
                    glm.Part(
                        inline_data=glm.Blob(
                            mime_type="image/jpeg",
                            data=image_bytes,
                        ),
                    ),
                ],
            ),
            stream=True
        )
        response.resolve()
        to_markdown(response.text)
    cap.release()
    cv2.destroyAllWindows()
    


if __name__ == "__main__":
    
  detect()
