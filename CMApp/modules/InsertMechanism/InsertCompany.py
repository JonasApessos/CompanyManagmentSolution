

from . import *

def ICompany():
	
	if request.method == "POST":
		
		Conn = sqlite3.connect(PREFIX + DATABASE);
		Index = Conn.cursor();
		
		CompName = request.form["CompName"];
		CDate = request.form["CDate"];
		Country = request.form["Country"];
		IR = request.form["IR"];
		
		
		LastIndex = 0;
		SqlQuery = "";
		
		SqlQuery = "INSERT INTO " + PREFIX + "CMComp(CMActiv) \
		VALUES \
		(?)";
		
		Index.execute(SqlQuery,(1,));
		
		LastIndex = Index.lastrowid;
		
		SqlQuery = "INSERT INTO " + PREFIX + "CMCompInf(CMCompID,CMCompName,CMDateC,CMLocation,CMLocInterest,CMActiv) \
		VALUES \
		(?,?,?,?,?,?)";
		
		Index.execute(SqlQuery,(LastIndex,CompName,CDate,Country,IR,1));
		
		Conn.commit();
		Conn.close();
		
		#nothing to see heir, just taking out my garbages
		Conn = None;
		Index = None;
		CompName = None;
		CDate = None;
		Country = None;
		IR = None;
		LastIndex = None;
		SqlQuery = None;
