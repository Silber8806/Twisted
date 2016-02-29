import sys

from twisted.python.log import FileLogObserver

class ColorizedLogObserver(FileLogObserver):
	def emit(self,eventDict):
		self.write("\033[0m")

		if eventDict["isError"]:
			self.write("\033[91m")

	FileLogObserver.emit(self,eventDict)

def logger():
	return ColorizedLogObserver(sys.stdout).emit