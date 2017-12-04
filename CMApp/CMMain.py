import os
import sqlite3
from flask import Flask, request, render_template


Database = "CompanyManagmentDB.db"
Prefix = "RE1201";
Prefix += "_" ;
	
app = Flask(__name__);


#//------------------<Testing Functions>------------------//
@app.route("/add")
def add():

	Conn = sqlite3.connect(Prefix + Database);

	Index = Conn.cursor();

	Index.execute("INSERT INTO " + Prefix + "CMDep(CMDepInfID) VALUES(1)");

	Conn.commit();
	Conn.close();
	
	#nothing to see heir, just taking out my garbages
	Conn = None;
	Index = None;
	
	return render_template("test.html");

@app.route("/test")
def test():

	Conn = sqlite3.connect(Prefix + Database);

	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	#Get data
	Index.execute("SELECT * FROM " + Prefix + "CMDep;");

	TableRows = Index.fetchall();
	
	Conn.close();
	
	#nothing to see heir, just taking out my garbages
	Conn = None;
	Index = None;
	
	#render html with tuple data
	return render_template("test2.html",rows = TableRows);

	
#//------------------<Index Functions>------------------//
@app.route("/")
def index():
	#render html
	return render_template("index.html");

	
#//------------------<Employee Functions>------------------//
@app.route("/Forms/EmployeeForm")
def EmpForm():

	Conn = sqlite3.connect(Prefix + Database);
	
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	#Get data
	SqlQuery = "SELECT " + Prefix + "CMDep.CMDepID, " + Prefix + "CMDepInf.CMName, " + Prefix + "CMCompInf.CMCompName \
	FROM " + Prefix + "CMDep, " + Prefix + "CMDepInf, " + Prefix + "CMCompInf, " + Prefix + "CMComp \
	WHERE (" + Prefix + "CMDep.CMDepInfID = " + Prefix + "CMDepInf.CMDepInfID) \
	AND (" + Prefix + "CMComp.CMCompInfID = " + Prefix + "CMCompInf.CMCompInfID) \
	AND (" + Prefix + "CMComp.CMCompID = " + Prefix + "CMDep.CMCompID);";
	
	Index.execute(SqlQuery);
	
	#get data from rows
	TableRows = Index.fetchall();
	
	Conn.close();
	
	#nothing to see heir, just taking out my garbages
	Conn = None;
	index = None;
	SqlQuery = None;
	
	#render html with tuple data
	return render_template("Forms/EmpForm.html",rows = TableRows);

@app.route("/Forms/EmployeeForm",methods=["POST"])
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
		
		SqlQuery = "INSERT INTO " + Prefix + "CMEmpInf(CMEmpName,CMBirthDate,CMCity,CMCivCode,CMAvail,CMActiv) \
		VALUES \
		(?,?,?,?,?,?)";
		Index.execute(SqlQuery,(EmpName,BDay,EmpCity,EmpCivilCode,EmpAvail,1));
		LastIndex = Index.lastrowid;
		
		SqlQuery = "INSERT INTO " + Prefix + "CMEmpSal(CMEmpInfID,CMIncome,CMDate,CMActiv) \
		VALUES \
		(?,?,?,?)";
		Index.execute(SqlQuery,(LastIndex,EmpSal,EmpSalDateS,1));
		
		SqlQuery = "INSERT INTO " + Prefix + "CMEmp(CMEmpInfID,CMDepID,CMActiv) \
		VALUES \
		(?,?,?)";
		Index.execute(SqlQuery,(LastIndex,EmpDep,1));
		
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
		
		#render html
		return render_template("index.html");

#//------------------<Task Functions>------------------//
@app.route("/Forms/TaskForm")
def TaskForm():

	Conn = sqlite3.connect(Prefix + Database);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	#Queries
	SqlScript = "SELECT " + Prefix + "CMContrInf.CMProdName, " + Prefix + "CMProj.CMProjID \
	FROM " + Prefix + "CMContrInf," + Prefix + "CMProj, " + Prefix + "CMContr \
	WHERE (" + Prefix + "CMProj.CMContrID = " + Prefix + "CMContr.CMContrID) \
	AND (" + Prefix + "CMContr.CMContrInfID = " + Prefix + "CMContrInf.CMContrInfID);";
	
	Index.execute(SqlScript);
	
	TableRows = Index.fetchall();
	
	Conn.close();
	
	
	#nothing to see heir, just taking out my garbages
	Conn = None;
	Index = None;
	SqlScript = None;
	
	#render html with tuple data
	return render_template("Forms/TaskForm.html",rows = TableRows);

