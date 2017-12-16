from . import *

def IEmployee():
	if request.method == "POST":
		
		Conn = sqlite3.connect(Prefix + Database);
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
		SqlQuery = "";
		
		SqlQuery = "INSERT INTO " + Prefix + "CMEmp(CMDepID,CMActiv) \
		VALUES \
		(?,?)";
		Index.execute(SqlQuery,(EmpDep,1));
		
		SqlQuery = "INSERT INTO " + Prefix + "CMEmpInf(CMEmpID,CMEmpName,CMBirthDate,CMCity,CMCivCode,CMAvail,CMActiv) \
		VALUES \
		(?,?,?,?,?,?,?)";
		Index.execute(SqlQuery,(LastIndex,EmpName,BDay,EmpCity,EmpCivilCode,EmpAvail,1));
		LastIndex = Index.lastrowid;
		
		SqlQuery = "INSERT INTO " + Prefix + "CMEmpSal(CMEmpID,CMIncome,CMDateC,CMActiv) \
		VALUES \
		(?,?,?,?)";
		Index.execute(SqlQuery,(LastIndex,EmpSal,EmpSalDateS,1));
		
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