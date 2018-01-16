from .__init__ import *

def GetDepList(RowType):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript=" \
		SELECT \
		"+PREFIX+"CMTaskDep.CMTaskID, \
		"+PREFIX+"CMTaskDep.CMDep \
		\
		FROM \
		"+PREFIX+"CMTaskDep \
		\
		WHERE \
		("+PREFIX+"CMTaskDep.CMActiv = 1);"

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;

def GetDepProjListByID(RowType,ProjID):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript=" \
		SELECT \
		"+PREFIX+"CMTaskDep.CMTaskID, \
		"+PREFIX+"CMTaskDep.CMDep \
		\
		FROM \
		"+PREFIX+"CMTaskDep, \
		"+PREFIX+"CMTask \
		\
		WHERE \
		("+PREFIX+"CMTask.CMProjID = "+str(ProjID)+")\
		AND \
		("+PREFIX+"CMTask.CMTaskID = "+PREFIX+"CMTaskDep.CMTaskID) \
		AND \
		("+PREFIX+"CMTaskDep.CMActiv = 1);"

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;
