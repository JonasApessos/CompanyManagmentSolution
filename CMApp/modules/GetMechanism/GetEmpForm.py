from . import *

def GetFormDepartment():
	
	Conn = sqlite3.connect(PREFIX + DATABASE);
	
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	Rows = 0;
	
	#Get data
	SqlQuery = " \
	SELECT \
	"+PREFIX+"CMDep.CMDepID, \
	"+PREFIX+"CMDepInf.CMName, \
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
	
	Index.execute(SqlQuery);
	
	#get data from rows
	Rows = Index.fetchall();
	
	Conn.close();
	
	#nothing to see heir, just taking out my garbages
	Conn = None;
	index = None;
	SqlQuery = None;
	
	return Rows;