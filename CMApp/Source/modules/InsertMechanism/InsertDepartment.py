from . import *

def IDepartment(CompID, DepName):

	try:

		if request.method == "POST":

			Conn = DatabaseQuery(PREFIX + DATABASE, 0);

			LastIndex = 0;
			SqlScript = "";

			SqlScript = "INSERT INTO " + PREFIX + "CMDep(CMCompID,CMActiv) \
			VALUES \
			("+str(CompID)+",1);";

			Conn.ExecQuery(SqlScript);

			LastIndex = Conn.GetLastRowID();

			SqlScript = "INSERT INTO " + PREFIX + "CMDepInf(CMDepID,CMDepName,CMActiv) \
			VALUES \
			("+str(LastIndex)+",\""+str(DepName)+"\",1);";

			Conn.ExecQuery(SqlScript);

			Conn.Save();
			Conn.CloseConnection();

			Conn = None;
			LastIndex = None;
			SqlScript = None;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();
