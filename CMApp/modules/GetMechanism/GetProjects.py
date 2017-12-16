from .__init__ import *

def GetProjectContractList():

	Conn = DatabaseQuery(PREFIX, DATABASE);
	
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMProj.CMProjID, \
	"+PREFIX+"CMCompInf.CMCompName, \
	"+PREFIX+"CMContrInf.CMContractor, \
	"+PREFIX+"CMContrInf.CMDateS, \
	"+PREFIX+"CMContrInf.CMDueDate, \
	"+PREFIX+"CMContrInf.CMProdName \
	\
	FROM \
	"+PREFIX+"CMProj, \
	"+PREFIX+"CMContrInf, \
	"+PREFIX+"CMCompInf \
	\
	WHERE \
	("+PREFIX+"CMProj.CMCompID = "+PREFIX+"CMCompInf.CMCompID) \
	AND \
	("+PREFIX+"CMProj.CMContrID = "+PREFIX+"CMContrInf.CMContrID) \
	AND \
	("+PREFIX+"CMProj.CMActiv = 1);";
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;
	
	
	
def GetProjectListByID(ProjID):
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMProj.CMProjID, \
	"+PREFIX+"CMProj.CMContrID, \
	"+PREFIX+"CMProj.CMCompID, \
	"+PREFIX+"CMProj.CMDepID \
	\
	FROM \
	"+PREFIX+"CMProj \
	WHERE \
	("+PREFIX+"CMProj.CMProjID = "+str(ProjID)+") \
	AND \
	("+PREFIX+"CMProj.CMActiv = 1)";
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;
	
def GetProjectList():
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMProj.CMProjID, \
	"+PREFIX+"CMProj.CMContrID, \
	"+PREFIX+"CMProj.CMCompID, \
	"+PREFIX+"CMProj.CMDepID \
	\
	FROM \
	"+PREFIX+"CMProj \
	WHERE \
	("+PREFIX+"CMProj.CMActiv = 1)";
	
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();

	Conn.CloseDatabase();
	
	return Rows;