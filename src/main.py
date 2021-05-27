from gtts import gTTS
from google.cloud import texttospeech
import html
import os
import csv
import re
import random
import sys
from datetime import datetime
import math

from phrases import *

# colouring printouts
class colours:
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	CYAN = '\033[96m'
	GREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	REGULAR = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


namesList = []
# assigns just names to `namesList`
def importCSV(path,stop = 4):
	datafile = open(path,'r',encoding='utf-8-sig')
	reader = csv.reader(datafile)
	rowNum = 0
	for row in reader:
		rowNum+=1
		if rowNum>stop:
			break
		namesList.append(row[0])

def ssml_to_audio(ssml_text, outfile):
	# Instantiates a client
	client = texttospeech.TextToSpeechClient()

	# Sets the text input to be synthesized
	synthesis_input = texttospeech.SynthesisInput(ssml=ssml_text)

	# Builds the voice request, selects the language code ("en-US") and
	# the SSML voice gender ("MALE")
	voice = texttospeech.VoiceSelectionParams(
		language_code="en-gb",
		name='en-GB-Wavenet-D',
		ssml_gender=texttospeech.SsmlVoiceGender.MALE,
		
	)

	# Selects the type of audio file to return
	audio_config = texttospeech.AudioConfig(
		audio_encoding=texttospeech.AudioEncoding.MP3
	)

	# Performs the text-to-speech request on the text input with the selected
	# voice parameters and audio file type
	response = client.synthesize_speech(
		input=synthesis_input, voice=voice, audio_config=audio_config
	)

	# Writes the synthetic audio to the output file.
	with open(outfile, "wb") as out:
		out.write(response.audio_content)
		print(f"{colours.WARNING}Audio content written to file {colours.UNDERLINE}{colours.BOLD}" + outfile +f"{colours.REGULAR}")


def text_to_ssml(inputfile):

	raw_lines = inputfile

	# For example, '<' --> '&lt;' and '&' --> '&amp;'

	escaped_lines = html.escape(raw_lines)

	repl_text = replace_all(escaped_lines)

	ssml = "<speak>{}</speak>".format(repl_text)
		# replace_all(escaped_lines))
		# escaped_lines.replace("\n", '\n<break time="2s"/>'),

	return ssml

def replace_all(text):
	for key, val in replacementDict.items():
		text = text.replace(key,val)
	return text

# whenever a special character comes up, replace it with its corresponding
replacementDict = { 
			"\n":'\n<break time="2s"/>',
			"|":'\n<break time=".5s"/>',
			"[.5]":'\n<break time="0.5s"/>',
			'[1]':'<break time="1s"/>',
			"[1.5]":'\n<break time="1.5s"/>',
			"[2]":'\n<break time="2s"/>',
			# emphasis:
			"[EMPH]":'\n<emphasis level="strong">',
			"[/EMPH]":'\n</emphasis>'

			}

def pickRandName():
	namesLength = len(namesList)
	randNum = random.randint(0,namesLength-1)
	return namesList[randNum]

# can still be called with amountNames=0, without fail
def fillPhrase(amountNames,phrase):
	names=[]
	for i in range(0,amountNames):
		rndName = pickRandName()
		while (rndName in names):
			rndName = pickRandName()
		names.append(rndName)
	tupNames=tuple(names)
	phrase = phrase.format(*tupNames)
	return phrase

# these go between the phrases to make it sound a bit more natural
repeaters = ["i repeat,",
							"again,",
							"once again,",
							"to be clear,",
							"once more,"]

# returns randomly generated + repeated phrase, with newline character appended
def createPhrase():
	amount, greeting, phrase = getRandomPhrase()
	phrase = fillPhrase(amount,phrase)
	phraseRepeated = phrase + "[1] " + repeaters[random.randint(0,len(repeaters)-1)] + " " + phrase
	fullPhrase = "[EMPH]{}[/EMPH]|".format(greeting) + phraseRepeated
	return fullPhrase + "\n"

