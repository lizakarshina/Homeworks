import json
import pyaudio
import random

from vosk import Model, KaldiRecognizer

def listening():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (recognizer.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(recognizer.Result())
            if answer['text']:
                yield answer['text']

model = Model('vosk-model-uk-v3')
recognizer = KaldiRecognizer(model, 16000)
words = pyaudio.PyAudio()
stream = words.open(format=pyaudio.paInt16, channels=1,
                    rate=16000, input=True,
                    frames_per_buffer=8192)

stream.start_stream()

facts = ['На нашій шкірі може жити більше живих організмів, ніж людей на всій планеті',
            'Три найбагатші родини у світі мають більше активів, ніж 48 найбідніших країн.',
            'Половина населення Землі (а за деякими підрахунками навіть дві третини) ніколи не бачили снігу.',
            'Найсухіше місце на Землі знаходиться в Антарктиді. Хоч як дивно це звучить, але деякі ділянки антарктичної долини Мак-Мердо не бачили опадів уже 2 мільйона років.',
            'Кубик Рубика – товар, який найбільше продається у світі. На другому місці – iPhone.',]

name = input('Як вас зовут?\n')
age = int(input('Скільки вам років?\n'))


for text in listening():
    print(f"User: {text}")
    if text == 'вийти':
        break
    if text == 'привіт' or text == 'вітаю':
        print('Вітаю, чим можу допомогти?\n')

    if text == 'розкажи цікавий факт':
        print(random.choice(facts))

    if text == 'скільки мені років':
        print(f'Вам {age} років')

    if text == 'як мене звати':
        print(f'Вас звати {name}')

    if text == 'як я можу до вас звертатися':
        print('Ви можете називати мене Цар')