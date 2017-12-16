from . import *

def ITask():
	
	if request.method == "POST":
		
		Conn = sqlite3.connect(Prefix + Database);
		Index = Conn.cursor();
		
		#Data from form
		TaskName = request.form["TaskName"];
		ProjOption = request.form["ProjOption"];
		PosPre = int(request.form["PosPre"]);
		NormPre = int(request.form["NormPre"]);
		NegPre = int(request.form["NegPre"]);
		Months = request.form["Months"];
		CDate = request.form["CDate"];
		
		Expected = ((PosPre + (4 * NormPre) + NegPre)/6);
		Variance = (((NegPre - PosPre)/6) ** 2);
		
		#Queries
		LastIndex = 0;
		SqlQuery = "";
		
		SqlQuery = "INSERT INTO " + Prefix + "CMTask(CMProjID,CMActiv) \
		VALUES \
		(?,?)";
		
		Index.execute(SqlQuery,(ProjOption,1));
		
		LastIndex = Index.lastrowid;
		
		SqlQuery = "INSERT INTO " + Prefix + "CMTaskInf(CMTaskID,CMName,CMPos,CMNorm,CMNeg,CMExp,CMVar,CMMonth,CMDateC,CMActiv) \
		VALUES \
		(?,?,?,?,?,?,?,?,?,?)";
		
		Index.execute(SqlQuery,(LastIndex,TaskName,PosPre,NormPre,NegPre,Expected,Variance,Months,CDate,1));
		
		Conn.commit();
		Conn.close();
		
		#nothing to see heir, just taking out my garbages
		Conn = None;
		Index = None;
		TaskName = None;
		ProjOption = None;
		PosPre = None;
		NormPre = None;
		NegPre = None;
		Months = None;
		CDate = None;
		LastIndex = None;
		SqlQuery = None;
		Expected = None;
		Variance = None;
