from .__init__ import *

def GetEmpRowData():
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
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
	
	Conn.SetSqlScript(SqlScript);
	
	Rows = Conn.ExecQueryToRow();
	
	Conn.CloseDatabase();
	
	return Rows;
	