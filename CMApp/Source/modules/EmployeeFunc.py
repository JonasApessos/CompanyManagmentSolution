from . import *

from modules.GetMechanism.GetEmpForm import GetFormDepartment
from modules.InsertMechanism.InsertEmployee import IEmployee

#//=======================<Employee Functions>=======================//

def EmpForm():
	
	TableRows = GetFormDepartment();

	#render html with tuple data
	return render_template("Forms/EmpForm.html",rows = TableRows);
EmpB.add_url_rule("/Forms/EmployeeForm","EmpForm",EmpForm);

def Employee():
	
	IEmployee();
		
	#render html
	return redirect(url_for("empb.EmpForm"),code=302);
EmpB.add_url_rule("/Forms/EmployeeForm","Employee",Employee,methods = ["POST"]);