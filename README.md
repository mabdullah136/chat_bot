# ChatBot
ChatBot is a Django-based web application that enables users to interact with an AI chatbot powered by the OpenAI API. Users can submit prompts, receive AI-generated responses, and view up to 5 previous chat interactions stored in the session. The chatbot is configurable, allowing you to specify the OpenAI model and max tokens, with a default model of o3-mini.
Features

Submit prompts and receive AI-generated responses via the OpenAI API.
Stores up to 5 previous prompt-response pairs in the session for context.
Clean, responsive UI styled with Tailwind CSS.
Configurable OpenAI model and max tokens.
Secure API key management using environment variables.

## Prerequisites

Python 3.8 or higher
Git
An OpenAI API key (sign up at OpenAI)

## Installation

### Clone the Repository:

-  git clone <repository-url>
- cd chat_bot
- python3 -m venv env
- source env/bin/activate  
- pip install -r requirements.txt
- python3 manage.py migrate
- python3 manage.py runserver

Create a .env file in the project root and add your OpenAI API key:
- Open_api_key=your_openai_api_key_here

## Access the Chatbot:
Open your browser and navigate to http://127.0.0.1:8000/. You’ll see a screen where you can enter prompts, view responses, and see up to 5 previous chat interactions.

## Usage

Enter a prompt in the textarea and click "Submit".
The AI response will appear below the form.
Up to 5 previous prompt-response pairs are displayed in the "Previous Chats" section.
Chat history is stored in the session and persists until the session expires or is cleared.

## Security Notes

Keep your OpenAI API key secure in the .env file, which is ignored by .gitignore.
Consider adding rate limiting or input validation for production use.

## Troubleshooting

API Key Error: Ensure Open_api_key is correctly set in .env.
Migration Issues: Run python3 manage.py makemigrations if migrations fail.
Model Not Found: Verify the model name in bot/views.py is valid for your OpenAI account.

## Contributing
Feel free to fork the repository, make improvements, and submit pull requests.
License
This project is open-source and available under the MIT License.
