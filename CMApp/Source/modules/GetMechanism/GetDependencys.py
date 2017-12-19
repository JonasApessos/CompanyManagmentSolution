from .__init__ import *

def GetDepList():
	
	Conn = DatabaseQuery(PREFIX , DATABASE);
	
	SqlScript=" \
	SELECT \
	"+PREFIX+"CMTaskDep.CMTaskID, \
	"+PREFIX+"CMTaskDep.CMDep \
	\
	FROM \
	"+PREFIX+"CMTaskDep \
	\
	WHERE \
	("+PREFIX+"CMTaskDep.CMActiv = 1);"
	
	Conn.SetSqlScript(SqlScript);
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;
	
def GetDepProjListByID(ProjID):
	
	Conn = DatabaseQuery(PREFIX , DATABASE);
	
	SqlScript=" \
	SELECT \
	"+PREFIX+"CMTaskDep.CMTaskID, \
	"+PREFIX+"CMTaskDep.CMDep \
	\
	FROM \
	"+PREFIX+"CMTaskDep, \
	"+PREFIX+"CMTask \
	\
	WHERE \
	("+PREFIX+"CMTask.CMProjID = "+str(ProjID)+")\
	AND \
	("+PREFIX+"CMTask.CMTaskID = "+PREFIX+"CMTaskDep.CMTaskID) \
	AND \
	("+PREFIX+"CMTaskDep.CMActiv = 1);"
	
	Conn.SetSqlScript(SqlScript);
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;