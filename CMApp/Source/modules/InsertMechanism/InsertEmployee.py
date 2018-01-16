from .__init__ import *

def IEmployee(EmpName, BDay, EmpCity, EmpCivilCode, EmpAvail, EmpDep, EmpSal, EmpSalDateS):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, 0);


		#Queries
		LastIndex = 0;
		SqlScript = "";

		SqlScript = "INSERT INTO " + PREFIX + "CMEmp(CMDepID,CMActiv) \
		VALUES \
		("+str(EmpDep)+",1)";
		#Index.execute(SqlScript,(EmpDep,1));

		Conn.ExecQuery(SqlScript);

		LastIndex = Conn.GetLastRowID();

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
		LastIndex = None;
		SqlQuery = None;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();
