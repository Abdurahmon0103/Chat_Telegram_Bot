from google import genai
client = genai.Client(api_key="AIzaSyDCYRBoyDrNEf154YntSmY92XQvthVRO-8")
def ai():      
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"""{message.text}"""
    )
    return response.text