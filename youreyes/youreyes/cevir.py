import openai


openai.api_key = "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"
text= "Hello Guys"
completion = openai.ChatCompletion.create(
  model = 'gpt-3.5-turbo',
  messages = [
    {'role': 'user', 'content': 'Translate the following English text to Turkish:' + text}
  ],
  temperature = 0  
)

sonuc = str(completion['choices'][0]['message']['content'])
print(sonuc.lstrip())