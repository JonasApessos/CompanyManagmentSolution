from .DatabaseConnection import DatabaseConnectionBase

class DatabaseQuery(DatabaseConnectionBase):
	
	SqlScript = "";
	Index = None;
	
	def __init__(self,Prefix,Database):
		super().__init__(Prefix,Database);
		self.Index = super().GetIndex();
		
	def __del__(self):
		super().__del__();
		self.SqlScript = None;
	
	def ExecQuery(self):
		self.Index.execute(self.SqlScript);
		print("LASTROWID IN EXEC: " + str(self.Index.lastrowid));

	def ExecQueryToRow(self):
		self.Index.execute(self.SqlScript);
		
		return self.Index.fetchall();
		
	def GetLastRowID(self):
		print("LASTROWID IN GET: " + str(self.Index.lastrowid));
		return self.Index.lastrowid;
		
	def SetSqlScript(self,SqlScript):
		self.SqlScript = SqlScript;
	
	def GetSqlScript(self):
		return SqlScript;