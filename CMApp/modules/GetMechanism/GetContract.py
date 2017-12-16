from .__init__ import *

def GetContractList():

	Conn = DatabaseQuery(PREFIX, DATABASE);
	
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMContrInf.CMProdName, \
	"+PREFIX+"CMContrInf.CMContrID \
    \
	FROM \
	"+PREFIX+"CMContrInf, \
	"+PREFIX+"CMContr \
    \
	WHERE \
	("+PREFIX+"CMContr.CMContrID = "+PREFIX+"CMContrInf.CMContrID);";
	
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;
	
def GetContractListByProject(ProjID):
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMContrInf.CMProdName, \
	"+PREFIX+"CMContrInf.CMContrID \
    \
	FROM \
	"+PREFIX+"CMContrInf, \
	"+PREFIX+"CMContr, \
	"+PREFIX+"CMProj \
    \
	WHERE \
	("+PREFIX+"CMContr.CMContrID = "+PREFIX+"CMContrInf.CMContrID) \
	AND \
	("+PREFIX+"CMProj.CMContrID = "+PREFIX+"CMContr.CMContrID) \
	AND \
	("+PREFIX+"CMProj.CMProjID = "+str(ProjID)+");";
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;