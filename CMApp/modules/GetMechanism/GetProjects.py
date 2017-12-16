from . import *

def GetProjectList():
	
	Conn = sqlite3.connect(Prefix + Database);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	SqlScript = " \
	SELECT \
	"+Prefix+"CMProj.CMProjID, \
	"+Prefix+"CMCompInf.CMCompName, \
	"+Prefix+"CMContrInf.CMContractor, \
	"+Prefix+"CMContrInf.CMDateS, \
	"+Prefix+"CMContrInf.CMDueDate, \
	"+Prefix+"CMContrInf.CMProdName \
	\
	FROM \
	"+Prefix+"CMProj, \
	"+Prefix+"CMContrInf, \
	"+Prefix+"CMCompInf \
	\
	WHERE \
	("+Prefix+"CMProj.CMCompID = "+Prefix+"CMCompInf.CMCompID) \
	AND \
	("+Prefix+"CMProj.CMContrID = "+Prefix+"CMContrInf.CMContrID)";
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn.close();
	
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;