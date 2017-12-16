

def class ErrorHandleBase:
	
	def __init__(self):
		pass;
		
	def __del__(self):
		pass;
	
	
	def SaveErrorToDefaultLog(self):
		if(request.remote_addr)