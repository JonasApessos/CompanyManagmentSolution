from .__init__ import *

def ITask(Name,ProjectOption,Pos,Norm,Neg,Months,Dep):
	
	Conn = DatabaseQuery(PREFIX,DATABASE);	
		
	Exp = ((Pos + (4 * Norm) + Neg)/6);
	Var = (((Neg - Pos)/6) ** 2);
		
	#Queries
	LastIndex = 0;
	SqlQuery = "";
		
	SqlScript = "INSERT INTO " + PREFIX + "CMTask(CMProjID,CMActiv) \
	VALUES \
	("+str(ProjectOption)+",1)";
	
	Conn.SetSqlScript(SqlScript);
	
	Conn.ExecQuery();
		
	LastIndex = Conn.GetLastRowID();
		
	SqlScript = "INSERT INTO " + PREFIX + "CMTaskInf(CMTaskID,CMName,CMPos,CMNorm,CMNeg,CMExp,CMVar,CMMonth,CMActiv) \
	VALUES \
	("+str(LastIndex)+",\""+str(Name)+"\","+str(Pos)+","+str(Norm)+","+str(Neg)+","+str(Exp)+","+str(Var)+","+str(Months)+",1)";
	
	Conn.SetSqlScript(SqlScript);
	Conn.ExecQuery();
	
	for i in range(0,len(Dep)):
		SqlScript = "INSERT INTO " + PREFIX + "CMTaskDep(CMTaskID,CMDep,CMActiv) \
		VALUES \
		("+str(LastIndex)+","+str(Dep[i])+",1)";
		Conn.SetSqlScript(SqlScript);
		Conn.ExecQuery();
	
	Conn.Save();
	Conn.CloseDatabase();
		
	#nothing to see heir, just taking out my garbages
	Conn = None;
	Name = None;
	ProjectOption = None;
	Pos = None;
	Norm = None;
	Neg = None;
	Months = None;
	LastIndex = None;
	SqlScript = None;
	Expected = None;
	Variance = None;
