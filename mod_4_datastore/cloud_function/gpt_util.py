import openai

def get_gpt_response(messages):
    """Processes messages using ChatGPT.
    
    Returns: a response from ChatGPT.

    Raises: openai.error.OpenAIError

    API Details here: https://platform.openai.com/docs/api-reference/chat/create 
    """

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=1.1,
        messages=messages
    )

    gpt_response = completion['choices'][0]['message']['content']

    return gpt_response