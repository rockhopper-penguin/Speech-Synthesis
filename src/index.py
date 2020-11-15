from flask import Flask, render_template, request
import sys
import SpeechSynthesis

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/result', methods=['POST'])
def post():
	key = request.form['apiKey']
	text = request.form['setText']
	voice = request.form['setVoice']
	emotion = request.form['setEmotion']
	emotion_level = request.form['setEmotionLevel']
	pitch = request.form['setPitch']
	speed = request.form['setSpeed']
	volume = request.form['setVolume']
	speechSynthesis = SpeechSynthesis.SpeechSynthesis(key, text, voice, emotion, emotion_level, pitch, speed, volume)
	speechSynthesis.getVoice()
	return render_template('result.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)