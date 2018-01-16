from .__init__ import *

def SetEmployee(EmpID, EmpName, EmpCity, EmpCivCode, EmpBDay, EmpIncome):

    try:

        Conn = DatabaseQuery(PREFIX + DATABASE, 0);

        SqlScript=" \
        UPDATE \
        "+PREFIX+"CMEmpInf \
        \
        SET \
        CMEmpName = \""+str(EmpName)+"\", \
        CMBirthDate = \""+str(EmpBDay)+"\", \
        CMCity = \""+str(EmpCity)+"\", \
        CMCivCode = \""+str(EmpCivCode)+"\" \
        \
        WHERE \
        "+PREFIX+"CMEmpInf.CMEmpID = "+str(EmpID)+";";

        Conn.ExecQuery(SqlScript);

        SqlScript=" \
        UPDATE \
        "+PREFIX+"CMEmpSal \
        \
        SET \
        CMIncome = "+str(EmpIncome)+" \
        \
        WHERE \
        "+PREFIX+"CMEmpSal.CMEmpID = "+str(EmpID)+";";

        Conn.ExecQuery(SqlScript);

        Conn.Save();
        Conn.CloseConnection();

        Conn = None;
        SqlScript = None;

    except Exception as Error:

        Handle = ErrorHandle("ErrorLog/Log.txt", "a");

        Handle.SaveErrorToLogNoComment(Error);

        Handle.CloseStream();


def SetEmployeeIsActive(EmpID,Switch):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, 0);

		SqlScript = " \
		UPDATE \
		"+PREFIX+"CMEmp \
		\
		SET \
		CMActiv = "+str(Switch)+" \
		\
		WHERE \
		("+PREFIX+"CMEmp.CMEmpID = "+str(EmpID)+");";

		Conn.ExecQuery(SqlScript);

		Conn.Save();
		Conn.CloseConnection();

		Conn = None;
		SqlScript = None;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();
