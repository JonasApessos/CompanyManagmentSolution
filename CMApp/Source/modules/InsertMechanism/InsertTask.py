from .__init__ import *

def ITask(Name,ProjID,Pos,Norm,Neg,Months,Dep):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, 0);	
			
		Exp = ((Pos + (4 * Norm) + Neg)/6);
		Var = (((Neg - Pos)/6) ** 2);
			
		#Queries
		LastIndex = 0;
		SqlQuery = "";
			
		SqlScript = "INSERT INTO " + PREFIX + "CMTask(CMProjID,CMActiv) \
		VALUES \
		("+str(ProjID)+",1)";
		
		Conn.ExecQuery(SqlScript);
			
		LastIndex = Conn.GetLastRowID();
			
		SqlScript = "INSERT INTO " + PREFIX + "CMTaskInf(CMTaskID,CMName,CMPos,CMNorm,CMNeg,CMExp,CMVar,CMMonth,CMActiv) \
		VALUES \
		("+str(LastIndex)+",\""+str(Name)+"\","+str(Pos)+","+str(Norm)+","+str(Neg)+","+str(Exp)+","+str(Var)+","+str(Months)+",1)";
		
		Conn.ExecQuery(SqlScript);
		
		DepLength = len(Dep);
		
		if DepLength > 0:
			for i in range(0,len(Dep)):
				SqlScript = "INSERT INTO " + PREFIX + "CMTaskDep(CMTaskID,CMDep,CMActiv) \
				VALUES \
				("+str(LastIndex)+","+str(Dep[i])+",1)";
			
				Conn.ExecQuery(SqlScript);
		else:
			SqlScript = "INSERT INTO " + PREFIX + "CMTaskDep(CMTaskID,CMDep,CMActiv) \
			VALUES \
			("+str(LastIndex)+",NULL,1)";
			
			Conn.ExecQuery(SqlScript);
		
		Conn.Save();
		Conn.CloseConnection();
			
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
		Exp = None;
		Var = None;
		
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return -1;
