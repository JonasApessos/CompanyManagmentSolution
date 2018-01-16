from .__init__ import *

def SetContract(ContrID, Contractor, ProdName, ContrPay, AdvPay, DDate, DStart):

    try:

        Conn = DatabaseQuery(PREFIX + DATABASE, 0);

        SqlScript=" \
        UPDATE \
        "+PREFIX+"CMContrInf \
        \
        SET \
        CMProdName = \""+str(ProdName)+"\", \
        CMContractor = \""+str(Contractor)+"\", \
        CMContrPay = "+str(ContrPay)+", \
        CMAdvPay = "+str(AdvPay)+", \
        CMDueDate = \""+str(DDate)+"\", \
        CMDateS = \""+str(DStart)+"\" \
        \
        WHERE \
        "+PREFIX+"CMContrInf.CMContrID = "+str(ContrID)+";";

        Conn.ExecQuery(SqlScript);

        Conn.Save();
        Conn.CloseConnection();

        Conn = None;
        SqlScript = None;

    except Exception as Error:

        Handle = ErrorHandle("ErrorLog/Log.txt", "a");

        Handle.SaveErrorToLogNoComment(Error);

        Handle.CloseStream();

def SetContractIsActive(ContrID,Switch):

	try:

		Conn = DatabaseQuery(PREFIX + DATABASE, 0);

		SqlScript = " \
		UPDATE \
		"+PREFIX+"CMContr \
		\
		SET \
		CMActiv = "+str(Switch)+" \
		\
		WHERE \
		("+PREFIX+"CMContr.CMContrID = "+str(ContrID)+");";

		Conn.ExecQuery(SqlScript);

		Conn.Save();
		Conn.CloseConnection();

		Conn = None;
		SqlScript = None;

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();
