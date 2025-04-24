from django.shortcuts import render
from openai import OpenAI
from decouple import config

def chat_view(request):
    # Initialize session for chat history
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    response_text = None
    error = None

    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        if prompt:
            try:
                # Initialize OpenAI client
                client = OpenAI(api_key=config('OPEN_API_KEY'))
                
                # Get previous chats from session (up to 5)
                chat_history = request.session['chat_history']
                
                # Prepare messages with context
                messages = [
                    {'role': 'system', 'content': 'You are a helpful assistant.'}
                ]
                
                # Add previous chats as context
                for chat in chat_history:
                    messages.append({'role': 'user', 'content': chat['prompt']})
                    messages.append({'role': 'assistant', 'content': chat['response']})
                
                # Add current prompt
                messages.append({'role': 'user', 'content': prompt})
                
                # Call OpenAI API
                response = client.chat.completions.create(
                    model='o3-mini',
                    messages=messages,
                    # max_tokens=500,
                )
                response_text = response.choices[0].message.content.strip()
                
                # Update chat history
                chat_history.append({'prompt': prompt, 'response': response_text})
                
                # Keep only the last 5 interactions
                if len(chat_history) > 5:
                    chat_history = chat_history[-5:]
                
                # Save updated history to session
                request.session['chat_history'] = chat_history
                request.session.modified = True
                
            except Exception as e:
                error = f"Error: {str(e)}"

    return render(request, 'bot/chat.html', {
        'response': response_text,
        'error': error,
        'chat_history': request.session['chat_history']
    })