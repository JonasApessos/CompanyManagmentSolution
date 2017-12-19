from .__init__ import *

def SetTask(TaskID,Name,Project,Pos,Norm,Neg,Month):
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
	Exp = (float(Pos) + (4 * float(Norm)) + float(Neg))/6;
	Var = ((float(Neg) - float(Pos))/6) ** 2;
	
	#Queries
	SqlScript = " \
	UPDATE "+PREFIX+"CMTaskInf \
	\
	SET \
	CMName = \""+str(Name)+"\", \
	CMPos = "+str(Pos)+", \
	CMNorm = "+str(Norm)+", \
	CMNeg = "+str(Neg)+", \
	CMMonth = "+str(Month)+", \
	CMExp = "+str(Exp)+", \
	CMVar = "+str(Var)+" \
	\
	WHERE \
	("+PREFIX+"CMTaskInf.CMTaskID = "+str(TaskID)+");";
	

	Conn.SetSqlScript(SqlScript);
	Conn.ExecQuery();
	
	SqlScript = " \
	UPDATE "+PREFIX+"CMTask \
	\
	SET \
	CMProjID = "+str(Project)+" \
	\
	WHERE \
	("+PREFIX+"CMTask.CMTaskID = "+TaskID+");";
	
	Conn.SetSqlScript(SqlScript);
	Conn.ExecQuery();
	
	Conn.Save();
	Conn.CloseDatabase();
	
def SetTaskIsActiv(TaskID, IsActiv):
	
	Conn = DatabaseQuery(PREFIX, DATABASE);
	
	#Queries
	SqlScript = " \
	UPDATE "+PREFIX+"CMTask \
	\
	SET\
	CMActiv = "+str(IsActiv)+" \
	\
	WHERE \
	("+PREFIX+"CMTask.CMTaskID = "+str(TaskID)+");";
	
	Conn.SetSqlScript(SqlScript);
	Conn.ExecQuery();
	
	Conn.Save();
	Conn.CloseDatabase();