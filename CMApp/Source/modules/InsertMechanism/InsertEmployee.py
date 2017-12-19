from .__init__ import *

def IEmployee():
	if request.method == "POST":
		
		Conn = sqlite3.connect(PREFIX + DATABASE);
		Index = Conn.cursor();
		
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
		(?,?)";
		Index.execute(SqlScript,(EmpDep,1));
		
		SqlScript = "INSERT INTO " + PREFIX + "CMEmpInf(CMEmpID,CMEmpName,CMBirthDate,CMCity,CMCivCode,CMAvail,CMActiv) \
		VALUES \
		(?,?,?,?,?,?,?)";
		Index.execute(SqlScript,(LastIndex,EmpName,BDay,EmpCity,EmpCivilCode,EmpAvail,1));
		LastIndex = Index.lastrowid;
		
		SqlScript = "INSERT INTO " + PREFIX + "CMEmpSal(CMEmpID,CMIncome,CMDateC,CMActiv) \
		VALUES \
		(?,?,?,?)";
		Index.execute(SqlScript,(LastIndex,EmpSal,EmpSalDateS,1));
		
		Conn.commit();
		Conn.close();
		
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