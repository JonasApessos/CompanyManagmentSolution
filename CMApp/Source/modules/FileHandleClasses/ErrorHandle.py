from . import *

from .FileHandle import FileHandleBase
from datetime import *

class ErrorHandle(FileHandleBase):

	def __init__(self, FileName, FileMode):
		super().__init__(FileName, FileMode);

	def __del__(self):
		super().__del__();

	def SaveErrorToLogNoComment(self, Data):
		super().ParseData("\n\n//--V" + VERSION +" Error Log: " + str(datetime.now()) + " -> Exception: " + str(Data) + " -- function: "+str(inspect.stack()[1][3])+" - LINE: "+ str(inspect.stack()[1][2]) +" , From file: " + str(inspect.stack()[1][1]));

	def SaveErrorToLog(self, Data, Text):
		super().ParseData("\n\n//--V" + VERSION +" Error Log: " + str(datetime.now()) + " -> Exception: " + str(Data) + " -- function: "+str(inspect.stack()[1][3])+" - LINE: "+ str(inspect.stack()[1][2]) +" , From file: " + str(inspect.stack()[1][1]) + " -- Message: " + str(Text));
