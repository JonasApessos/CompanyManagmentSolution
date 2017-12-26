from .__init__ import *

def SetProject(ProjID, CompID, ContrID, DepID):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, 0);
		
		SqlScript = " \
		UPDATE \
		"+PREFIX+"CMProj \
		\
		SET \
		CMCompID = "+str(CompID)+", \
		CMContrID = "+str(ContrID)+" , \
		CMDepID = "+str(DepID)+" \
		\
		WHERE \
		"+PREFIX+"CMProj.CMProjID = "+str(ProjID)+";";
		
		Conn.ExecQuery(SqlScript);
		
		Conn.Save();
		Conn.CloseConnection();
		
		Conn = None;
		SqlScript = None;
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
def SetProjectIsActiv(ProjID,Switch):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, 0);
		
		SqlScript = " \
		UPDATE \
		"+PREFIX+"CMProj \
		\
		SET \
		CMActiv = "+str(Switch)+" \
		\
		WHERE \
		("+PREFIX+"CMProj.CMProjID = "+str(ProjID)+");";
		
		Conn.ExecQuery(SqlScript);
		
		Conn.Save();
		Conn.CloseConnection();
		
		Conn = None;
		SqlScript = None;
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();