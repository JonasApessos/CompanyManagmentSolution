from .__init__ import *

def ICompany(CompName, Country, IR):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, 0);

		LastIndex = "";
		SqlScript = "";


		SqlScript = "INSERT INTO " + PREFIX + "CMComp(CMActiv) \
		VALUES \
		(1)";

		Conn.ExecQuery(SqlScript);

		LastIndex = str(Conn.GetLastRowID());

		SqlScript = "INSERT INTO " + PREFIX + "CMCompInf(CMCompID,CMCompName,CMLocation,CMLocInterest,CMActiv) \
		VALUES \
		("+str(LastIndex)+",\""+str(CompName)+"\",\""+str(Country)+"\","+str(IR)+",1)";

		Conn.ExecQuery(SqlScript);

		Conn.Save();
		Conn.CloseConnection();

		#nothing to see heir, just taking out my garbages
		LastIndex = None;
		SqlQuery = None;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();
