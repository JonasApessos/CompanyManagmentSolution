from .__init__ import *


def SetDepartment(DepID,DepName):

    try:

        Conn = DatabaseQuery(PREFIX + DATABASE, 0);

        SqlScript=" \
        UPDATE \
        "+PREFIX+"CMDepInf \
        \
        SET \
        CMDepName = \""+str(DepName)+"\" \
        \
        WHERE \
        "+PREFIX+"CMDepInf.CMDepID = "+str(DepID)+";";

        Conn.ExecQuery(SqlScript);

        Conn.Save();
        Conn.CloseConnection();

        Conn = None;
        SqlScript = None;

    except Exception as Error:

        Handle = ErrorHandle("ErrorLog/Log.txt", "a");

        Handle.SaveErrorToLogNoComment(Error);

        Handle.CloseStream();

def SetDepartmentIsActive(DepID, Switch):
    try:
        Conn = DatabaseQuery(PREFIX + DATABASE, 0);

        SqlScript = " \
        UPDATE \
        "+PREFIX+"CMDep \
        \
        SET \
        CMActiv = "+str(Switch)+" \
        \
        WHERE \
        ("+PREFIX+"CMDep.CMDepID = "+str(DepID)+");";

        Conn.ExecQuery(SqlScript);

        Conn.Save();
        Conn.CloseConnection();

        Conn = None;
        SqlScript = None;

    except Exception as Error:

        Handle = ErrorHandle("ErrorLog/Log.txt", "a");

        Handle.SaveErrorToLogNoComment(Error);

        Handle.CloseStream();
