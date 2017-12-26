from .DatabaseConnection import DatabaseConnectionBase

class DatabaseQuery(DatabaseConnectionBase):
	
	SqlScript = "";
	Index = None;
	
	def __init__(self, Database, RowType):
		super().__init__(Database, RowType);
		self.Index = super().GetIndex();
		
	def __del__(self):
		super().__del__();
		self.SqlScript = None;
		self.Index = None;
	
	def ExecQuery(self, SqlScript):
		self.SetSqlScript(SqlScript);
		self.Index.execute(SqlScript);

	def ExecQueryToRow(self, SqlScript):
		self.SetSqlScript(SqlScript);
		self.Index.execute(SqlScript);
		
		return self.Index.fetchall();
		
	def GetLastRowID(self):
		return self.Index.lastrowid;
		
	def SetSqlScript(self,SqlScript):
		self.SqlScript = SqlScript;
	
	def GetSqlScript(self):
		return self.SqlScript;