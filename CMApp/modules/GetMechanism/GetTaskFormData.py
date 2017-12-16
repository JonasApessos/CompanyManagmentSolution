from . import *

def GetFormAssignProject():
	
	Conn = sqlite3.connect(Prefix + Database);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	Rows = 0;
	
	#Queries
	SqlScript = " \
	SELECT \
	"+Prefix+"CMContrInf.CMProdName, \
	"+Prefix+"CMProj.CMProjID \
	\
	FROM \
	"+Prefix+"CMContrInf, \
	"+Prefix+"CMProj \
	\
	WHERE ("+Prefix+"CMContrInf.CMContrID = "+Prefix+"CMProj.CMContrID)";
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn.close();
	
	#nothing to see heir, just taking out my garbages
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;