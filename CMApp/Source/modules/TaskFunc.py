from . import *

from modules.GetMechanism.GetTaskForm import GetTaskFormAssignProject
from modules.GetMechanism.GetTask import GetTaskByID
from modules.GetMechanism.GetTask import GetTaskDepByID
from modules.GetMechanism.GetTask import GetTaskDepList
from modules.GetMechanism.GetTask import GetTaskList
from modules.GetMechanism.GetDependencys import GetDepList
from modules.GetMechanism.GetProjects import GetProjectList
from modules.GetMechanism.GetProjects import GetProjectContractList
from modules.GetMechanism.GetContract import GetContractList

from modules.UpdateMechanism.SetTask import SetTask
from modules.UpdateMechanism.SetTask import SetTaskIsActiv

from modules.InsertMechanism.InsertTask import ITask

#//=======================<Task Functions>=======================//
def TaskForm():

	TaskProjectRows = GetProjectContractList();
	TaskRows = GetTaskList(); 
	
	#render html with tuple data
	return render_template("Forms/TaskForm.html",TaskProjRows = TaskProjectRows, TaskRows = TaskRows);
TaskB.add_url_rule("/Forms/TaskForm","TaskForm",TaskForm);

def AddTask():
	
	if request.method == "POST":
		
		#Data from form
		TaskName = request.form["TaskName"];
		ProjOption = request.form["ProjOption"];
		PosPre = request.form["PosPre"];
		NormPre = request.form["NormPre"];
		NegPre = request.form["NegPre"];
		Months = request.form["Months"];
		Dep = request.values.getlist('TaskDep[]');
		
		ITask(TaskName,ProjOption,float(PosPre),float(NormPre),float(NegPre),Months,Dep);
		
	return redirect(url_for("taskb.TaskForm"), code=302);
TaskB.add_url_rule("/Forms/AddTaskForm","AddTask",AddTask,methods=["POST"]);



def TaskEdit():
	
	if request.method == "POST":
		
		if "TaskID" in session:

			ProjectRows = GetProjectList();
			ContractRows = GetContractList();
			TaskDependencyRows = GetTaskDepList();
			TaskDataRows = GetTaskByID(session['TaskID']);
			TaskRows = GetTaskList();
	
			return render_template("/Forms/TaskEditForm.html",ProjRows = ProjectRows,ContrRows = ContractRows, TaskDataRows = TaskDataRows, TaskDepRows = TaskDependencyRows, TaskRows = TaskRows);

TaskB.add_url_rule("/Forms/TaskEditForm","TaskEdit",TaskEdit,methods=["POST"]);

def UpdateTask():
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
	return redirect(url_for("projb.ProjOverv"), code=302);
TaskB.add_url_rule("/Forms/UpdateTaskForm","UpdateTask",UpdateTask,methods=["POST"]);

def DeleteTask():

	if request.method == "POST":
		SetTaskIsActiv(session['TaskID'],0);

		return redirect(url_for("projb.ProjTaskDisplay"), code=307);
		
	return redirect(url_for("projb.ProjOverv"), code=302);
TaskB.add_url_rule("/Forms/DeleteTask","DeleteTask",DeleteTask,methods=["POST"]);

def TaskLoad():

	if request.method == "POST":

		if "TaskID" in request.form:
			
			session['TaskID'] = request.form['TaskID'];
		
			if "TaskEdit" in request.form:
				return redirect(url_for("taskb.TaskEdit"), code=307);
			
			elif "TaskDel" in request.form:
				return redirect(url_for("taskb.DeleteTask"), code=307);
	
	return redirect(url_for("projb.ProjOverv"), code=302);
TaskB.add_url_rule("/Forms/TaskEdit","TaskLoad",TaskLoad,methods=["POST"]);
	