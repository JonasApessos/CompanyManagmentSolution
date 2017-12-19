from .__init__ import *

def ICompany():
	
	if request.method == "POST":
		
		Conn = DatabaseQuery(PREFIX, DATABASE);
		
		CompName = str(request.form["CompName"]);
		CDate = str(request.form["CDate"]);
		Country = str(request.form["Country"]);
		IR = str(request.form["IR"]);
		
		LastIndex = "";
		SqlScript = "";
		
		
		SqlScript = "INSERT INTO " + PREFIX + "CMComp(CMActiv) \
		VALUES \
		(1)";
		

		Conn.SetSqlScript(SqlScript)
		Conn.ExecQuery();

		LastIndex = str(Conn.GetLastRowID());
		
		SqlScript = "INSERT INTO " + PREFIX + "CMCompInf(CMCompID,CMCompName,CMDateC,CMLocation,CMLocInterest,CMActiv) \
		VALUES \
		("+LastIndex+",\""+CompName+"\",\""+CDate+"\",\""+Country+"\","+IR+",1)";
		
		Conn.SetSqlScript(SqlScript);
		Conn.ExecQuery();
		
		Conn.Save();
		Conn.CloseDatabase();
		
		#nothing to see heir, just taking out my garbages
		Conn = None;
		CompName = None;
		CDate = None;
		Country = None;
		IR = None;
		LastIndex = None;
		SqlQuery = None;
