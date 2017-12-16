from . import *

from modules.GetMechanism.GetTaskForm import GetFormAssignProject
from modules.InsertMechanism.InsertTask import ITask

#//=======================<Task Functions>=======================//
def TaskForm():

	TableRows = GetFormAssignProject();
	
	#render html with tuple data
	return render_template("Forms/TaskForm.html",rows = TableRows);
TaskB.add_url_rule("/Forms/TaskForm","TaskForm",TaskForm);

def Task():
	
	ITask();
		
	return redirect(url_for("taskb.TaskForm"),code=302);
TaskB.add_url_rule("/Forms/TaskForm","Task",Task,methods=["POST"]);