import sys
from PyQt4 import QtCore,QtGui
from Test_two import Ui_MainWindow
import time, wave, pymedia.audio.sound as sound


class Test_Two(QtGui.QMainWindow):
	
	def __init__(self,parent=None):
		
		QtGui.QWidget.__init__(self, parent=None)
		
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
	
		QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.file_dialog)
	
	def file_dialog(self):
		
		f= wave.open( 'phone-off-hook-1.wav', 'rb' )
		sampleRate= f.getframerate()
		channels= f.getnchannels()
		format= sound.AFMT_S16_LE
		snd= sound.Output( sampleRate, channels, format )
		s= f.readframes( 300000 )
		snd.play( s )
		while snd.isPlaying(): time.sleep( 0.05 )
				
		#print ("hello")
		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = Test_Two()
	myapp.show()
	sys.exit(app.exec_())		
		
		
		
		
