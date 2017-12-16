from . import *

def GetProjectList():
	
	Conn = sqlite3.connect(PREFIX + DATABASE);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
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
	("+PREFIX+"CMProj.CMContrID = "+PREFIX+"CMContrInf.CMContrID)";
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn.close();
	
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;