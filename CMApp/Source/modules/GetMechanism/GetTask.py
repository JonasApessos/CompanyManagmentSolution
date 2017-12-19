from .__init__ import *

def GetTaskList():
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
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
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;
	
def GetTaskByID(TaskID):
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
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
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;
	
def GetProjectTask(ProjectID):
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMTaskInf.CMTaskID, \
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
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;
	
def GetProjectTaskDep(ProjectID):
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMTaskDep.CMTaskID, \
	"+PREFIX+"CMTaskDep.CMDep \
	\
	FROM \
	"+PREFIX+"CMTaskDep, \
	"+PREFIX+"CMTask, \
	"+PREFIX+"CMProj \
	\
	WHERE \
	("+PREFIX+"CMTask.CMTaskID = RE1201_CMTaskDep.CMTaskID) \
	AND \
	("+PREFIX+"CMTask.CMTaskID = RE1201_CMTaskDep.CMTaskID) \
	AND \
	("+PREFIX+"CMProj.CMProjID = "+ProjectID+") \
	AND \
	("+PREFIX+"CMTask.CMActiv = 1)";
	
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;

def GetTaskDepByID(TaskID):
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
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
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;
	
def GetTaskDepList():
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
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
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;
	
	