from . import *

from modules.InsertMechanism.InsertCompany import ICompany

#//=======================<Company Functions>=======================//

#The function that will render on entering the url
def CompForm():

	try:
	
		#render html
		return render_template("Forms/CompanyForm.html");
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
CompB.add_url_rule("/Forms/CompanyForm","CompForm",CompForm);

#Set the company values in the database
def Company():
	
	try:
	
		ICompany();
		
		return redirect(url_for("compb.CompForm"),code=303);
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
CompB.add_url_rule("/Forms/CompanyForm","Company",Company,methods=["POST"]);