import webbrowser
import wikipedia
import os
import datetime
import pyttsx3
import random
import gtts
from PIL import Image
from time import *
import random as r
from pytube import YouTube
from docx2pdf import convert
from pdf2docx import Converter
edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register("Microsoft edge",None,webbrowser.BackgroundBrowser(edge))
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
User_Neme = input("What's your name sir: ")
def speak(audio):
	engine.say(audio)
	engine.runAndWait()
def wishme():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak(f"Good Morning! Sir, {User_Neme}")
	elif hour>=12 and hour<18:
		speak(f"Good Afternoon! Sir, {User_Neme}")
	else:
		speak(f"Good Evening! Sir, {User_Neme}")
	speak("I am jarvis, Sir. Please tell me how may I help you!")
def Youtube(Userinput):
	if "open youtube" in Userinput:
		try:
			speak("opening youtube, sir!")
			webbrowser.get("Microsoft edge").open_new_tab("youtube.com")
		except Exception as e:
			print("Please download and install Microsoft edge in C drive")
			speak("Please download and install Microsoft edge in C drive")
def Wikipedia(Userinput):
	if "wikipedia" in Userinput:
		print("Serching...")
		speak("Serching...")
		Userinput = Userinput.replace("wikipedia", "")
		res = wikipedia.summary(Userinput, sentences = 2)
		print(res)
		speak(res)
def Song(Userinput):
	if "play songs" in Userinput:
		try:
			songs_dir = "E:\\songs"
			songs = os.listdir(songs_dir)
			speak("playing songs, sir!")
			random.shuffle(songs)
			os.startfile(os.path.join(songs_dir, songs[0]))
		except Exception as e:
			print("Please create a folder in E drive name as songs and put your songs in the folder")
			speak("Please create a folder in E drive name as songs and put your songs in the folder")
def Time(Userinput):
	if "the time" in Userinput:
		strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
		print(f"Sir, the time is {strTime}")
		speak(f"Sir, the time is {strTime}")
def ST(Userinput):
	if "open st" in Userinput:
		stPath = "C:\\Program Files\\Sublime Text\\sublime_text.exe"
		speak("opening sublime text sir")
		os.startfile(stPath)
def BuildYou(Userinput):
	if "build you" in Userinput:
		if "Amanat" in User_Neme:
			speak("I am builded by you, Sir!")
		else:
			speak("I am builded by sir Amanat Ali Panhwer")
def CMD(Userinput):
	if "open cmd" in Userinput:
		cmd_Path = "C:\\Windows\\System32\\cmd.exe"
		speak("opening Command Prompt Sir!")
		os.startfile(cmd_Path)
def hi(Userinput):
	if "Hi" in Userinput:
		speak(f"Hi sir {User_Neme}.")
def CYD(Userinput):
	if "can you do" in Userinput:
		print("If you write 'play youtube, play songs, wikipedia, the time, open st, open cmd, TTS = text to speak, png to ico, ITP = ico to png, TST, YTD = YouTube downloader, SSM, WTP = word to pdf, PTW = pdf to word'")
		speak("If you write 'play youtube, play songs, wikipedia, the time, open st, open cmd, TTS = text to speak, png to ico, ITP = ico to png, TST, YTD = YouTube downloader, SSM, WTP = word to pdf, PTW = pdf to word'")
def TTS(Userinput):
	if "TTS" in Userinput:
		while True:
			text = input("Enter what you want to prononse or q to Quit: ")
			if text != 'q':
				file_name = input("Enter the name and path of the file and plase remamber end of the file name add '.mp3': ")
				sound = gtts.gTTS(text, lang="en")
				sound.save(file_name)
			if text == 'q':
				break
def PTI(Userinput):
	if "png to ico" in Userinput:
		while True:
			pngfile = input("Enter the file path and name and remember that end of the file enter '.png' or q to Quit: ")
			if pngfile != 'q':
				saveIco = input("Enter the file name and path that you want to save the file and remember that end of the file enter '.ico': ")
				logo = Image.open(pngfile)
				logo.save(saveIco,format='ICO')
			elif pngfile == 'q':
				break
def ITP(Userinput):
	if "ico to png" in Userinput:
		while True:
			pngfile = input("Enter the file path and name and remember that end of the file enter '.ico' or q to Quit: ")
			if pngfile != 'q':
				saveIco = input("Enter the file name and path that you want to save the file and remember that end of the file enter '.png': ")
				logo = Image.open(pngfile)
				logo.save(saveIco,format='PNG')
			elif pngfile == 'q':
				break
def Mestak(pergrhaph,userinput):
	error = 0
	for i in range(len(pergrhaph)):
		try:
			if pergrhaph[i] != userinput[i]:
				error = error + 1
		except:
			error = error + 1
	return error
def Speed_time(time_s,time_e,user_input):
	time_d = time_e - time_s
	time_R = round(time_d,2)
	speed = len(user_input) / time_R
	return round(speed)
def TST(Userinput):
	if "TST" in Userinput:
		Test = ['The quick brown fox jumps over the lazy dog.',''' Finance is the soul and blood of any business and no firm can survive without finance.
		It concerns itself with the management of the monetary affairs of the firm and how money can be raised on the best terms available.''','''Proper mental health is essential in every stage of life from childhood and teenage to adulthood.
		Throughout a lifetime, an individual can experience mental health issues at any point.''',''' Today Startups are being widely recognized as important engines for growth and job generation.
		Through innovation and scalable technology, startups can generate impactful solutions, and thereby act as vehicles for socio economic development and transformation.''']
		while True:
			Test1 = r.choice(Test)
			print("***** Typing Speed *****")
			print()
			print(Test1)
			print()
			print()
			time1 = time()
			Te_input = input("Enter or q to Quit: ")
			time2 = time()
			if Te_input == 'q':
				break
			print("Speed : ",Speed_time(time1,time2,Te_input),"wps")
			print("Error : ",Mestak(Test1,Te_input))
def YTD(Userinput):
	if "YTD" in Userinput:
		link = input("URL: ")
		youtube_1 = YouTube(link)
		print(youtube_1.title)
		video = youtube_1.streams.all()
		vid = list(enumerate(video))
		for i in vid:
			print(i)
		print()
		stre = int(input("Enter: "))
		video[stre].download()
		print('Successfully')
def SSM(Userinput):
	if "SSM" in Userinput:
		import Send_Secret_Messages
def WTP(Userinput):
	if "WTP" in Userinput:
		word_path = input("Enter the word file path and name: ")
		pdf_path = input("Enter the output pdf file path and name:")
		convert(word_path, pdf_path)
def PTW(Userinput):
	if "PTW" in Userinput:
		pdf_file = input("Enter the pdf file path and name and remember that end of the file enter '.pdf': ")
		doc_file= input("Enter the word file path and name and remember that end of the file enter '.docx': ")
		c=Converter(pdf_file)
		c.convert(doc_file)
		c.close()
if __name__ == '__main__':
	wishme()
	while True:
		User_input = input(f"How can I acest you Sir {User_Neme}: ")
		Youtube(User_input)
		Wikipedia(User_input)
		Song(User_input)
		Time(User_input)
		TTS(User_input)
		PTI(User_input)
		ITP(User_input)
		TST(User_input)	
		YTD(User_input)
		SSM(User_input)
		ST(User_input)
		BuildYou(User_input)
		CMD(User_input)
		hi(User_input)
		CYD(User_input)
		WTP(User_input)
		PTW(User_input)
		if "quit" in User_input:
			speak("quitting sir...")
			break