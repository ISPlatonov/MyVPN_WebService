import openai
openai.api_key = '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'


def send_text(message):
    try:
        response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=message,
          temperature=0.9,
          max_tokens=4000,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0.6,
        )
        return response['choices'][0]['text']

    except:
        return 'Sorry, I don\'t know the answer.'
