from .__init__ import *

def SetCompany(CompID, CompName, CompLoc, CompLocI):

    try:

        Conn = DatabaseQuery(PREFIX + DATABASE, 0);

        SqlScript=" \
        UPDATE \
        "+PREFIX+"CMCompInf \
        \
        SET \
        CMCompName = \""+str(CompName)+"\", \
        CMLocation = \""+str(CompLoc)+"\", \
        CMLocInterest = "+str(CompLocI)+" \
        \
        WHERE \
        "+PREFIX+"CMCompInf.CMCompID = "+str(CompID)+";";

        Conn.ExecQuery(SqlScript);

        Conn.Save();
        Conn.CloseConnection();

        Conn = None;
        SqlScript = None;

    except Exception as Error:

        Handle = ErrorHandle("ErrorLog/Log.txt", "a");

        Handle.SaveErrorToLogNoComment(Error);

        Handle.CloseStream();


def SetCompanyIsActive(CompID, switch):

    try:

        Conn = DatabaseQuery(PREFIX + DATABASE, 0);

        SqlScript=" \
        UPDATE \
        "+PREFIX+"CMComp \
        \
        SET \
        CMActiv = "+str(switch)+" \
        \
        WHERE \
        "+PREFIX+"CMComp.CMCompID = "+str(CompID)+";";

        Conn.ExecQuery(SqlScript);

        Conn.Save();
        Conn.CloseConnection();

        Conn = None;
        SqlScript = None;

    except Exception as Error:

        Handle = ErrorHandle("ErrorLog/Log.txt", "a");

        Handle.SaveErrorToLogNoComment(Error);

        Handle.CloseStream();
