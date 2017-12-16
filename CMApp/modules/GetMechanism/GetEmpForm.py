from .__init__ import *

def GetFormDepartment():
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
	#Query
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMDep.CMDepID, \
	"+PREFIX+"CMDepInf.CMDepName, \
	"+PREFIX+"CMCompInf.CMCompName \
	\
	FROM \
	"+PREFIX+"CMDep, \
	"+PREFIX+"CMDepInf, \
	"+PREFIX+"CMCompInf, \
	"+PREFIX+"CMComp \
	\
	WHERE ("+PREFIX+"CMDep.CMDepID = "+PREFIX+"CMDepInf.CMDepID) \
	AND ("+PREFIX+"CMComp.CMCompID = "+PREFIX+"CMCompInf.CMCompID) \
	AND ("+PREFIX+"CMComp.CMCompID = "+PREFIX+"CMDep.CMCompID);";
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;