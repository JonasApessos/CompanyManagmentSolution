from .__init__ import *

def GetEmpRowData(RowType):
	
	try:
	
		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));
		
		SqlScript = " \
		SELECT \
		"+PREFIX+"CMEmp.CMEmpID, \
		"+PREFIX+"CMEmpInf.CMAvail, \
		"+PREFIX+"CMEmpInf.CMBirthDate, \
		"+PREFIX+"CMEmpInf.CMCity, \
		"+PREFIX+"CMEmpInf.CMCivCode, \
		"+PREFIX+"CMEmpInf.CMEmpName, \
		"+PREFIX+"CMEmpSal.CMDateC, \
		"+PREFIX+"CMEmpSal.CMIncome \
		\
		FROM \
		"+PREFIX+"CMEmp, \
		"+PREFIX+"CMEmpInf, \
		"+PREFIX+"CMEmpSal, \
		"+PREFIX+"CMDep \
		\
		WHERE \
		("+PREFIX+"CMEmp.CMEmpID = "+PREFIX+"CMEmpInf.CMEmpID \
		AND "+PREFIX+"CMEmpInf.CMEmpID = "+PREFIX+"CMEmpSal.CMEmpID) \
		AND ("+PREFIX+"CMEmp.CMDepID = "+PREFIX+"CMDep.CMDepID);";
		
		Rows = Conn.ExecQueryToRow(SqlScript);
		
		Conn.CloseConnection();
		
		return Rows;
	
	except Exception as Error:
		
		Handle = ErrorHandle("ErrorLog/Log.txt", "a");
		
		Handle.SaveErrorToLog(Error, " -- function: "+str(inspect.stack()[0][3])+" , From file: " + str(inspect.stack()[0][1]));
		
		Handle.CloseStream();
		
		return None;