from .__init__ import *

def GetDepartmentList(RowType):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
		SqlScript = " \
		SELECT \
		"+PREFIX+"CMDepInf.CMDepID, \
		"+PREFIX+"CMDepInf.CMDepName \
		\
		FROM \
		"+PREFIX+"CMDep, \
		"+PREFIX+"CMDepInf \
		\
		WHERE \
		("+PREFIX+"CMDep.CMDepID = "+PREFIX+"CMDepInf.CMDepID) \
		AND \
		("+PREFIX+"CMDepInf.CMActiv= 1);";
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
	
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;