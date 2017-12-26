from .__init__ import *

def GetContractList(RowType):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
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
		("+PREFIX+"CMContr.CMContrID = "+PREFIX+"CMContrInf.CMContrID) \
		AND \
		("+PREFIX+"CMContr.CMActiv = 1);";
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;
	
def GetContractListByProject(RowType,ProjID):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
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
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
	
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;