from . import *

def GetFormDepartment():
	
	Conn = sqlite3.connect(Prefix + Database);
	
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	Rows = 0;
	
	#Get data
	SqlQuery = " \
	SELECT \
	"+Prefix+"CMDep.CMDepID, \
	"+Prefix+"CMDepInf.CMName, \
	"+Prefix+"CMCompInf.CMCompName \
	\
	FROM \
	"+Prefix+"CMDep, \
	"+Prefix+"CMDepInf, \
	"+Prefix+"CMCompInf, \
	"+Prefix+"CMComp \
	\
	WHERE ("+Prefix+"CMDep.CMDepID = "+Prefix+"CMDepInf.CMDepID) \
	AND ("+Prefix+"CMComp.CMCompID = "+Prefix+"CMCompInf.CMCompID) \
	AND ("+Prefix+"CMComp.CMCompID = "+Prefix+"CMDep.CMCompID);";
	
	Index.execute(SqlQuery);
	
	#get data from rows
	Rows = Index.fetchall();
	
	Conn.close();
	
	#nothing to see heir, just taking out my garbages
	Conn = None;
	index = None;
	SqlQuery = None;
	
	return Rows;