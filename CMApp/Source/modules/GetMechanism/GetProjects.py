from .__init__ import *

def GetProjectContractList(RowType):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
		SqlScript = " \
		SELECT \
		"+PREFIX+"CMProj.CMProjID, \
		"+PREFIX+"CMCompInf.CMCompName, \
		"+PREFIX+"CMContrInf.CMContractor, \
		"+PREFIX+"CMContrInf.CMDateS, \
		"+PREFIX+"CMContrInf.CMDueDate, \
		"+PREFIX+"CMContrInf.CMProdName \
		\
		FROM \
		"+PREFIX+"CMProj, \
		"+PREFIX+"CMContrInf, \
		"+PREFIX+"CMCompInf \
		\
		WHERE \
		("+PREFIX+"CMProj.CMCompID = "+PREFIX+"CMCompInf.CMCompID) \
		AND \
		("+PREFIX+"CMProj.CMContrID = "+PREFIX+"CMContrInf.CMContrID) \
		AND \
		("+PREFIX+"CMProj.CMActiv = 1);";
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
		
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;
		
def GetProjectContractListByID(RowType, ProjID):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
		SqlScript = " \
		SELECT \
		"+PREFIX+"CMProj.CMProjID, \
		"+PREFIX+"CMCompInf.CMCompName, \
		"+PREFIX+"CMContrInf.CMContractor, \
		"+PREFIX+"CMContrInf.CMDateS, \
		"+PREFIX+"CMContrInf.CMDueDate, \
		"+PREFIX+"CMContrInf.CMProdName \
		\
		FROM \
		"+PREFIX+"CMProj, \
		"+PREFIX+"CMContrInf, \
		"+PREFIX+"CMCompInf, \
		"+PREFIX+"CMContr \
		\
		WHERE \
		("+PREFIX+"CMProj.CMCompID = "+PREFIX+"CMCompInf.CMCompID) \
		AND \
		("+PREFIX+"CMProj.CMContrID = "+PREFIX+"CMContr.CMContrID) \
		AND \
		("+PREFIX+"CMProj.CMContrID = "+PREFIX+"CMContrInf.CMContrID) \
		AND \
		("+PREFIX+"CMProj.CMContrID = "+ProjID+") \
		AND \
		("+PREFIX+"CMProj.CMActiv = 1);";
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
		
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;
	
	
	
def GetProjectListByID(RowType, ProjID):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
		SqlScript = " \
		SELECT \
		"+PREFIX+"CMProj.CMProjID, \
		"+PREFIX+"CMProj.CMContrID, \
		"+PREFIX+"CMProj.CMCompID, \
		"+PREFIX+"CMProj.CMDepID \
		\
		FROM \
		"+PREFIX+"CMProj \
		WHERE \
		("+PREFIX+"CMProj.CMProjID = "+str(ProjID)+") \
		AND \
		("+PREFIX+"CMProj.CMActiv = 1)";
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
		
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;
	
def GetProjectList(RowType):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
		SqlScript = " \
		SELECT \
		"+PREFIX+"CMProj.CMProjID, \
		"+PREFIX+"CMProj.CMContrID, \
		"+PREFIX+"CMProj.CMCompID, \
		"+PREFIX+"CMProj.CMDepID \
		\
		FROM \
		"+PREFIX+"CMProj \
		WHERE \
		("+PREFIX+"CMProj.CMActiv = 1)";
		
		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();
		
		return Rows;
	
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;