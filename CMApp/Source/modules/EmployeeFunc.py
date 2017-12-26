from . import *

from modules.GetMechanism.GetEmpForm import GetFormDepartment
from modules.InsertMechanism.InsertEmployee import IEmployee

#//=======================<Employee Functions>=======================//

#The function that will render on entering the url
def EmpForm():
	
	try:
	
		TableRows = GetFormDepartment(1);

		#render html with tuple data
		return render_template("Forms/EmpForm.html",rows = TableRows);
		
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
EmpB.add_url_rule("/Forms/EmployeeForm","EmpForm",EmpForm);

#Set employee values in the database
def Employee():
	
	try:
	
		IEmployee();
		
		#render html
		return redirect(url_for("empb.EmpForm"),code=303);
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
EmpB.add_url_rule("/Forms/EmployeeForm","Employee",Employee,methods = ["POST"]);