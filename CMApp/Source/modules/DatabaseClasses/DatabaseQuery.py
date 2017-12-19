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

	def ExecQueryToRow(self):
		self.Index.execute(self.SqlScript);
		
		return self.Index.fetchall();
		
	def GetLastRowID(self):
		return self.Index.lastrowid;
		
	def SetSqlScript(self,SqlScript):
		self.SqlScript = SqlScript;
	
	def GetSqlScript(self):
		return SqlScript;