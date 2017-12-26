from .__init__ import *

class DatabaseConnectionBase:
	
	Database = "";
	Connection = None;
	
	def __init__(self, Database, RowType):
		self.SetConnection(Database, RowType);
	
	def __del__(self):
		self.Database = None;
		self.Connection = None;
	
	def Save(self):
		self.Connection.commit();
	
	def CloseConnection(self):
		self.Connection.close();
		
	def SetConnection(self, Database, RowType):
		self.SetDatabase(Database);
		self.Connection = sqlite3.connect(self.Database);
		self.SetRowTypeToSql(RowType);
		
	def SetRowTypeToSql(self, RowType):
		if RowType == 1:
			self.Connection.row_factory = sqlite3.Row;
		
	def SetDatabase(self,Database):
		self.Database = Database;

	def GetConnection(self):
		return Self.Connection
		
	def GetDatabase(self):
		return self.Database;
	
	def GetPrefix(self):
		return self.Prefix;
		
	def GetIndex(self):
		return self.Connection.cursor();

	