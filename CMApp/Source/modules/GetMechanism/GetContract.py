from .__init__ import *

def GetContractList(RowType):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript = " \
		SELECT \
		"+PREFIX+"CMContrInf.CMProdName, \
		"+PREFIX+"CMContrInf.CMContrID, \
		"+PREFIX+"CMContrInf.CMAdvPay, \
		"+PREFIX+"CMContrInf.CMContrPay, \
		"+PREFIX+"CMContrInf.CMDateS, \
		"+PREFIX+"CMContrInf.CMDueDate, \
		"+PREFIX+"CMContrInf.CMContractor \
		\
		FROM \
		"+PREFIX+"CMContrInf, \
		"+PREFIX+"CMContr \
		\
		WHERE \
		("+PREFIX+"CMContr.CMContrID = "+PREFIX+"CMContrInf.CMContrID) \
		AND \
		("+PREFIX+"CMContr.CMActiv = 1);";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;

def GetContractListByProjectID(RowType,ProjID):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript = " \
		SELECT \
		"+PREFIX+"CMContrInf.CMProdName, \
		"+PREFIX+"CMContrInf.CMContrID \
		\
		FROM \
		"+PREFIX+"CMContrInf, \
		"+PREFIX+"CMContr, \
		"+PREFIX+"CMProj \
		\
		WHERE \
		("+PREFIX+"CMContr.CMContrID = "+PREFIX+"CMContrInf.CMContrID) \
		AND \
		("+PREFIX+"CMProj.CMContrID = "+PREFIX+"CMContr.CMContrID) \
		AND \
		("+PREFIX+"CMProj.CMProjID = "+str(ProjID)+");";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;

def GetContractListID(RowType,ContrID):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, int(RowType));

		SqlScript = " \
		SELECT \
		"+PREFIX+"CMContrInf.CMProdName, \
		"+PREFIX+"CMContrInf.CMContrID, \
		"+PREFIX+"CMContrInf.CMContractor, \
		"+PREFIX+"CMContrInf.CMAdvPay, \
		"+PREFIX+"CMContrInf.CMContrPay, \
		"+PREFIX+"CMContrInf.CMDueDate, \
		"+PREFIX+"CMContrInf.CMDateS \
		\
		FROM \
		"+PREFIX+"CMContrInf \
		\
		WHERE \
		("+PREFIX+"CMContrInf.CMContrID = "+str(ContrID)+");";

		Rows = Conn.ExecQueryToRow(SqlScript);

		Conn.CloseConnection();

		return Rows;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return None;
