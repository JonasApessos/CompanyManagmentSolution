from . import *

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

		
		SqlQuery = "INSERT INTO " + Prefix + "CMContr(CMActiv) \
		VALUES \
		(?);";
		
		Index.execute(SqlQuery,(1,));
		
		LastIndex = Index.lastrowid;
		
		SqlQuery = "INSERT INTO " + Prefix + "CMContrInf(CMContrID,CMContractor,CMDueDate,CMAdvPay,CMContrPay,CMDateS,CMProdName,CMActiv) \
		VALUES \
		(?,?,?,?,?,?,?,?);";
		
		Index.execute(SqlQuery,(LastIndex,Contr,DDate,APay,CPay,DateS,PName,1));
		
		Conn.commit();
		Conn.close();
		
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