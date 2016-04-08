import sys
from PyQt4 import QtCore, QtGui, uic
import os
#from PyQt4.QtGui import *
#audio
from array import array
from struct import pack
from sys import byteorder
from scipy import signal
import matplotlib.pyplot as plt
import copy
import numpy as np
#import pyaudio
#import wave
#Funciones Audio
import pyaudio
import wave
from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write
#creacion y escritura de archivo
from sys import argv

def plotSpectru(y,Fs):
    n = len(y) # lungime semnal
    print "Esto es n:", n
    k = arange(n)
    print "Esto es k:", k
    T = n/Fs
    print "Esto es T:", T
    frq = k/T # two sides frequency range
    print "Esto es frq:", frq
    #creacion de archivo
    archivo = open("entradas.txt",'w')
    archivo.write(frq)
    archivo.close()

    frq = frq[range(n/2)] # one side frequency range
    print "Esto es frq de nuevo:", frq
    Y = fft(y)/n # fft computing and normalization
    print "Esto es Y:", Y

    Y = Y[range(n/2)]
    print "Esto es Y de nuevo:", Y

    plot(frq,abs(Y),'r') # plotting the spectrum
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')


def Procesamiento_Audio():
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 4
    WAVE_OUTPUT_FILENAME = "file.wav"

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
    print "recording..."
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print "finished recording"


    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()


    Fs = 44100;  # sampling rate

    rate,data=read('file.wav')
    y=data[:,1]

    lungime=len(y)
    timp=len(y)/44100.
    t=linspace(0,timp,len(y))

    subplot(2,1,1)
    plot(t,y)
    xlabel('Time')
    ylabel('Amplitude')
    subplot(2,1,2)
    plotSpectru(y,Fs)
    show()


def llamada():
    print ("Por favor diga una palabra en el microfono")
    print("Hecho - Audio guardo como demo.wav")
    Procesamiento_Audio()

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("GUI_IA.ui")[0]
form_class2 = uic.loadUiType("GUI2_IA.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
 def __init__(self, parent=None):
  QtGui.QMainWindow.__init__(self, parent)
  self.setupUi(self)
  self.pushButton.clicked.connect(self.pushButton_clicked)
  self.window2 = None
 # Evento del boton btn_CtoF
 def pushButton_clicked(self):
  #MyWindow2 = MyWindowClass2(None)
  #MyWindow2.show()
  llamada()
  if self.window2 is None:
        self.window2 = MyWindowClass2(self)
        self.window2.show()



class MyWindowClass2(QtGui.QMainWindow, form_class2):
 def __init__(self, parent=None):
  QtGui.QMainWindow.__init__(self, parent)
  self.setupUi(self)
  self.pushButton.clicked.connect(self.botonwriter)
  self.pushButton_2.clicked.connect(self.botonmozila)
  self.pushButton_3.clicked.connect(self.botonterminal)
  self.pushButton_4.clicked.connect(self.botonsolitario)
  self.pushButton_5.clicked.connect(self.botonapagar)
 # Evento del boton btn_CtoF
 def botonwriter(self):
  os.system('start WINWORD.EXE')
  #os.system('sudo shutdown -h now')
 def botonmozila(self):
  os.system('start FIREFOX')

 def botonterminal(self):
  os.system('start CMD')

 def botonsolitario(self):
  os.system('start MSPAINT.EXE')

 def botonapagar(self):
  os.system('start SHUTDOWN /S')


app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
