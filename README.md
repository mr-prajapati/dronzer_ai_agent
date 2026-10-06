# 🤖 Gemini AI Chatbot

Gemini AI Chatbot is a simple and interactive AI chatbot developed using Python and the Google Gemini API. The project allows users to communicate with Google's Gemini AI directly through the terminal and supports continuous conversations using the Gemini Chat SDK.

## Features

• Powered by Google Gemini AI
• Continuous conversation using Gemini Chat SDK
• Fast responses using Gemini Flash model
• User-friendly terminal interface
• Secure API key management using .env file
• Conversation context maintained during the chat session
• Type "endchat" to exit the chatbot
• Response handling without unnecessary thought_signature warnings

## Technologies Used

• Python
• Google Gemini API
• Google GenAI SDK
• Python-dotenv
• VS Code
• Git & GitHub

## Project Files

The project contains the following important files:

• basic.py – Basic Gemini API implementation and experimentation.
• text_generation.py – Generates AI responses based on user prompts and system instructions.
• chatbot_demo.py – Demonstrates a basic terminal-based chatbot.
• chat_SDK.py – Main chatbot using Gemini Chat SDK for continuous conversation.
• requirement.txt – Contains the required Python packages.
• .env – Stores the Gemini API key securely.
• .gitignore – Prevents sensitive and unnecessary files from being uploaded to GitHub.
• README.md – Project documentation.

## API Key Setup

To use the Gemini API, you need a Gemini API key.

Create a file named ".env" in the project directory and add your API key in the following format:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

The API key should never be shared publicly or uploaded to GitHub.

The .env file should be added to .gitignore to keep the API key secure.

## Installation

First, clone the repository from GitHub:

git clone https://github.com/mr-prajapati/dronzer_ai_agent.git

Then open the project directory:

cd dronzer_ai_agent

Install the required Python packages using:

pip install -r requirement.txt

Make sure Python is installed on your computer before running the project.

## Running the Chatbot

The main chatbot can be started using:

python chat_SDK.py

After running the program, the chatbot will display:

Chat Starts here......Type 'endchat' to stop & exit

The user can then enter questions or messages.

Example:

User : Hello

DRONZER : Hello! How can I help you today?

The conversation can continue with multiple messages.

To stop the chatbot, type:

endchat

## Gemini Chat SDK

The project uses the Gemini Chat SDK to maintain a continuous conversation.

A chat session is created using the Gemini Flash model. User messages are sent to Gemini through the chat session, allowing the chatbot to maintain the context of the conversation.

The chatbot processes the response parts directly and displays only the actual text response. This prevents unnecessary warnings related to non-text response parts such as thought_signature.

## Security

API keys and other sensitive information should never be uploaded to GitHub.

The following files should be included in .gitignore:

.env
apikey
__pycache__/
*.pyc

If an API key is accidentally exposed publicly, it should be revoked immediately and replaced with a new API key.

## Learning Objectives

This project was developed to learn and practice:

• Python programming
• API integration
• Google Gemini API
• Gemini Chat SDK
• Environment variables
• .env configuration
• User input and loops
• AI chatbot development
• Git and GitHub

## How the Chatbot Works

The chatbot starts by loading the Gemini API configuration from the .env file. A Gemini client is then created and a chat session is started using the Gemini Flash model.

The user enters a message, which is sent to Gemini. The generated response is displayed in the terminal. The program continues asking for new messages until the user enters "endchat".

This creates a simple continuous AI conversation through the terminal.

## Author

Dheeraj Kumar

GitHub Repository:
https://github.com/mr-prajapati/dronzer_ai_agent

## License

This project is created for educational and learning purposes.
