from .__init__ import *

def GetTaskList(RowType):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript = " \
		SELECT \
		"+PREFIX+"CMTaskInf.CMTaskID, \
		"+PREFIX+"CMTask.CMProjID, \
		"+PREFIX+"CMTaskInf.CMDateC, \
		"+PREFIX+"CMTaskInf.CMName, \
		"+PREFIX+"CMTaskInf.CMMonth, \
		"+PREFIX+"CMTaskInf.CMPos, \
		"+PREFIX+"CMTaskInf.CMNorm, \
		"+PREFIX+"CMTaskInf.CMNeg, \
		"+PREFIX+"CMTaskInf.CMVar, \
		"+PREFIX+"CMTaskInf.CMExp \
		\
		FROM \
		"+PREFIX+"CMTaskInf, \
		"+PREFIX+"CMTask \
		WHERE \
		("+PREFIX+"CMTaskInf.CMTaskID = "+PREFIX+"CMTask.CMTaskID) \
		AND \
		("+PREFIX+"CMTask.CMTaskID = "+PREFIX+"CMTaskInf.CMTaskID)\
		AND \
		("+PREFIX+"CMTask.CMActiv = 1);";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;

def GetTaskByID(TaskID, RowType):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript = " \
		SELECT \
		"+PREFIX+"CMTaskInf.CMTaskID, \
		"+PREFIX+"CMTask.CMProjID, \
		"+PREFIX+"CMTaskInf.CMDateC, \
		"+PREFIX+"CMTaskInf.CMName, \
		"+PREFIX+"CMTaskInf.CMMonth, \
		"+PREFIX+"CMTaskInf.CMPos, \
		"+PREFIX+"CMTaskInf.CMNorm, \
		"+PREFIX+"CMTaskInf.CMNeg, \
		"+PREFIX+"CMTaskInf.CMVar, \
		"+PREFIX+"CMTaskInf.CMExp \
		\
		FROM \
		"+PREFIX+"CMTaskInf, \
		"+PREFIX+"CMTask \
		WHERE \
		("+PREFIX+"CMTaskInf.CMTaskID = "+str(TaskID)+") \
		AND \
		("+PREFIX+"CMTask.CMTaskID = "+PREFIX+"CMTaskInf.CMTaskID)\
		AND \
		("+PREFIX+"CMTaskInf.CMActiv = 1);";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;

def GetProjectTask(ProjectID, RowType):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript = " \
		SELECT \
		"+PREFIX+"CMTaskInf.CMTaskID, \
		"+PREFIX+"CMTask.CMProjID, \
		"+PREFIX+"CMTaskInf.CMName, \
		"+PREFIX+"CMTaskInf.CMPos, \
		"+PREFIX+"CMTaskInf.CMNorm, \
		"+PREFIX+"CMTaskInf.CMNeg, \
		"+PREFIX+"CMTaskInf.CMExp, \
		"+PREFIX+"CMTaskInf.CMMonth, \
		"+PREFIX+"CMTaskInf.CMDateC, \
		"+PREFIX+"CMTaskInf.CMVar \
		\
		FROM \
		"+PREFIX+"CMTaskInf, \
		"+PREFIX+"CMProj, \
		"+PREFIX+"CMTask \
		\
		WHERE \
		("+PREFIX+"CMTask.CMProjID = "+PREFIX+"CMProj.CMProjID) \
		AND \
		("+PREFIX+"CMTask.CMTaskID = "+PREFIX+"CMTaskInf.CMTaskID) \
		AND \
		("+PREFIX+"CMTask.CMProjID = "+str(ProjectID)+") \
		AND \
		("+PREFIX+"CMTask.CMActiv = 1);";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return redirect(url_for("Index"), code=303);

def GetProjectTaskDep(ProjectID, RowType):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript=" \
		SELECT \
		"+PREFIX+"CMTaskDep.CMTaskID, \
		"+PREFIX+"CMTaskDep.CMDep\
				\
		FROM \
		"+PREFIX+"CMTaskDep, \
		"+PREFIX+"CMTask\
				\
		WHERE \
		("+PREFIX+"CMTaskDep.CMTaskID = "+PREFIX+"CMTask.CMTaskID) \
		AND \
		("+PREFIX+"CMTask.CMProjID = "+str(ProjectID)+") \
		AND \
		("+PREFIX+"CMTask.CMActiv = 1) \
		ORDER BY "+PREFIX+"CMTaskDep.CMDep DESC;";



		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;

def GetTaskDepByID(TaskID, RowType):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript =" \
		SELECT \
		"+PREFIX+"CMTaskDep.CMTaskID, \
		"+PREFIX+"CMTaskDep.CMDep \
		\
		FROM \
		"+PREFIX+"CMTaskDep \
		\
		WHERE \
		("+PREFIX+"CMTaskDep.CMTaskID = "+str(TaskID)+") \
		AND \
		("+PREFIX+"CMTaskDep.CMActiv = 1);";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;

def GetTaskDepList(RowType):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript =" \
		SELECT \
		"+PREFIX+"CMTaskDep.CMTaskID, \
		"+PREFIX+"CMTaskDep.CMDep \
		\
		FROM \
		"+PREFIX+"CMTaskDep \
		\
		WHERE \
		("+PREFIX+"CMTaskDep.CMActiv = 1);";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;
