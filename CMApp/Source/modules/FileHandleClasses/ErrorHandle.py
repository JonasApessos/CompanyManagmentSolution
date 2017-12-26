from . import *

from .FileHandle import FileHandleBase
from datetime import *

class ErrorHandle(FileHandleBase):
	
	def __init__(self, FileName, FileMode):
		super().__init__(FileName, FileMode);
		
		
	def __del__(self):
		super().__del__();
	
	
	def SaveErrorToLogNoComment(self, Data):
		super().ParseData("\n\n//--Error Log: " + str(datetime.now()) + " -> Exception: " + str(Data));
		
	def SaveErrorToLog(self, Data, Text):
		super().ParseData("\n\n//--Error Log: " + str(datetime.now()) + " -> Exception: " + str(Data) + " -- " + str(Text));