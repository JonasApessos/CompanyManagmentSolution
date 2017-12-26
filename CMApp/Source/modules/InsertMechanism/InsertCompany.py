from .__init__ import *

def ICompany():
	
	try:
	
		if request.method == "POST":
			
			Conn = DatabaseQuery(PREFIX + DATABASE, 0);
			
			CompName = str(request.form["CompName"]);
			CDate = str(request.form["CDate"]);
			Country = str(request.form["Country"]);
			IR = str(request.form["IR"]);
			
			LastIndex = "";
			SqlScript = "";
			
			
			SqlScript = "INSERT INTO " + PREFIX + "CMComp(CMActiv) \
			VALUES \
			(1)";

			Conn.ExecQuery(SqlScript);

			LastIndex = str(Conn.GetLastRowID());
			
			SqlScript = "INSERT INTO " + PREFIX + "CMCompInf(CMCompID,CMCompName,CMDateC,CMLocation,CMLocInterest,CMActiv) \
			VALUES \
			("+LastIndex+",\""+CompName+"\",\""+CDate+"\",\""+Country+"\","+IR+",1)";
			
			Conn.ExecQuery(SqlScript);
			
			Conn.Save();
			Conn.CloseConnection();
			
			#nothing to see heir, just taking out my garbages
			Conn = None;
			CompName = None;
			CDate = None;
			Country = None;
			IR = None;
			LastIndex = None;
			SqlQuery = None;
			
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
