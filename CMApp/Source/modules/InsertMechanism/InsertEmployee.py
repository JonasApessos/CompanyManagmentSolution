from .__init__ import *

def IEmployee():
	
	try:

		if request.method == "POST":
			
			Conn = DatabaseQuery(PREFIX + DATABASE, 0);
			
			#Data from form
			EmpName = request.form["EmpName"];
			BDay = request.form["BDay"];
			EmpCity = request.form["EmpCity"];
			EmpCivilCode = request.form["EmpCivilCode"];
			EmpAvail = request.form["EmpAvail"];
			EmpDep = request.form["DepOption"];
			EmpSal = request.form["EmpSal"];
			EmpSalDateS = request.form["EmpSalDateS"];
			
			
			#Queries
			LastIndex = 0;
			SqlScript = "";
			
			SqlScript = "INSERT INTO " + PREFIX + "CMEmp(CMDepID,CMActiv) \
			VALUES \
			("+str(EmpDep)+",1)";
			#Index.execute(SqlScript,(EmpDep,1));
			
			Conn.ExecQuery(SqlScript);
			
			SqlScript = "INSERT INTO " + PREFIX + "CMEmpInf(CMEmpID,CMEmpName,CMBirthDate,CMCity,CMCivCode,CMAvail,CMActiv) \
			VALUES \
			("+str(LastIndex)+",\""+str(EmpName)+"\",\""+str(BDay)+"\",\""+str(EmpCity)+"\",\""+str(EmpCivilCode)+"\","+str(EmpAvail)+",1)";
			#Index.execute(SqlScript,(LastIndex,EmpName,BDay,EmpCity,EmpCivilCode,EmpAvail,1));
			
			Conn.ExecQuery(SqlScript);
			
			LastIndex = Conn.GetLastRowID();
			
			SqlScript = "INSERT INTO " + PREFIX + "CMEmpSal(CMEmpID,CMIncome,CMDateC,CMActiv) \
			VALUES \
			("+str(LastIndex)+","+str(EmpSal)+",\""+str(EmpSalDateS)+"\",1)";
			#Index.execute(SqlScript,(LastIndex,EmpSal,EmpSalDateS,1));
			
			Conn.ExecQuery(SqlScript);
			
			Conn.Save();
			Conn.CloseConnection();
			
			#nothing to see heir, just taking out my garbages
			EmpName = None;
			BDay = None;
			EmpCity = None;
			EmpCivilCode = None;
			EmpAvail = None;
			EmpDep = None;
			EmpSal = None;
			EmpSalDateS = None;
			LastIndex = None;
			SqlQuery = None;
			
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();