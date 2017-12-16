from . import *

def GetFormAssignProject():
	
	Conn = sqlite3.connect(PREFIX + DATABASE);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	Rows = 0;
	
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
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn.close();
	
	#nothing to see heir, just taking out my garbages
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;