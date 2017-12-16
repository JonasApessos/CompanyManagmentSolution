from . import *

def SetProject(ProjID):
	
	
	Conn = sqlite3.connect(PREFIX + DATABASE);
	#Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	SqlScript = " \
	UPDATE \
	"+PREFIX+"CMProj \
	\
	SET \
	CMCompID = 1, \
	CMContrID = 1 , \
	CMDepID = 1 \
	\
	WHERE \
	"+PREFIX+"CMProj.CMProjID = "+ProjID+";";
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn.close();
	
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;