from . import *

from modules.InsertMechanism.InsertContract import IContract

#//=======================<Contract Functions>=======================//

#The function that will render on entering the url
def ContrForm():

	try:

		#render html
		return render_template("Forms/ContractForm.html");
	
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
ContrB.add_url_rule("/Forms/ContractForm","ContrForm",ContrForm);

#Set the contract values in the database
def Contract():

	try:

		IContract();
	
		return redirect(url_for("contrb.ContrForm"), code=303);
	
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
ContrB.add_url_rule("/Forms/ContractForm","Contract",Contract,methods=["POST"]);