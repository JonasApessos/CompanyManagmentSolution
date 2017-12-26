from .__init__ import *

def IContract():

	try:

		if request.method == "POST":
		
			Conn = DatabaseQuery(PREFIX + DATABASE, 0);
			
			LastIndex = 0;
			SqlScript = "";
			
			Contr = request.form["Contractor"];
			DDate = request.form["DueDate"];
			APay = request.form["AdvPay"];
			CPay = request.form["ContrPay"];
			DateS = request.form["DateS"];
			PName = request.form["ProdName"];

			
			SqlScript = "INSERT INTO " + PREFIX + "CMContr(CMActiv) \
			VALUES \
			(1);";
			
			Conn.ExecQuery(SqlScript);
			
			LastIndex = Conn.GetLastRowID();
			
			SqlScript = "INSERT INTO " + PREFIX + "CMContrInf(CMContrID,CMContractor,CMDueDate,CMAdvPay,CMContrPay,CMDateS,CMProdName,CMActiv) \
			VALUES \
			("+str(LastIndex)+",\""+str(Contr)+"\",\""+str(DDate)+"\","+str(APay)+","+str(CPay)+",\""+str(DateS)+"\",\""+str(PName)+"\",1);";
			
			Conn.ExecQuery(SqlScript);
			
			Conn.Save();
			Conn.CloseConnection();
			
			Conn = None;
			LastIndex = None;
			SqlScript = None;
			Contr = None;
			DDate = None;
			APay = None;
			CPay = None;
			DateS = None;
			PName = None;
			
	except Exception as Error:
	
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();