from .__init__ import *

def GetFormDepartment(RowType):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
		#Query
		SqlScript = " \
		SELECT \
		"+PREFIX+"CMDep.CMDepID, \
		"+PREFIX+"CMDepInf.CMDepName, \
		"+PREFIX+"CMCompInf.CMCompName \
		\
		FROM \
		"+PREFIX+"CMDep, \
		"+PREFIX+"CMDepInf, \
		"+PREFIX+"CMCompInf, \
		"+PREFIX+"CMComp \
		\
		WHERE ("+PREFIX+"CMDep.CMDepID = "+PREFIX+"CMDepInf.CMDepID) \
		AND ("+PREFIX+"CMComp.CMCompID = "+PREFIX+"CMCompInf.CMCompID) \
		AND ("+PREFIX+"CMComp.CMCompID = "+PREFIX+"CMDep.CMCompID);";
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
		
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;