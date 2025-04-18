# Groq LLM Chat - Streamlit App
This repository contains a Streamlit app that enables you to interact with the Groq LLM API. The app allows users to chat with a powerful language model and displays token usage for each conversation. You can choose between different models, configure the temperature setting, and view responses generated by the selected model.

Features
Multi-Model Support: Choose between available models such as llama2-70b-chat, mixtral-8x7b, and gemma-7b-it for chatting.
Interactive Chat: The app provides an interface where users can type their messages, and the model will generate responses in real-time.
Token Usage Tracking: Displays token usage for both prompt and completion tokens to track consumption during chat sessions.
Customizable Temperature: Adjust the temperature parameter to control the randomness of the model’s responses.
Groq API Integration: Uses the Groq API for generating responses based on selected models.

Prerequisites
To run this application, you’ll need the following:
Python 3.x or later
Streamlit: For building the web-based user interface.
Requests: For making API calls to Groq’s API.
python-dotenv: For securely loading environment variables like API keys.

How the App Works
Groq API Key:

The app loads the Groq API key from the .env file using the python-dotenv library.

If the API key is missing or invalid, the app will show an error message.

Streamlit Interface:

The main interface features:

A sidebar where you can select the model and adjust the temperature setting.
A chat area to see the conversation history and type your messages.

Model Selection:

The sidebar allows you to choose between three models: llama2-70b-chat, mixtral-8x7b, and gemma-7b-it.
You can also adjust the temperature slider, which controls how random or creative the model's responses are.

Token Usage Tracking:

The app tracks the token usage for both the prompt and the completion of each interaction.
Token statistics are displayed in the sidebar, showing the prompt tokens, completion tokens, and total tokens used.

Conversation History:
Each message sent by the user and received from the assistant is displayed in the chat area.
As the conversation progresses, the messages are appended to the session state to maintain the conversation context.

API Interaction:
Every time the user submits a message, the app sends a request to the Groq API with the selected model, message history, and temperature setting.
It then parses the response and displays the assistant's reply in the chat interface.
If there are any errors during the API request, an error message will be displayed.

Error Handling
Missing API Key: If the API key is not set or is incorrect, the app will display an error message instructing the user to check the .env file.
API Request Failures: If the API request fails (e.g., network issues or an invalid response), an error message will be displayed in the chat area.

Customizing the App
You can easily customize the app by modifying the following components:
Models: You can add or remove models from the available_models list in the code.
Temperature Range: Adjust the minimum and maximum values for the temperature slider in the code if you want to control the randomness differently.

