from . import *

def GetEmpRowData():
	
	Conn = sqlite3.connection(PREFIX + DATABASE);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
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
	
	Index = Conn.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn = 0;
	Index = 0;
	SqlScript = 0;
	
	return Rows;
	