from .__init__ import *

def GetEmpList(RowType):

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
		AND ("+PREFIX+"CMEmp.CMDepID = "+PREFIX+"CMDep.CMDepID) \
		AND ("+PREFIX+"CMEmp.CMActiv = 1);";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;


def GetEmpListByID(RowType,EmpID):

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
		AND ("+PREFIX+"CMEmp.CMDepID = "+PREFIX+"CMDep.CMDepID) \
		AND ("+PREFIX+"CMEmp.CMEmpID = "+str(EmpID)+");";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;
