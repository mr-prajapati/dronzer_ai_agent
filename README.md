# 🤖 Gemini AI Chatbot

A simple Python-based AI chatbot that uses the Google Gemini API to generate responses to user prompts.

## 📌 Features

- Interactive command-line chatbot
- Uses Google Gemini API
- Secure API key management using `.env`
- Simple and beginner-friendly Python code
- Generates AI responses based on user prompts

## 🛠️ Technologies Used

- Python
- Google Gemini API
- Google GenAI Python SDK
- python-dotenv

## 📂 Project Structure

```text
dronzer_ai_agent/
├── basic.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

> **Note:** The `.env` file is used locally to store the Gemini API key and should never be uploaded to GitHub.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/mr-prajapati/dronzer_ai_agent.git
```

### 2. Open the project folder

```bash
cd dronzer_ai_agent
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

## 🔑 API Key Setup

Create a `.env` file in the project folder.

Add your Gemini API key in this format:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

**Never share or upload your API key publicly.**

## ▶️ How to Run

Run the following command:

```bash
python basic.py
```

The program will ask:

```text
Enter your Prompt :
```

Enter your question or message and the chatbot will generate an AI response.

## 💡 Example

```text
Enter your Prompt : Hello

The Response is
----------------
Hello! How can I help you today?
----------------
```

## 🔒 Security

The Gemini API key is stored in the `.env` file and excluded from Git using `.gitignore`.

Do not upload the `.env` file or expose your API key in the source code.

## 👨‍💻 Author

**Dheeraj Kumar**

## 📄 License

This project is created for learning and educational purposes.