@app.route("/Forms/TaskForm",methods=["POST"])
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
		
		SqlQuery = "INSERT INTO " + Prefix + "CMTaskInf(CMName,CMPos,CMNorm,CMNeg,CMExp,CMVar,CMMonth,CMDateC,CMActiv) \
		VALUES \
		(?,?,?,?,?,?,?,?,?)";
		
		Index.execute(SqlQuery,(TaskName,PosPre,NormPre,NegPre,Expected,Variance,Months,CDate,1));
		
		LastIndex = Index.lastrowid;
		
		SqlQuery = "INSERT INTO " + Prefix + "CMTask(CMTaskInfID,CMProjID,CMActiv) \
		VALUES \
		(?,?,?)";
		
		Index.execute(SqlQuery,(LastIndex,ProjOption,1));
		
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
		
		#render html
		return render_template("index.html");
	
#//------------------<Company Functions>------------------//
@app.route("/Forms/CompanyForm")
def CompForm():

	return render_template("Forms/CompanyForm.html");

@app.route("/Forms/CompanyForm",methods=["POST"])
def ICompany():
	
	if request.method == "POST":
		
		Conn = sqlite3.connect(Prefix + Database);
		Index = Conn.cursor();
		
		CompName = request.form["CompName"];
		CDate = request.form["CDate"];
		Country = request.form["Country"];
		IR = request.form["IR"];
		
		
		LastIndex = 0;
		SqlQuery = "";
		
		SqlQuery = "INSERT INTO " + Prefix + "CMCompInf(CMCompName,CMDateC,CMLocation,CMLocInterest) \
		VALUES \
		(?,?,?,?)";
		
		Index.execute(SqlQuery,(CompName,CDate,Country,IR));
		
		LastIndex = Index.lastrowid;
		
		SqlQuery = "INSERT INTO " + Prefix + "CMComp(CMCompInfID) \
		VALUES \
		(?)";
		
		Index.execute(SqlQuery,(LastIndex,));
		
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
		
		#render html
		return render_template("index.html");
		
		
	
#//------------------<Contract Functions>------------------//
@app.route("/Forms/ContractForm")
def ContrForm():
	#render html
	return render_template("Forms/ContractForm.html");
	
@app.route("/Forms/ContractForm", methods=["POST"])
def IContract():

	if request.method == "POST":
	
		Conn = sqlite3.connect(Prefix + Database);
		Index = Conn.cursor();

		
		LastIndex = 0;
		SqlQuery = "";
		
		Contr = request.form["Contractor"];
		DDate = request.form["DueDate"];
		APay = request.form["AdvPay"];
		CPay = request.form["ContrPay"];
		DateS = request.form["DateS"];
		PName = request.form["ProdName"];

		
		SqlQuery = "INSERT INTO " + Prefix + "CMContrInf(CMContractor,CMDueDate,CMAdvPay,CMContrPay,CMDateS,CMProdName) \
		VALUES \
		(?,?,?,?,?,?);";
		
		Index.execute(SqlQuery,(Contr,DDate,APay,CPay,DateS,PName));
		
		LastIndex = Index.lastrowid;
		
		SqlQuery = "INSERT INTO " + Prefix + "CMContr(CMContrInfID) \
		VALUES \
		(?);";
		
		Index.execute(SqlQuery,(LastIndex,));
		
		Conn.commit();
		Conn.close();
		
		#nothing to see heir, just taking out my garbages
		Conn = None;
		Index = None;
		LastIndex = None;
		SqlQuery = None;
		Contr = None;
		DDate = None;
		APay = None;
		CPay = None;
		DateS = None;
		PName = None;
		
		#render html
		return render_template("/Forms/ContractForm.html");
		
	else:
		
		#render html
		return render_template("index.html");
		
		

#//------------------<Main>------------------//
if __name__ == '__main__':

	app.run(debug = True,port=80);
