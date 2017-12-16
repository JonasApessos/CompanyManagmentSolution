from .__init__ import *

class DatabaseConnectionBase:
	
	Prefix = "";
	Database = "";
	Connection = None;
	
	def __init__(self,Prefix, Database):
		self.SetConnection(Prefix,Database);
	
	def __del__(self):
		#self.CloseDatabase();
		self.Prefix = None;
		self.Database = None;
		self.Connection = None;
	
	def Save(self):
		self.Connection.commit();
	
	def CloseDatabase(self):
		self.Connection.close();
		
	def SetConnection(self,Prefix, Database):
		self.SetPrefix(Prefix);
		self.SetDatabase(Database);
		self.Connection = sqlite3.connect(self.Prefix + self.Database);
		self.SetRowTypeToSql();
		
	def SetRowType(self,RowType):
		self.Connection.row_factory = RowType;
		
	def SetRowTypeToSql(self):
		self.Connection.row_factory = sqlite3.Row;
		
	def SetDatabase(self,Database):
		self.Database = Database;
		
	def SetPrefix(self,Prefix):
		self.Prefix = Prefix;

	def GetConnection(self):
		return Self.Connection
		
	def GetDatabase(self):
		return self.Database;
	
	def GetPrefix(self):
		return self.Prefix;
		
	def GetIndex(self):
		return self.Connection.cursor();

	