# returns randomly generated name, with newline character appended
def createName():
	rndName = pickRandName()
	return rndName + "\n"

# master function, returns string of entire thing. this *definitely* isnt a good way to go about this
# function which goes adds one of the following:
# - name
# - phrase
# - random read
# each loop iteration
# note: a `hit` is a phrase, instead of a name
def generate(phraseFrequency=5,amountGenerated=10):
	hitNum = phraseFrequency//2 # `hitNum` describes 
	speech = ""
	lastHit=10
	curAmount = 0
	for i in range(0,amountGenerated):
		addition = ""
		rndNum = random.randint(1,phraseFrequency)
		if (rndNum==hitNum):
			if lastHit<2: #if last hit was recent, dont hit
				addition=createName()
				lastHit+=1
			else:
				rangeLength=10
				randomReadHit=math.floor(rangeLength*.75)
				if (random.randint(1,rangeLength)>randomReadHit):
					addition=randomReads[random.randint(0,len(randomReads)-1)] + "\n"
				else:
					addition=createPhrase()
				lastHit=0
		else:
			addition=createName()
			lastHit+=1
		speech+=addition
		curAmount+=1
	return speech


def callGenerate(path,createAudio,iter,freq,outputnumber=0,outputPath=''):
	importCSV(path,stop=400)
	masterStr = ""
	masterStr = generate(freq,iter)
	print(masterStr)
	if (not createAudio):
		pass
	else:
		ssml = text_to_ssml(masterStr)
		ssml_to_audio(ssml, "{0}voices{1}.mp3".format(outputPath,outputnumber))

# takes:
# - bool: whether to create audio
# - int: how many iterations of speech
# - int: freq of phrases
# example:
#  python3 textToSpeech.py true 10 5
if __name__ == '__main__':
	inputList = sys.argv[1:]

	if (len(inputList)!=3):
		print("please yarn 3 inputs [boolean] [int] [int]")
		exit()	


	createAudio = False
	if (inputList[0]=='True' or inputList[0]=='true'):
		createAudio = True
	iterations = int(str(inputList[1]))
	frequency = int(str(inputList[2]))

	print("~~~~~~~~~~~~~~~~~~~")
	print(f"create audio? {colours.GREEN}"+ str(createAudio)+f"{colours.REGULAR}")
	print(f"# iterations? {colours.GREEN}"+ str(iterations)+f"{colours.REGULAR}")
	print(f"freq of phrases? {colours.GREEN}"+ str(frequency)+f"{colours.REGULAR}")
	print("~~~~~~~~~~~~~~~~~~~")

	# ssml = text_to_ssml("You are now crossing the final muntier,| you may remove your helmet.")
	# ssml_to_audio(ssml, "Vestibule2.mp3")
	# exit()

	guest_list_path = "guest_list.csv"
	f = None
	try:
		f = open(guest_list_path, encoding='utf-8')
	except FileNotFoundError as fnfe:
		print("File `{}` not found".format(guest_list_path))
		exit(10)
	finally:
		if f:
			f.close()

	# # # # # # # # #
	numPerOutput=50
	loopAmount = (iterations//numPerOutput) # only used when iterations exceeds 'numPerOutput'
	remaining = (iterations%numPerOutput)

	voicesDir = '../output/'

	if (iterations>numPerOutput):

		for i in range(0,loopAmount):
			print(str(i+1)+" loop")
			callGenerate(guest_list_path,createAudio,numPerOutput,frequency,i, outputPath=voicesDir)
		if (remaining > 0):
			print("")
			print("~~~~~~~~{} calls remaining:".format(remaining))
			callGenerate(guest_list_path,createAudio,remaining,frequency,'-LAST', outputPath=voicesDir)
			
	else: # just call as normal, no output number required.
		callGenerate(guest_list_path,createAudio,iterations,frequency, outputPath=voicesDir)

	print(f"{colours.GREEN}{colours.BOLD}~~~TERMINATION SUCESSFUL~~~{colours.REGULAR}")