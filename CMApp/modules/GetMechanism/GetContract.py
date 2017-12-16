from . import *

def GetContractList():

	Conn = sqlite3.connect(PREFIX + DATABASE);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMContrInf.CMProdName, \
	"+PREFIX+"CMContrInf.CMContrID \
    \
	FROM \
	"+PREFIX+"CMContrInf, \
	"+PREFIX+"CMContr \
    \
	WHERE \
	("+PREFIX+"CMContr.CMContrID = "+PREFIX+"CMContrInf.CMContrID);";
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn.close();
	
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;
	
def GetContractListByProject(ProjID):

	Conn = sqlite3.connect(PREFIX + DATABASE);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	SqlScript = " \
	SELECT \
	"+PREFIX+"CMContrInf.CMProdName, \
	"+PREFIX+"CMContrInf.CMContrID \
    \
	FROM \
	"+PREFIX+"CMContrInf, \
	"+PREFIX+"CMContr, \
	"+PREFIX+"CMProj \
    \
	WHERE \
	("+PREFIX+"CMContr.CMContrID = "+PREFIX+"CMContrInf.CMContrID) \
	AND \
	("+PREFIX+"CMProj.CMContrID = "+PREFIX+"CMContr.CMContrID) \
	AND \
	("+PREFIX+"CMProj.CMProjID = "+str(ProjID)+");";
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn.close();
	
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;