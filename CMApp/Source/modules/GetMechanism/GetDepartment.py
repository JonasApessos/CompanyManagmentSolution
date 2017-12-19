from .__init__ import *

def GetDepartmentList():
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMDepInf.CMDepID, \
	"+PREFIX+"CMDepInf.CMDepName \
	\
	FROM \
	"+PREFIX+"CMDep, \
	"+PREFIX+"CMDepInf \
	\
	WHERE \
	("+PREFIX+"CMDep.CMDepID = "+PREFIX+"CMDepInf.CMDepID) \
	AND \
	("+PREFIX+"CMDepInf.CMActiv= 1);";
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;