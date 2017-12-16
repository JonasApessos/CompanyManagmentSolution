from . import *

def GetEmpRowData():
	
	Conn = sqlite3.connection(Prefix + Database);
	Conn.row_factory = sqlite3.Row;
	
	Index = Conn.cursor();
	
	SqlScript = " \
	SELECT \
	"+Prefix+"CMEmp.CMEmpID, \
	"+Prefix+"CMEmpInf.CMAvail, \
	"+Prefix+"CMEmpInf.CMBirthDate, \
	"+Prefix+"CMEmpInf.CMCity, \
	"+Prefix+"CMEmpInf.CMCivCode, \
	"+Prefix+"CMEmpInf.CMEmpName, \
	"+Prefix+"CMEmpSal.CMDateC, \
	"+Prefix+"CMEmpSal.CMIncome \
	\
	FROM \
	"+Prefix+"CMEmp, \
	"+Prefix+"CMEmpInf, \
	"+Prefix+"CMEmpSal, \
	"+Prefix+"CMDep \
	\
	WHERE \
	("+Prefix+"CMEmp.CMEmpID = "+Prefix+"CMEmpInf.CMEmpID \
	AND "+Prefix+"CMEmpInf.CMEmpID = "+Prefix+"CMEmpSal.CMEmpID) \
	AND ("+Prefix+"CMEmp.CMDepID = "+Prefix+"CMDep.CMDepID);";
	
	Index = Conn.execute(SqlScript);
	
	Rows = Index.fetchall();
	
	Conn = 0;
	Index = 0;
	SqlScript = 0;
	
	return Rows;
	