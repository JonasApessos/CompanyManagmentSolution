from .__init__ import *


def GetCompanyList(RowType):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript = " \
		SELECT \
		"+PREFIX+"CMCompInf.CMCompID, \
		"+PREFIX+"CMCompInf.CMCompName, \
		"+PREFIX+"CMCompInf.CMLocation, \
		"+PREFIX+"CMCompInf.CMLocInterest \
		\
		FROM \
		"+PREFIX+"CMCompInf, \
		"+PREFIX+"CMComp \
		\
		WHERE \
		("+PREFIX+"CMCompInf.CMCompID = "+PREFIX+"CMComp.CMCompID) \
		AND \
		("+PREFIX+"CMComp.CMActiv = 1);";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;


def GetCompanyListByID(RowType,CompID):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript = " \
		SELECT \
		"+PREFIX+"CMCompInf.CMCompID, \
		"+PREFIX+"CMCompInf.CMCompName, \
		"+PREFIX+"CMCompInf.CMLocation, \
		"+PREFIX+"CMCompInf.CMLocInterest \
		\
		FROM \
		"+PREFIX+"CMCompInf \
		\
		WHERE \
		("+PREFIX+"CMCompInf.CMCompID = "+str(CompID)+");";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;
