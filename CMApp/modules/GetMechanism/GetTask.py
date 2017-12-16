from . import *

def GetTask():
	
	Conn = sqlite3.connect(PREFIX + DATABASE);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMTask.CMTaskID, \
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
	"+PREFIX+"CMTask, \
	"+PREFIX+"CMTaskInf, \
	"+PREFIX+"CMProj \
    \
	WHERE ("+PREFIX+"CMTask.CMTaskInfID = "+PREFIX+"CMTaskInf.CMTaskInfID) \
	AND ("+PREFIX+"CMTask.CMProjID = "+PREFIX+"CMProj.CMProjID)";
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;
	
def GetProjectTask(ProjectID):
	
	Conn = sqlite3.connect(PREFIX + DATABASE);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
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
	("+PREFIX+"CMTask.CMProjID = "+ProjectID+") \
	AND \
	("+PREFIX+"CMTask.CMActiv = 1)";
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;
	
def GetProjectTaskDep(ProjectID):
	
	Conn = sqlite3.connect(PREFIX + DATABASE);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
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
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;
	
	