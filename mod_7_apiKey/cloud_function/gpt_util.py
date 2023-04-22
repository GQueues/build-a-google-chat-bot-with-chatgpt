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


def create_image_with_prompt(image_prompt):
    """Generates an image using DALL-E.
    
    Returns: url of new image.

    Raises: openai.error.OpenAIError

    API Details here: https://platform.openai.com/docs/api-reference/images
    """

    response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="1024x1024"
    )

    image_url = response['data'][0]['url']
    return image_url