from .__init__ import *

def GetTaskFormAssignProject(RowType):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
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
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
		
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;