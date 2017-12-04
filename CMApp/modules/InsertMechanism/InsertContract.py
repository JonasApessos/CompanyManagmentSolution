from flask import Flask, request, render_template
app = Flask(__name__);

@app.route("/Forms/ContractForm")
def ContrForm():

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

		
		SqlQuery = "INSERT INTO " + Prefix + "CMContrInf(CMContractor,CMDueDate,CMAdvPay,CMContrPay,CMDateS,CMProdName) VALUES(?,?,?,?,?,?);";
		
		Index.execute(SqlQuery,(Contr,DDate,APay,CPay,DateS,PName));
		
		LastIndex = Index.lastrowid;
		
		SqlQuery = "INSERT INTO " + Prefix + "CMContr(CMContrInfID) VALUES(?);";
		
		Index.execute(SqlQuery,(LastIndex,));
		
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
		
		return render_template("/Forms/ContractForm.html");
		
	else:
		return render_template("index.html");