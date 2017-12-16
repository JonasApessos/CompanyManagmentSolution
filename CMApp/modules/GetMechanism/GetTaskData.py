from . import *

def GetTaskData():
	
	Conn = sqlite3.connect(Prefix + Database);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	SqlScript = " \
	SELECT \
	"+Prefix+"CMTask.CMTaskID, \
	"+Prefix+"CMTaskInf.CMDateC, \
	"+Prefix+"CMTaskInf.CMName, \
	"+Prefix+"CMTaskInf.CMMonth, \
	"+Prefix+"CMTaskInf.CMPos, \
	"+Prefix+"CMTaskInf.CMNorm, \
	"+Prefix+"CMTaskInf.CMNeg, \
	"+Prefix+"CMTaskInf.CMVar, \
	"+Prefix+"CMTaskInf.CMExp \
    \
	FROM \
	"+Prefix+"CMTask, \
	"+Prefix+"CMTaskInf, \
	"+Prefix+"CMProj \
    \
	WHERE ("+Prefix+"CMTask.CMTaskInfID = "+Prefix+"CMTaskInf.CMTaskInfID) \
	AND ("+Prefix+"CMTask.CMProjID = "+Prefix+"CMProj.CMProjID)";
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;
	
def GetProjectTaskData(ProjectID):
	
	Conn = sqlite3.connect(Prefix + Database);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	SqlScript = " \
	SELECT \
	"+Prefix+"CMTaskInf.CMTaskID, \
	"+Prefix+"CMTaskInf.CMName, \
	"+Prefix+"CMTaskInf.CMPos, \
	"+Prefix+"CMTaskInf.CMNorm, \
	"+Prefix+"CMTaskInf.CMNeg, \
	"+Prefix+"CMTaskInf.CMExp, \
	"+Prefix+"CMTaskInf.CMMonth, \
	"+Prefix+"CMTaskInf.CMDateC, \
	"+Prefix+"CMTaskInf.CMVar \
	\
	FROM \
	"+Prefix+"CMTaskInf, \
	"+Prefix+"CMProj, \
	"+Prefix+"CMTask \
	\
	WHERE \
	("+Prefix+"CMTask.CMProjID = "+Prefix+"CMProj.CMProjID) \
	AND \
	("+Prefix+"CMTask.CMTaskID = "+Prefix+"CMTaskInf.CMTaskID) \
	AND \
	("+Prefix+"CMTask.CMProjID = "+ProjectID+") \
	AND \
	("+Prefix+"CMTask.CMActiv = 1)";
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;
	
def GetProjectTaskDataDep(ProjectID):
	
	Conn = sqlite3.connect(Prefix + Database);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	SqlScript = " \
	SELECT \
	"+Prefix+"CMTaskInf.CMTaskID, \
	"+Prefix+"CMTaskInf.CMName, \
	"+Prefix+"CMTaskInf.CMPos, \
	"+Prefix+"CMTaskInf.CMNorm, \
	"+Prefix+"CMTaskInf.CMNeg, \
	"+Prefix+"CMTaskInf.CMExp, \
	"+Prefix+"CMTaskInf.CMMonth, \
	"+Prefix+"CMTaskInf.CMDateC, \
	"+Prefix+"CMTaskInf.CMVar \
	\
	FROM \
	"+Prefix+"CMTaskInf, \
	"+Prefix+"CMProj, \
	"+Prefix+"CMTask \
	\
	WHERE \
	("+Prefix+"CMTask.CMProjID = "+Prefix+"CMProj.CMProjID) \
	AND \
	("+Prefix+"CMTask.CMTaskID = "+Prefix+"CMTaskInf.CMTaskID) \
	AND \
	("+Prefix+"CMTask.CMProjID = "+ProjectID+") \
	AND \
	("+Prefix+"CMTask.CMActiv = 1)";
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;
	
	