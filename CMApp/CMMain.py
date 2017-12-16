from CMApp import *

#PYTHONDONTWRITEBYTECODE=1;
#PYTHONMALLOCSTATS=1;
#from flask import Flask, request, render_template, redirect, url_for	
#app = Flask(__name__);


#//=======================<Index Functions>=======================//
def index():
	#render html
	return render_template("index.html");
app.add_url_rule("/","index",index);
#//===============================================================//

	
	
#//=======================<Employee Functions>=======================//
def EmpForm():
	
	TableRows = GetFormDepartment();

	#render html with tuple data
	return render_template("Forms/EmpForm.html",rows = TableRows);
app.add_url_rule("/Forms/EmployeeForm","EmpForm",EmpForm);

def Employee():
	
	IEmployee();
		
	#render html
	return redirect(url_for("EmpForm"));
app.add_url_rule("/Forms/EmployeeForm","Employee",Employee,methods = ["POST"]);
#//===============================================================//

	
	
#//=======================<Task Functions>=======================//
def TaskForm():

	TableRows = GetFormAssignProject();
	
	#render html with tuple data
	return render_template("Forms/TaskForm.html",rows = TableRows);
app.add_url_rule("/Forms/TaskForm","TaskForm",TaskForm);

def Task():
	
	ITask();
		
	#render html
	return redirect(url_for("TaskForm"));
app.add_url_rule("/Forms/TaskForm","Task",Task,methods=["POST"]);
#//===============================================================//
	
	
	
#//=======================<Company Functions>=======================//
def CompForm():

	return render_template("Forms/CompanyForm.html");
app.add_url_rule("/Forms/CompanyForm","CompForm",CompForm);

def Company():
	
	ICompany();
		
	#render html
	return redirect(url_for("CompForm"));
app.add_url_rule("/Forms/CompanyForm","Company",Company,methods=["POST"]);
#//===============================================================//
		
		
	
#//=======================<Contract Functions>=======================//
def ContrForm():
	#render html
	return render_template("Forms/ContractForm.html");
app.add_url_rule("/Forms/ContractForm","ContrForm",ContrForm);
	
def Contract():

	IContract();

	return redirect(url_for("ContractForm"));
app.add_url_rule("/Forms/ContractForm","Contract",Contract,methods=["POST"]);
#//===============================================================//
		

#//=======================<Project Functions>=======================//
def ProjOverv():

	TableRows = GetProjectList();

	#render html
	return render_template("DisplayData/ProjectOverview.html",rows = TableRows);
app.add_url_rule("/DisplayData/ProjectOverview","ProjOverv",ProjOverv);
	
def ProjOvervLoad():
	if request.method=="POST":
		ID = str(request.form['ProjID']);
		print("ID: " + ID);
		TableRows = GetProjectTaskData(ID);
	
	return render_template("DisplayData/TaskData.html",rows = TableRows);
app.add_url_rule("/DisplayData/TaskData","ProjOvervLoad",ProjOvervLoad,methods=["POST"]);
#//===============================================================//
		

#//=======================<Main Functions>=======================//
if __name__ == '__main__':

	app.run(debug = True,port=80);
#//===============================================================//
