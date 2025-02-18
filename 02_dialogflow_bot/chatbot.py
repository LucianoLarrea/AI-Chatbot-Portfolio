import dialogflow_v2 as dialogflow
import json
import os

# Configura la ruta a tu archivo de credenciales JSON
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

# ID del proyecto en Dialogflow
PROJECT_ID = "your-dialogflow-project-id"

def detect_intent(text, session_id="12345"):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PROJECT_ID, session_id)

    text_input = dialogflow.types.TextInput(text=text, language_code="en")
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)

    return response.query_result.fulfillment_text

if __name__ == "__main__":
    print("Dialogflow Chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = detect_intent(user_input)
        print(f"Chatbot: {response}")
