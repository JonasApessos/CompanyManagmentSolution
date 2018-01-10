from . import *

from modules.GetMechanism.GetProjects import GetProjectList, GetProjectListByID, GetProjectContractList, GetProjectContractListByID
from modules.GetMechanism.GetTask import GetProjectTask, GetProjectTaskDep
from modules.GetMechanism.GetContract import GetContractList, GetContractListByProjectID
from modules.GetMechanism.GetCompany import GetCompanyList
from modules.GetMechanism.GetDepartment import GetDepartmentList

from modules.UpdateMechanism.SetProject import SetProject, SetProjectIsActiv

from modules.InsertMechanism.InsertProject import IProj

from modules.TableDiagramSystem import TableDiagram

#//=======================<Project Functions>=======================//

#Get projects list and display them
def ProjOverv():
	
	try:
	
		#Get available projects list
		ProjectRows = GetProjectContractList(1);

		#render html
		return render_template("DisplayData/ProjectOverview.html",ProjRows = ProjectRows);
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/DisplayData/ProjectOverview","ProjOverv",ProjOverv);	

#Get Tasks list from selected project and display them
def ProjTaskDisplay():

	try:

		if request.method == "POST":
		
			if "ProjID" in session:
				
				Table = TableDiagram();
				
				#Get the project Tasks to display 
				TaskRows = GetProjectTask(1,session["ProjID"]);
				TaskDepRows = GetProjectTaskDep(1,session["ProjID"]);
				
				#TaskList = GetProjectTask(0,session["ProjID"]);
				#TaskDepList = GetProjectTaskDep(0,session["ProjID"]);
				
				TableList = Table.CreateTableDiagram(GetProjectTask(0,session["ProjID"]), GetProjectTaskDep(0,session["ProjID"]));
			
				#render html
				return render_template("DisplayData/TaskData.html",TaskRows = TaskRows,TaskDepRows = TaskDepRows );

		return redirect(url_for("projb.ProjOverv"), code=303);
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/DisplayData/TaskData","ProjTaskDisplay",ProjTaskDisplay,methods=["POST"]);

#The function for the create new task form
def ProjTaskForm():

	try:	
	
		if "ProjID" in session:
		
			TaskProjectRows = GetProjectListByID(1,session['ProjID']);
			TaskProjectContractRows = GetProjectContractListByID(1,session['ProjID']);
			TaskRows = GetProjectTask(1,session['ProjID']); 
			
			#render html with tuple data
			return render_template("Forms/TaskForm.html",TaskProjRows = TaskProjectRows, TaskRows = TaskRows, TaskProjContrRows = TaskProjectContractRows);
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/Forms/TaskForm","ProjTaskForm",ProjTaskForm);

#update the selected projects values
def ProjUpdate():

	try:
	
		if request.method == "POST":
			
			#Get data from the form
			ContrID = request.form['ContrID'];
			CompID = request.form['CompID'];
			DepID = request.form['DepID'];
			
			#Set the new values of the current selected project in the database
			SetProject(session['ProjID'], CompID, ContrID, DepID);
			
			#when finished return to the edit form of the selected project
			return redirect(url_for("projb.ProjEdit"), code=307);
			
		return redirect(url_for("projb.ProjOverv"), code=303);#if non of the above is true, then redirect to project list
	
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/DisplayData/ProjectEdit","ProjUpdate",ProjUpdate,methods=["POST"]);

#display the projects edit form  with it's necessary data
def ProjEdit():

	try:

		if request.method == "POST":
		
			if "ProjID" in session:

				#Get all the listtype that the current project is associated to
				ProjectRows = GetProjectListByID(1,session['ProjID']);
				ContractRows = GetContractList(1);
				CompanyRows = GetCompanyList(1);
				DepartmentRows = GetDepartmentList(1);
				
				#render html
				return render_template("Forms/ProjectEditForm.html", ContrRows = ContractRows, ProjRows = ProjectRows, CompRows = CompanyRows, DepRows = DepartmentRows);
		return redirect(url_for("projb.ProjOverv"), code=303);#if non of the above is true, then redirect to project list
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/Forms/ProjectEditForm","ProjEdit",ProjEdit,methods=["POST"]);

#Update the active value of the current selected project to FALSE 
def ProjDel():
	
	try:
	
		if request.method == "POST":
		
			if "ProjID" in session:
				#Set the active value to 0 to deactivate it
				SetProjectIsActiv(session['ProjID'],0);
		
		return redirect(url_for("projb.ProjOverv"),code=303);#if non of the above is true, then redirect to project list
		
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/DeleteProject","ProjDel",ProjDel,methods=["POST"]);

def ProjForm():

	try:
	
		ContractRows = GetContractList(1);
		CompanyRows = GetCompanyList(1);
		DepartmentRows = GetDepartmentList(1);
	
		return render_template("forms/ProjectForm.html", ContrRows = ContractRows, CompRows = CompanyRows, DepRows = DepartmentRows);
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/AddProject","ProjForm",ProjForm);

def AddProj():

	try:
	
		if request.method == "POST":
	
			ContrID = request.form['ContrID'];
			CompID = request.form['CompID'];
			DepID = request.form['DepID'];
			
			IProj(ContrID,CompID,DepID);
	
			return redirect(url_for('projb.ProjForm'), code=303);
			
		return redirect(url_for('projb.ProjOverv'), code=303);
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/AddNewProject","AddProj",AddProj,methods=["POST"]);

#The decision making when selecting an option in project list
def ProjOvervLoad():

	try:

		if request.method=="POST":
			
			if "ProjID" in request.form:
			
				session['ProjID'] = request.form['ProjID'];#set the current loaded project to session for the rest of the functions to know
				
				if "ProjLoad" in request.form:#if submit was ProjLoad then start project load methods
			
					return redirect(url_for("projb.ProjTaskDisplay"), code=307);
				
				elif "ProjEdit" in request.form:#if submit was ProjEdit then start project edit methods
			
					return redirect(url_for("projb.ProjEdit"), code=307);
				
				elif "ProjDel" in request.form:#if submit was ProjDel then start project delete methods
				
					return redirect(url_for("projb.ProjDel"), code=307);	
						
		return redirect(url_for("projb.ProjOverv"), code=303);#if non of the above is true, then redirect to project list
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/DisplayData/ProjectOverview","ProjOvervLoad",ProjOvervLoad,methods=["POST"]);
#//===============================================================//