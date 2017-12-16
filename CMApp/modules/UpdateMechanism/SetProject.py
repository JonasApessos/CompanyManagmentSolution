from . import *

def SetProject(ProjID):
	
	
	Conn = sqlite3.connect(PREFIX + DATABASE);
	
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
	
	Conn.commit();
	Conn.close();
	
	Conn = None;
	Index = None;
	SqlScript = None;
	
def SetProjectIsActiv(ProjID,Switch):
	
	
	Conn = sqlite3.connect(PREFIX + DATABASE);
	
	Index = Conn.cursor();
	
	SqlScript = " \
	UPDATE \
	"+PREFIX+"CMProj \
	\
	SET \
	CMActiv = "+Switch+" \
	\
	WHERE \
	("+PREFIX+"CMProj.CMProjID = "+ProjID+");";
	
	Index.execute(SqlScript);
	
	Conn.commit();
	Conn.close();
	
	Conn = None;
	Index = None;
	SqlScript = None;