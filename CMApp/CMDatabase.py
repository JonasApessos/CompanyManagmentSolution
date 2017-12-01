import sqlite3

try:

	prefix = "RE1201";
	prefix += "_";

	conn = sqlite3.connect(prefix + "CompanyManagmentDB.db");

#------------------<DROP TABLES>------------------

	SqlScript = "DROP TABLE IF EXISTS " + prefix + "CMContrInf;";
#conn.execute(SqlScript);

	SqlScript += "DROP TABLE IF EXISTS " + prefix + "CMCompInf;";
#conn.execute(SqlScript);

	SqlScript += "DROP TABLE IF EXISTS " + prefix + "CMContr;";
#conn.execute(SqlScript);

	SqlScript += "DROP TABLE IF EXISTS " + prefix + "CMComp;";
#conn.execute(SqlScript);

	SqlScript += "DROP TABLE IF EXISTS " + prefix + "CMProj;";
#conn.execute(SqlScript);

	SqlScript += "DROP TABLE IF EXISTS " + prefix + "CMTaskInf;";
#conn.execute(SqlScript);

	SqlScript += "DROP TABLE IF EXISTS " + prefix + "CMTask;";
#conn.execute(SqlScript);

	SqlScript += "DROP TABLE IF EXISTS " + prefix + "CMEmpSal;";
#conn.execute(SqlScript);

	SqlScript += "DROP TABLE IF EXISTS " + prefix + "CMEmpInf;";
#conn.execute(SqlScript);

	SqlScript += "DROP TABLE IF EXISTS " + prefix + "CMDep;";
#conn.execute(SqlScript);

	SqlScript += "DROP TABLE IF EXISTS " + prefix + "CMDepInf;";
#conn.execute(SqlScript);

	SqlScript += "DROP TABLE IF EXISTS " + prefix + "CMEmp;";
#conn.execute(SqlScript);

	SqlScript += "DROP TABLE IF EXISTS " + prefix + "CMEmpUnav;";
#conn.execute(SqlScript);

	SqlScript += "DROP TABLE IF EXISTS " + prefix + "CMEmpAssigTask;";
#conn.execute(SqlScript);
	conn.executescript(SqlScript);

#------------------<CREATE TABLES>------------------

	SqlScript = "CREATE TABLE IF NOT EXISTS " + prefix + "CMContrInf(CMContrInfID INTEGER PRIMARY KEY AUTOINCREMENT,CMContractor TEXT NOT NULL DEFAULT 'MISSING FIELD',CMDueDate DATE NOT NULL,CMAdvPay REAL NOT NULL DEFAULT 0,CMContrPay REAL NOT NULL DEFAULT 0,CMDateS DATE NOT NULL DEFAULT (DATETIME('now')),CMProdName TEXT NOT NULL DEFAULT 'MISSING FIELD');";
#conn.execute(SqlScript);

	SqlScript += "CREATE TABLE IF NOT EXISTS " + prefix + "CMCompInf(CMCompInfID INTEGER PRIMARY KEY AUTOINCREMENT,CMCompName TEXT NOT NULL DEFAULT 'MISSING FIELD',CMDateC DATE NOT NULL DEFAULT (DATETIME('now')),CMLocation TEXT NOT NULL DEFAULT 'MISSING FIELD',CMLocInterest REAL NOT NULL DEFAULT 0.0);";
#conn.execute(SqlScript);

	SqlScript += "CREATE TABLE IF NOT EXISTS " + prefix + "CMContr(CMContrID INTEGER PRIMARY KEY AUTOINCREMENT,CMContrInfID INTEGER,FOREIGN KEY(CMContrInfID) REFERENCES " + prefix + "CMContrInf(CMContrInfID));";
#conn.execute(SqlScript);

	SqlScript += "CREATE TABLE IF NOT EXISTS " + prefix + "CMComp(CMCompID INTEGER PRIMARY KEY AUTOINCREMENT,CMCompInfID INTEGER,FOREIGN KEY(CMCompInfID) REFERENCES " + prefix + "CMCompInf(CMCompInfID));";
#conn.execute(SqlScript);

	SqlScript += "CREATE TABLE IF NOT EXISTS " + prefix + "CMProj(CMProjID INTEGER PRIMARY KEY AUTOINCREMENT,CMContrID INTEGER,CMCompID INTEGER,FOREIGN KEY(CMContrID) REFERENCES " + prefix + "CMContr(CMContrID),FOREIGN KEY(CMCompID) REFERENCES " + prefix + "CMComp(CMCompID));";
