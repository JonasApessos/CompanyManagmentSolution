from .__init__ import *


def GetCompanyList():
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMCompInf.CMCompID, \
	"+PREFIX+"CMCompInf.CMCompName \
	\
	FROM \
	"+PREFIX+"CMCompInf, \
	"+PREFIX+"CMComp \
	\
	WHERE \
	("+PREFIX+"CMCompInf.CMCompID = "+PREFIX+"CMComp.CMCompID);";
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;
	