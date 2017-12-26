from __init__ import *


try:
	#//=======================<Index Functions>=======================//
	def Index():
	
		try:
	
			#render html
			return render_template("index.html");
			
		except Exception as Error:
		
			Handle = ErrorHandle("ErrorLog/Log.txt","a");
	
			Handle.SaveErrorToLogNoComment(Error);
	
			Handle.CloseStream();
			
			return render_template("ErrorIndex.html");			
	app.add_url_rule("/","Index",Index);
	#//===============================================================//	

	#//=======================<Main Functions>=======================//
	if __name__ == '__main__':

		app.run(debug = DEBUG, port = PORT);
	#//===============================================================//
	
except RuntimeError as Error:

	Handle = ErrorHandle("ErrorLog/Log.txt","a");
	
	Handle.SaveErrorToLogNoComment(Error);
	
	Handle.CloseStream();