#conn.execute(SqlScript);

	SqlScript += "CREATE TABLE IF NOT EXISTS " + prefix + "CMTaskInf(CMTaskInfID INTEGER PRIMARY KEY AUTOINCREMENT, CMName TEXT NOT NULL DEFAULT 'MISSING FIELD',CMPos INTEGER NOT NULL DEFAULT 0,CMNeg INTEGER NOT NULL DEFAULT 0,CMNorm INTEGER NOT NULL DEFAULT 0,CMExp REAL NOT NULL DEFAULT 0,CMVar REAL NOT NULL DEFAULT 0,CMMonth INTEGER NOT NULL DEFAULT 0,CMDateC DATE NOT NULL DEFAULT (DATETIME('now')));";
#conn.execute(SqlScript);

	SqlScript += "CREATE TABLE IF NOT EXISTS " + prefix + "CMTask(CMTaskID INTEGER PRIMARY KEY AUTOINCREMENT,CMTaskInfID INTEGER,CMProjID INTEGER,FOREIGN KEY(CMTaskInfID) REFERENCES " + prefix + "CMTaskInf(CMTaskInfID),FOREIGN KEY(CMProjID) REFERENCES " + prefix + "CMProj(CMProjID));";
#conn.execute(SqlScript);

	SqlScript += "CREATE TABLE IF NOT EXISTS " + prefix + "CMEmpSal(CMEmpSalID INTEGER PRIMARY KEY AUTOINCREMENT,CMIncome REAL NOT NULL DEFAULT 0,CMDate DATE NOT NULL);";
#conn.execute(SqlScript);

	SqlScript += "CREATE TABLE IF NOT EXISTS " + prefix + "CMEmpInf(CMEmpInfID INTEGER PRIMARY KEY AUTOINCREMENT,CMEmpSalID INTEGER,CMEmpName TEXT NOT NULL DEFAULT 'MISSING FIELD',CMBirthDate DATE NOT NULL,CMCity TEXT NOT NULL DEFAULT 'MISSING FIELD',CMCivCode TEXT NOT NULL,CMAvail REAL NOT NULL DEFAULT 0.0,FOREIGN KEY(CMEmpSalID) REFERENCES " + prefix + "CMEmpSal(CMEmpSalID));";
#conn.execute(SqlScript);

	SqlScript += "CREATE TABLE IF NOT EXISTS " + prefix + "CMDep(CMDepID INTEGER PRIMARY KEY AUTOINCREMENT);";
#conn.execute(SqlScript);

	SqlScript += "CREATE TABLE IF NOT EXISTS " + prefix + "CMDepInf(CMDepInfID INTEGER PRIMARY KEY AUTOINCREMENT,CMDepID INTEGER,CMProjID INTEGER,CMName TEXT NOT NULL DEFAULT 'MISSING FIELD',CMDateC DATE NOT NULL DEFAULT (DATETIME('now')),FOREIGN KEY(CMDepID) REFERENCES " + prefix + "CMDep(CMDepID),FOREIGN KEY(CMProjID) REFERENCES " + prefix + "CMProj(CMProjID));";
#conn.execute(SqlScript);

	SqlScript += "CREATE TABLE IF NOT EXISTS " + prefix + "CMEmp(CMEmpID INTEGER PRIMARY KEY AUTOINCREMENT,CMEmpInfID INTEGER,CMDepID INTEGER,FOREIGN KEY(CMEmpInfID) REFERENCES " + prefix + "CMEmpInf(CMEmpInfID),FOREIGN KEY(CMDepID) REFERENCES " + prefix + "CMDep(CMDepID));";
#conn.execute(SqlScript);

	SqlScript += "CREATE TABLE IF NOT EXISTS " + prefix + "CMEmpUnav(CMEmpUnavID INTEGER PRIMARY KEY AUTOINCREMENT,CMEmpID INTEGER,CMDateS DATE NOT NULL DEFAULT (DATETIME('now')),CMDateE DATETIME NOT NULL DEFAULT (DATETIME('now')),FOREIGN KEY(CMEmpID) REFERENCES " + prefix + "CMEmp(CMEmpID));";
#conn.execute(SqlScript);

	SqlScript += "CREATE TABLE IF NOT EXISTS " + prefix + "CMEmpAssigTask(CMEmpAssigTask INTEGER PRIMARY KEY AUTOINCREMENT,CMEmpID INTEGER,CMTaskID INTEGER,FOREIGN KEY(CMEmpID) REFERENCES " + prefix + "CMEmp(CMEmpID),FOREIGN KEY(CMTaskID) REFERENCES " + prefix + 	"CMTask(CMTaskID));";
#conn.execute(SqlScript);

	conn.executescript(SqlScript);

	conn.commit();
	conn.close();
	
	prefix = None;
	SqlScript = None;
	conn = None;

	print("\nDatabase successfully installed!........i hope......");

except:
	print("An error has accured during installation");