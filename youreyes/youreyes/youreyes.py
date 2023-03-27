

import os
import openai
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import replicate

openai.api_key = "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"
os.environ['REPLICATE_API_TOKEN'] = '7b63ad7d84b75864d74799794581e3d441e3b81d'

def chat_gpt(cevir):
    completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
        messages = [
     {'role': 'user', 'content': 'Translate the following English text to Turkish:' + cevir}
        ],
    temperature = 0  
    )

    sonuc = str(completion['choices'][0]['message']['content'])
    print(sonuc.lstrip())

model = replicate.models.get("salesforce/blip")
version = model.versions.get("2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746")
inputs = {
    # Input image
    'image': open("C:\\Users\\mert9\\Desktop\\piton\\demo.jpg", "rb"),

    # Choose a task.
    'task': "image_captioning",

    # Type question for the input image for visual question answering
    # task.
    # 'question': ...,
}

output = version.predict(**inputs)
chat_gpt(str(output))
p = 1
while (p == 1): 
     query = input('Fotoğrafla ilgili soru sormak ister misiniz? Yes/No ') 
     Fl = query[0].lower() 
     if query == '' or not Fl in ['y','n']: 
        print('Lütfen "Yes" veya "No" olarak cevaplayın') 
     
     if Fl == 'y': 
        print("5 saniye içinde sorunuzu sorabilirsiniz")
    
        # Sampling frequency
        freq = 44100
 
        # Recording duration
        duration = 5
 
        # Start recorder with the given values
        # of duration and sample frequency
        recording = sd.rec(int(duration * freq),
                       samplerate=freq, channels=2)
 

        # Record audio for the given number of seconds
        sd.wait()
        print("Soru kaydedildi")
        # This will convert the NumPy array to an audio
        # file with the given sampling frequency
        write("recording0.wav", freq, recording)
 
        # Convert the NumPy array to audio file
        wv.write("recording1.wav", recording, freq, sampwidth=2)



        audio_file = open("recording1.wav", "rb")
        transcript = openai.Audio.translate("whisper-1", audio_file)
        print(str(transcript.text))
        chat_gpt(str(transcript.text))



        inputs = {
            # Input image
            'image': open("C:\\Users\\mert9\\Desktop\\piton\\demo.jpg", "rb"),
            'task': "visual_question_answering",

            # Type question for the input image for visual question answering
             # task.
            'question': str(transcript.text),
                  }

        output = version.predict(**inputs)

        chat_gpt(str(output))

     if Fl == 'n': 
        raise SystemExit
