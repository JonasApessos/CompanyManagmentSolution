from modules import *

#functions for to get project data from the database
from modules.GetMechanism.GetProjects import GetProjectList, GetProjectListByID, GetProjectContractList, GetProjectContractListByID

#functions for to get task data from the database
from modules.GetMechanism.GetTask import GetProjectTask, GetProjectTaskDep

#functions for to get contract data from the database
from modules.GetMechanism.GetContract import GetContractList, GetContractListByProjectID

#functions for to get company data from the database
from modules.GetMechanism.GetCompany import GetCompanyList

#functions for to get department data from the database
from modules.GetMechanism.GetDepartment import GetDepartmentList

#functions for to set selected project data to the database
from modules.UpdateMechanism.SetProject import SetProject, SetProjectIsActiv

#functions for to insert project data to the database
from modules.InsertMechanism.InsertProject import IProj

#the diagram system
from modules.TableDiagramSystem import TableDiagram

#//=======================<Project Functions>=======================//

#Get projects list and display them
def ProjOverv():

	try:
		if "ProjID" in session:
			session.pop("ProjID", None);
		#Get available projects list
		ProjectRows = GetProjectContractList(1);

		#render html
		return render_template("DisplayData/ProjectOverview.html",ProjRows = ProjectRows);

	except Exception as Error:#on exception register error to file

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/DisplayData/ProjectOverview","ProjOverv",ProjOverv);

#Get Tasks list from selected project and display them
def ProjTaskDisplay():

	try:
		if "ProjID" in session:#if there is no session for this variable, then there may have been an penetration attempt or error

			#Table = TableDiagram();

			#Get the project Tasks to display
			TaskRows = GetProjectTask(session["ProjID"],1);
			TaskDepRows = GetProjectTaskDep(session["ProjID"],1);

			#TaskDiagram = Table.CreateTableDiagram(GetProjectTask(session['ProjID'],0), GetProjectTaskDep(session['ProjID'],0));
			#print("Diagram: " + str(TaskDiagram));
			ProductName = {"ProdName" : session['ProdName']};

			#TableList = Table.CreateTableDiagram(GetProjectTask(0,session["ProjID"]), GetProjectTaskDep(0,session["ProjID"]));

			#render html
			return render_template("DisplayData/TaskData.html",TaskRows = TaskRows,TaskDepRows = TaskDepRows, ProdName = ProductName);

		return redirect(url_for("projb.ProjOverv"), code=303);

	except Exception as Error:#on exception register error to file

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/DisplayData/TaskData","ProjTaskDisplay",ProjTaskDisplay);

#The function for the create new task form
def ProjTaskForm():

	try:

		if "ProjID" in session:#if there is no session for this variable, then there may have been an penetration attempt or error

			TaskProjectRows = GetProjectListByID(session['ProjID'],1);
			TaskProjectContractRows = GetProjectContractListByID(session['ProjID'],1);
			TaskRows = GetProjectTask(session['ProjID'],1);

			#render html with tuple data
			return render_template("Forms/TaskForm/TaskForm.html",TaskProjRows = TaskProjectRows, TaskRows = TaskRows, TaskProjContrRows = TaskProjectContractRows);

	except Exception as Error:#on exception register error to file

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/Forms/TaskForm","ProjTaskForm",ProjTaskForm);

#update the selected projects values
def ProjUpdate():

	try:

		if request.method == "POST":#do not enter if it is not a post request

			#Get data from the form
			ContrID = request.form['ContrID'];
			CompID = request.form['CompID'];
			DepID = request.form['DepID'];

			#Set the new values of the current selected project in the database
			SetProject(session['ProjID'], CompID, ContrID, DepID);

			#when finished return to the edit form of the selected project
			return redirect(url_for("projb.ProjEdit"), code=307);

		return redirect(url_for("projb.ProjOverv"), code=303);#if non of the above is true, then redirect to project list

	except Exception as Error:#on exception register error to file

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/DisplayData/ProjectEdit","ProjUpdate",ProjUpdate,methods=["POST"]);

#display the projects edit form  with it's necessary data
def ProjEdit():

	try:

		if request.method == "POST":#do not enter if it is not a post request

			if "ProjID" in session:#if there is no session for this variable, then there may have been an penetration attempt or error

				#Get all the list type that the current project is associated to
				ProjectRows = GetProjectListByID(1,session['ProjID']);
				ContractRows = GetContractList(1);
				CompanyRows = GetCompanyList(1);
				DepartmentRows = GetDepartmentList(1);

				#render html
				return render_template("Forms/ProjectForm/ProjectEditForm.html", ContrRows = ContractRows, ProjRows = ProjectRows, CompRows = CompanyRows, DepRows = DepartmentRows);
		return redirect(url_for("projb.ProjOverv"), code=303);#if non of the above is true, then redirect to project list

	except Exception as Error:#on exception register error to file

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/Forms/ProjectEditForm","ProjEdit",ProjEdit,methods=["POST"]);

#Update the active value of the current selected project to FALSE, it does not actually delete the data
def ProjDel():

	try:

		if request.method == "POST":#do not enter if it is not a post request

			if "ProjID" in session:#if there is no session for this variable, then there may have been an penetration attempt or error
				#Set the active value to 0 to deactivate it
				SetProjectIsActiv(session['ProjID'],0);

		return redirect(url_for("projb.ProjOverv"),code=303);#if non of the above is true, then redirect to project list

	except Exception as Error:#on exception register error to file

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/DeleteProject","ProjDel",ProjDel,methods=["POST"]);

#The project edite form
def ProjForm():

	try:

		ContractRows = GetContractList(1);
		CompanyRows = GetCompanyList(1);
		DepartmentRows = GetDepartmentList(1);

		return render_template("forms/ProjectForm/ProjectForm.html", ContrRows = ContractRows, CompRows = CompanyRows, DepRows = DepartmentRows);

	except Exception as Error:#on exception register error to file

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/AddProject","ProjForm",ProjForm);

#the add new project form
def AddProj():

	try:

		if request.method == "POST":#do not enter if it is not a post request

			ContrID = request.form['ContrID'];
			CompID = request.form['CompID'];
			DepID = request.form['DepID'];

			IProj(ContrID,CompID,DepID);

			return redirect(url_for('projb.ProjForm'), code=303);

		return redirect(url_for('projb.ProjOverv'), code=303);#if non of the above is true, then redirect to project list

	except Exception as Error:#on exception register error to file

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/AddNewProject","AddProj",AddProj,methods=["POST"]);

#The decision making when selecting an option in project list
def ProjOvervLoad():

	try:

		if request.method=="POST":#do not enter if it is not a post request

			if "ProjID" in request.form:#if there is no session for this variable, then there may have been an penetration attempt or error

				session['ProjID'] = request.form['ProjID'];#set the current loaded project to session for the rest of the functions to know
				session['ProdName'] = request.form['ProdName'];

				if "ProjLoad" in request.form:#if submit was ProjLoad then start project load methods

					return redirect(url_for("projb.ProjTaskDisplay"), code=303);

				elif "ProjEdit" in request.form:#if submit was ProjEdit then start project edit methods

					return redirect(url_for("projb.ProjEdit"), code=307);

				elif "ProjDel" in request.form:#if submit was ProjDel then start project delete methods

					return redirect(url_for("projb.ProjDel"), code=307);

		return redirect(url_for("projb.ProjOverv"), code=303);#if non of the above is true, then redirect to project list

	except Exception as Error:#on exception register error to file

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
ProjB.add_url_rule("/DisplayData/ProjectOverview","ProjOvervLoad",ProjOvervLoad,methods=["POST"]);
#//===============================================================//
