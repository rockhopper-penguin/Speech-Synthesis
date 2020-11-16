import sys
import requests

class SpeechSynthesis():

	def __init__(self, key, text, voice, emotion, emotion_level, pitch, speed, volume):
		self.key = key
		self.text = text
		self.voice = voice
		self.emotion = emotion
		self.emotion_level = emotion_level
		self.pitch = pitch
		self.speed = speed
		self.volume = volume

	def getVoice(self):
		adress = 'https://api.voicetext.jp/v1/tts'
		Parameters = {
			'text': self.text,
			'speaker': self.voice,
			'emotion': self.emotion,
			'emotion_level': self.emotion_level,
			'pitch': self.pitch,
			'speed': self.speed,
			'volume': self.volume
		}
		try:
			send = requests.post(adress, params = Parameters, auth = (self.key,''))
			result = open("static/result/result.wav", 'wb')
		except:
			print("Error!")
		result.write(send.content)
		result.close()