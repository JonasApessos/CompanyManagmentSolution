from .__init__ import *

def GetTaskList(RowType):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript = " \
		SELECT \
		"+PREFIX+"CMTaskInf.CMTaskID, \
		"+PREFIX+"CMTask.CMProjID, \
		"+PREFIX+"CMTaskInf.CMDateC, \
		"+PREFIX+"CMTaskInf.CMName, \
		"+PREFIX+"CMTaskInf.CMMonth, \
		"+PREFIX+"CMTaskInf.CMPos, \
		"+PREFIX+"CMTaskInf.CMNorm, \
		"+PREFIX+"CMTaskInf.CMNeg, \
		"+PREFIX+"CMTaskInf.CMVar, \
		"+PREFIX+"CMTaskInf.CMExp \
		\
		FROM \
		"+PREFIX+"CMTaskInf, \
		"+PREFIX+"CMTask \
		WHERE \
		("+PREFIX+"CMTaskInf.CMTaskID = "+PREFIX+"CMTask.CMTaskID) \
		AND \
		("+PREFIX+"CMTask.CMTaskID = "+PREFIX+"CMTaskInf.CMTaskID)\
		AND \
		("+PREFIX+"CMTask.CMActiv = 1);";
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
		
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;
	
def GetTaskByID(RowType, TaskID):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
		SqlScript = " \
		SELECT \
		"+PREFIX+"CMTaskInf.CMTaskID, \
		"+PREFIX+"CMTask.CMProjID, \
		"+PREFIX+"CMTaskInf.CMDateC, \
		"+PREFIX+"CMTaskInf.CMName, \
		"+PREFIX+"CMTaskInf.CMMonth, \
		"+PREFIX+"CMTaskInf.CMPos, \
		"+PREFIX+"CMTaskInf.CMNorm, \
		"+PREFIX+"CMTaskInf.CMNeg, \
		"+PREFIX+"CMTaskInf.CMVar, \
		"+PREFIX+"CMTaskInf.CMExp \
		\
		FROM \
		"+PREFIX+"CMTaskInf, \
		"+PREFIX+"CMTask \
		WHERE \
		("+PREFIX+"CMTaskInf.CMTaskID = "+str(TaskID)+") \
		AND \
		("+PREFIX+"CMTask.CMTaskID = "+PREFIX+"CMTaskInf.CMTaskID)\
		AND \
		("+PREFIX+"CMTaskInf.CMActiv = 1);";
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;
		
def GetProjectTask(RowType, ProjectID):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
		SqlScript = " \
		SELECT \
		"+PREFIX+"CMTaskInf.CMTaskID, \
		"+PREFIX+"CMTask.CMProjID, \
		"+PREFIX+"CMTaskInf.CMName, \
		"+PREFIX+"CMTaskInf.CMPos, \
		"+PREFIX+"CMTaskInf.CMNorm, \
		"+PREFIX+"CMTaskInf.CMNeg, \
		"+PREFIX+"CMTaskInf.CMExp, \
		"+PREFIX+"CMTaskInf.CMMonth, \
		"+PREFIX+"CMTaskInf.CMDateC, \
		"+PREFIX+"CMTaskInf.CMVar \
		\
		FROM \
		"+PREFIX+"CMTaskInf, \
		"+PREFIX+"CMProj, \
		"+PREFIX+"CMTask \
		\
		WHERE \
		("+PREFIX+"CMTask.CMProjID = "+PREFIX+"CMProj.CMProjID) \
		AND \
		("+PREFIX+"CMTask.CMTaskID = "+PREFIX+"CMTaskInf.CMTaskID) \
		AND \
		("+PREFIX+"CMTask.CMProjID = "+str(ProjectID)+") \
		AND \
		("+PREFIX+"CMTask.CMActiv = 1)";
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
		
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return redirect(url_for("Index"), code=303);
	
def GetProjectTaskDep(RowType, ProjectID):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
		SqlScript = " \
		SELECT \
		"+PREFIX+"CMTaskDep.CMTaskID, \
		"+PREFIX+"CMTaskDep.CMDep, \
        "+PREFIX+"CMTaskInf.CMName \
		\
		FROM \
		"+PREFIX+"CMTaskDep, \
		"+PREFIX+"CMTask, \
		"+PREFIX+"CMProj,\
        "+PREFIX+"CMTaskInf \
		\
		WHERE \
		("+PREFIX+"CMTask.CMTaskID = "+PREFIX+"CMTaskDep.CMTaskID) \
		AND \
		("+PREFIX+"CMTask.CMTaskID = "+PREFIX+"CMTaskDep.CMTaskID) \
        AND \
		("+PREFIX+"CMTaskInf.CMTaskID = "+PREFIX+"CMTaskDep.CMDep) \
		AND \
		("+PREFIX+"CMProj.CMProjID = 1) \
		AND \
		("+PREFIX+"CMTask.CMActiv = 1)";
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;

def GetTaskDepByID(RowType, TaskID):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
		SqlScript =" \
		SELECT \
		"+PREFIX+"CMTaskDep.CMTaskID, \
		"+PREFIX+"CMTaskDep.CMDep \
		\
		FROM \
		"+PREFIX+"CMTaskDep \
		\
		WHERE \
		("+PREFIX+"CMTaskDep.CMTaskID = "+str(TaskID)+") \
		AND \
		("+PREFIX+"CMTaskDep.CMActiv = 1);";
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
		
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;
	
def GetTaskDepList(RowType):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
		SqlScript =" \
		SELECT \
		"+PREFIX+"CMTaskDep.CMTaskID, \
		"+PREFIX+"CMTaskDep.CMDep \
		\
		FROM \
		"+PREFIX+"CMTaskDep \
		\
		WHERE \
		("+PREFIX+"CMTaskDep.CMActiv = 1);";
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;