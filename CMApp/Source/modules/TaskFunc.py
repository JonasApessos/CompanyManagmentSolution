from . import *

from modules.GetMechanism.GetTaskForm import GetTaskFormAssignProject
from modules.GetMechanism.GetTask import GetTaskByID, GetTaskDepByID, GetTaskDepList, GetTaskList
from modules.GetMechanism.GetDependencys import GetDepList
from modules.GetMechanism.GetProjects import GetProjectList, GetProjectContractList
from modules.GetMechanism.GetContract import GetContractList

from modules.UpdateMechanism.SetTask import SetTask, SetTaskIsActiv

from modules.InsertMechanism.InsertTask import ITask

import inspect

#//=======================<Task Functions>=======================//

#add new task in the database
def AddTask():
	
	try:
	
		if request.method == "POST":

			#Data from form
			TaskName = request.form["TaskName"];
			ProjID = request.form["ProjID"];
			Pos = request.form["PosPre"];
			Norm = request.form["NormPre"];
			Neg = request.form["NegPre"];
			Months = request.form["Months"];
			
			if "TaskDep[]" in request.form:
				Dep = request.values.getlist('TaskDep[]');
			else:
				Dep = [];
			
			#Insert new data in the database
			ITask(TaskName, ProjID, float(Pos), float(Norm), float(Neg), Months, Dep);
		
		#if all else fails redirect to this url
		return redirect(url_for("projb.ProjTaskForm"), code=303);
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
TaskB.add_url_rule("/Forms/AddTaskForm","AddTask",AddTask,methods=["POST"]);

#Set new values of the selected task in the database
def TaskEdit():
	
	try:
	
		if request.method == "POST":
			
			if "TaskID" in session:

				#Get project list
				ProjectRows = GetProjectList(1);
				
				#Get contract list
				ContractRows = GetContractList(1);
				
				#Get task dependency's 
				TaskDependencyRows = GetTaskDepList(1);
				
				#Get the selected task data
				TaskDataRows = GetTaskByID(1, session['TaskID']);
				
				#Get task list
				TaskRows = GetTaskList(1);
		
				return render_template("/Forms/TaskEditForm.html",ProjRows = ProjectRows,ContrRows = ContractRows, TaskDataRows = TaskDataRows, TaskDepRows = TaskDependencyRows, TaskRows = TaskRows);
				
		return redirect(url_for("projb.ProjOverv"), code=303);
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
TaskB.add_url_rule("/Forms/TaskEditForm","TaskEdit",TaskEdit,methods=["POST"]);

def UpdateTask():

	try:

		if request.method == "POST":
		
			TaskName = request.form['TaskName'];
			ProjOption = request.form['ProjOption'];
			Pos = request.form['PosPre'];
			Norm = request.form['NormPre'];
			Neg = request.form['NegPre'];
			Month = request.form['Months'];
		
			if "TaskID" in session:
				SetTask(session['TaskID'],TaskName,ProjOption,Pos,Norm,Neg,Month);
		
				return redirect(url_for("taskb.TaskEdit"), code=307);
				
		return redirect(url_for("taskb.TaskForm"), code=307);
		
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
TaskB.add_url_rule("/Forms/UpdateTaskForm","UpdateTask",UpdateTask,methods=["POST"]);

def DeleteTask():

	try:

		if request.method == "POST":
			SetTaskIsActiv(session['TaskID'],0);

			return redirect(url_for("projb.ProjTaskDisplay"), code=307);
			
		return redirect(url_for("projb.ProjOverv"), code=303);
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
TaskB.add_url_rule("/Forms/DeleteTask","DeleteTask",DeleteTask,methods=["POST"]);

def TaskLoad():

	try:

		if request.method == "POST":

			if "TaskID" in request.form:
				
				session['TaskID'] = request.form['TaskID'];
			
				if "TaskEdit" in request.form:
					return redirect(url_for("taskb.TaskEdit"), code=307);
				
				elif "TaskDel" in request.form:
					return redirect(url_for("taskb.DeleteTask"), code=307);
		
		return redirect(url_for("projb.ProjOverv"), code=303);
	
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return render_template("ErrorIndex.html");
TaskB.add_url_rule("/Forms/TaskEdit","TaskLoad",TaskLoad,methods=["POST"]);
	