from .__init__ import *

def IProj(ContrID, CompID, DepID):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, 0);

		SqlScript = " \
		INSERT INTO \
		"+PREFIX+"CMProj(CMContrID,CMCompID,CMDepID,CMActiv) \
		\
		VALUES \
		("+str(ContrID)+","+str(CompID)+","+str(DepID)+",1);";

		Conn.ExecQuery(SqlScript);

		Conn.Save();
		Conn.CloseConnection();

		Conn = None;
		SqlScript = None;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();
