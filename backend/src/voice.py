from gtts import gTTS
from io import BytesIO


def generate_voice(text):
    audio = gTTS(text,lang="pt-br")
    audio_byte = BytesIO()
    audio.write_to_fp(audio_byte)
    audio_byte.seek(0)
    return audio_byte