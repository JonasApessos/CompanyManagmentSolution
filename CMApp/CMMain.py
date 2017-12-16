from __init__ import *

#//=======================<Index Functions>=======================//
def index():
	#render html
	return render_template("index.html");
app.add_url_rule("/","index",index);
#//===============================================================//

	
	
#//=======================<Employee Functions>=======================//
"""def EmpForm():
	
	TableRows = GetFormDepartment();

	#render html with tuple data
	return render_template("Forms/EmpForm.html",rows = TableRows);
app.add_url_rule("/Forms/EmployeeForm","EmpForm",EmpForm);

def Employee():
	
	IEmployee();
		
	#render html
	return redirect(url_for("EmpForm"),code=302);
app.add_url_rule("/Forms/EmployeeForm","Employee",Employee,methods = ["POST"]);"""
#//===============================================================//

	
	
"""#//=======================<Task Functions>=======================//
def TaskForm():

	TableRows = GetFormAssignProject();
	
	#render html with tuple data
	return render_template("Forms/TaskForm.html",rows = TableRows);
app.add_url_rule("/Forms/TaskForm","TaskForm",TaskForm);

def Task():
	
	ITask();
		
	return redirect(url_for("TaskForm"),code=302);
app.add_url_rule("/Forms/TaskForm","Task",Task,methods=["POST"]);"""

"""def TaskDisplay():
	if request.method == "POST":
	
		if "ProjID" in session:
			
			TaskRows = GetProjectTask(session["ProjID"]);
		
			TaskDepRows = GetProjectTaskDep(session["ProjID"]);
		
			#render html
			return render_template("DisplayData/TaskData.html",taskrows = TaskRows,taskdeprows = TaskDepRows );
		
	return redirect(url_for("ProjOverv"),code=302);
app.add_url_rule("/DisplayData/TaskData","TaskDisplay",TaskDisplay,methods=["POST"]);"""
	
#//===============================================================//
	
	
	
#//=======================<Company Functions>=======================//
"""def CompForm():

	#render html
	return render_template("Forms/CompanyForm.html");
app.add_url_rule("/Forms/CompanyForm","CompForm",CompForm);

def Company():
	
	ICompany();
		
	return redirect(url_for("CompForm"),code=302);
app.add_url_rule("/Forms/CompanyForm","Company",Company,methods=["POST"]);"""
#//===============================================================//
		
		
	
#//=======================<Contract Functions>=======================//
"""def ContrForm():

	#render html
	return render_template("Forms/ContractForm.html");
app.add_url_rule("/Forms/ContractForm","ContrForm",ContrForm);
	
def Contract():

	IContract();

	return redirect(url_for("ContractForm"), code=302);
app.add_url_rule("/Forms/ContractForm","Contract",Contract,methods=["POST"]);"""
#//===============================================================//
		

#//=======================<Project Functions>=======================//
"""def ProjOverv():

	ProjectRows = GetProjectContractList();

	#render html
	return render_template("DisplayData/ProjectOverview.html",ProjRows = ProjectRows);
app.add_url_rule("/DisplayData/ProjectOverview","ProjOverv",ProjOverv);	

def ProjEdit():
	if request.method == "POST":
	
		if "ProjID" in session:

			ProjectRows = GetProjectListByID(session['ProjID']);
			ContractRows = GetContractList();
			CompanyRows = GetCompanyList();
			DepartmentRows = GetDepartmentList();
			
			#render html
			return render_template("Forms/ProjectEditForm.html", ContrRows = ContractRows, ProjRows = ProjectRows, CompRows = CompanyRows, DepRows = DepartmentRows);
	return redirect(url_for("ProjOverv"), code=302);
app.add_url_rule("/Forms/ProjectEditForm","ProjEdit",ProjEdit,methods=["POST"]);

def ProjDel():

	if request.method == "POST":
	
		if "ProjID" in session:
		
			SetProjectIsActiv(str(session['ProjID']),"0");
	
	return redirect(url_for("ProjOverv"),code=302);	
app.add_url_rule("/ProjectDelete","ProjDel",ProjDel,methods=["POST"]);

app.secret_key="70012";
def ProjOvervLoad():

	if request.method=="POST":
		
		if "ProjID" in request.form:
		
			session['ProjID'] = request.form['ProjID'];
			
			if "ProjLoad" in request.form:#if submit was ProjLoad then start project load methods
		
				return redirect(url_for("TaskDisplay"), code=307);
			
			elif "ProjEdit" in request.form:#if submit was ProjEdit the start project edit methods
		
				return redirect(url_for("ProjEdit"), code=307);
			
			elif "ProjDel" in request.form:#if submit was ProjDel then Set del to query flag
			
				return redirect(url_for("ProjDel"), code=307);	
		
			else:
				return "There was an unknown error, please try again"
					
		else:
			return "There was an unknown error, Please try again";
app.add_url_rule("/DisplayData/ProjectOverview","ProjOvervLoad",ProjOvervLoad,methods=["POST"]);"""
#//===============================================================//
		

#//=======================<Main Functions>=======================//
if __name__ == '__main__':

	app.run(debug = DEBUG,port=PORT);
#//===============================================================//
