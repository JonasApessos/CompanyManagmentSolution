from .__init__ import *

def GetTaskFormAssignProject():
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
	#Queries
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMContrInf.CMProdName, \
	"+PREFIX+"CMProj.CMProjID \
	\
	FROM \
	"+PREFIX+"CMContrInf, \
	"+PREFIX+"CMProj \
	\
	WHERE ("+PREFIX+"CMContrInf.CMContrID = "+PREFIX+"CMProj.CMContrID)";
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;