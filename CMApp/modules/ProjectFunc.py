from . import *

from modules.GetMechanism.GetProjects import GetProjectList
from modules.GetMechanism.GetProjects import GetProjectListByID
from modules.GetMechanism.GetProjects import GetProjectContractList
from modules.GetMechanism.GetContract import GetContractListByProject
from modules.GetMechanism.GetTask import GetProjectTask
from modules.GetMechanism.GetTask import GetProjectTaskDep
from modules.GetMechanism.GetContract import GetContractList
from modules.GetMechanism.GetCompany import GetCompanyList
from modules.GetMechanism.GetDepartment import GetDepartmentList

#//=======================<Project Functions>=======================//

def ProjOverv():

	ProjectRows = GetProjectContractList();

	#render html
	return render_template("DisplayData/ProjectOverview.html",ProjRows = ProjectRows);
ProjB.add_url_rule("/DisplayData/ProjectOverview","ProjOverv",ProjOverv);	

def ProjTaskDisplay():
	if request.method == "POST":
	
		if "ProjID" in session:
			
			TaskRows = GetProjectTask(session["ProjID"]);
		
			TaskDepRows = GetProjectTaskDep(session["ProjID"]);
		
			#render html
			return render_template("DisplayData/TaskData.html",taskrows = TaskRows,taskdeprows = TaskDepRows );
		
	return redirect(url_for("projb.ProjOverv"),code=302);
ProjB.add_url_rule("/DisplayData/TaskData","ProjTaskDisplay",ProjTaskDisplay,methods=["POST"]);

def ProjEdit():
	if request.method == "POST":
	
		if "ProjID" in session:

			ProjectRows = GetProjectListByID(session['ProjID']);
			ContractRows = GetContractList();
			CompanyRows = GetCompanyList();
			DepartmentRows = GetDepartmentList();
			
			#render html
			return render_template("Forms/ProjectEditForm.html", ContrRows = ContractRows, ProjRows = ProjectRows, CompRows = CompanyRows, DepRows = DepartmentRows);
	return redirect(url_for("projb.ProjOverv"), code=302);
ProjB.add_url_rule("/Forms/ProjectEditForm","ProjEdit",ProjEdit,methods=["POST"]);

def ProjDel():

	if request.method == "POST":
	
		if "ProjID" in session:
		
			SetProjectIsActiv(str(session['ProjID']),"0");
	
	return redirect(url_for("projb.ProjOverv"),code=302);	
ProjB.add_url_rule("/ProjectDelete","ProjDel",ProjDel,methods=["POST"]);


ProjB.secret_key="70012";
def ProjOvervLoad():

	if request.method=="POST":
		
		if "ProjID" in request.form:
		
			session['ProjID'] = request.form['ProjID'];
			
			if "ProjLoad" in request.form:#if submit was ProjLoad then start project load methods
		
				return redirect(url_for("projb.ProjTaskDisplay"), code=307);
			
			elif "ProjEdit" in request.form:#if submit was ProjEdit the start project edit methods
		
				return redirect(url_for("projb.ProjEdit"), code=307);
			
			elif "ProjDel" in request.form:#if submit was ProjDel then Set del to query flag
			
				return redirect(url_for("projb.ProjDel"), code=307);	
		
			else:
				return "There was an unknown error, please try again"
					
		else:
			return "There was an unknown error, Please try again";
ProjB.add_url_rule("/DisplayData/ProjectOverview","ProjOvervLoad",ProjOvervLoad,methods=["POST"]);
#//===============================================================//