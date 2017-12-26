from . import *

class FileHandleBase:
	
	HandleFile = None;
	
	def __init__(self, FileName, FileMode):
		self.HandleFile = open(FileName,FileMode);
		
	def __del__(self):
		self.HandleFile = None;
		
	def CloseStream(self):
		self.HandleFile.close();
	
	def ParseData(self, Data):
		if self.HandleFile.mode != "r" or self.HandleFile.mode != "rb":
			self.HandleFile.write(Data);
		else:
			print("File mode is write only");
	
	def ReadData(self, ByteSize):
		FileData = "";
	
		if self.HandleFile.mode != "w" or self.HandleFile.mode != "wb":
			if ByteSize == 0:
				self.HandleFile.read();
			else:
				self.HandleFile.read(ByteSize);
				
			return FileData;
		else:
			print("File mode is read only");