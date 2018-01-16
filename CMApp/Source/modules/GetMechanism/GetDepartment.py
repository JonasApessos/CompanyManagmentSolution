from .__init__ import *

def GetDepartmentList(RowType):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript = " \
		SELECT \
		"+PREFIX+"CMDepInf.CMDepID, \
		"+PREFIX+"CMDepInf.CMDepName, \
		"+PREFIX+"CMDepInf.CMDateC \
		\
		FROM \
		"+PREFIX+"CMDepInf, \
		"+PREFIX+"CMDep \
		\
		WHERE \
		("+PREFIX+"CMDepInf.CMDepID = "+PREFIX+"CMDep.CMDepID) \
		AND \
		("+PREFIX+"CMDep.CMActiv= 1);";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;

def GetDepartmentListByComp(CompID, RowType):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript = " \
		SELECT \
		"+PREFIX+"CMDepInf.CMDepID, \
		"+PREFIX+"CMDepInf.CMDepName, \
		"+PREFIX+"CMDepInf.CMDateC \
		\
		FROM \
		"+PREFIX+"CMDepInf, \
		"+PREFIX+"CMDep \
		\
		WHERE \
		("+PREFIX+"CMDepInf.CMDepID = "+PREFIX+"CMDep.CMDepID) \
		AND \
		("+PREFIX+"CMDep.CMCompID = "+str(CompID)+") \
		AND \
		("+PREFIX+"CMDep.CMActiv= 1);";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;

def GetDepartmentListByID(DepID, RowType):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript = " \
		SELECT \
		"+PREFIX+"CMDepInf.CMDepID, \
		"+PREFIX+"CMDepInf.CMDepName \
		\
		FROM \
		"+PREFIX+"CMDepInf \
		\
		WHERE \
		("+PREFIX+"CMDepInf.CMDepID = "+DepID+");";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;
