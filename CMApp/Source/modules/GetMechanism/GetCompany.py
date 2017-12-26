from .__init__ import *


def GetCompanyList(RowType):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
		SqlScript = " \
		SELECT \
		"+PREFIX+"CMCompInf.CMCompID, \
		"+PREFIX+"CMCompInf.CMCompName \
		\
		FROM \
		"+PREFIX+"CMCompInf, \
		"+PREFIX+"CMComp \
		\
		WHERE \
		("+PREFIX+"CMCompInf.CMCompID = "+PREFIX+"CMComp.CMCompID);";
			
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
		
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;
	