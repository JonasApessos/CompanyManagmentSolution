from . import *

def GetContractList():

	Conn = sqlite3.connect(PREFIX + DATABASE);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	SqlScript = " \
	SELECT \
	RE1201_CMContrInf.CMProdName, \
	RE1201_CMContrInf.CMContrID \
    \
	FROM \
	RE1201_CMContrInf, \
	RE1201_CMContr \
    \
	WHERE \
	(RE1201_CMContr.CMContrID = RE1201_CMContrInf.CMContrID)";
	
	Index.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn.close();
	
	Conn = None;
	Index = None;
	SqlScript = None;
	
	return Rows;