import sqlite3

Prefix = "RE1201";
Prefix += "_";

Conn = sqlite3.connect(Prefix + "CompanyManagmentDB.db");

#------------------<DROP TABLES>------------------

SqlScript = "DROP TABLE IF EXISTS " + Prefix + "CMContrInf;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMCompInf;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMContr;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMComp;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMProj;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMTask;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMTaskInf;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMTaskDep;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMEmpSal;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMEmpInf;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMDep;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMDepInf;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMEmp;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMEmpUnav;";
#conn.execute(SqlScript);

SqlScript += "DROP TABLE IF EXISTS " + Prefix + "CMEmpAssigTask;";
#conn.execute(SqlScript);
Conn.executescript(SqlScript);

#------------------<CREATE TABLES>------------------
#Contract
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMContr \
( \
	CMContrID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMActiv INTEGERS NOT NULL DEFAULT 0 \
);";
Conn.execute(SqlScript);

#Company
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMComp \
( \
	CMCompID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMActiv INTEGERS NOT NULL DEFAULT 0 \
);";
Conn.execute(SqlScript);

#Contract Information
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMContrInf \
( \
	CMContrInfID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMContrID INTEGER, \
	CMContractor TEXT NOT NULL DEFAULT 'MISSING FIELD', \
	CMDueDate DATE NOT NULL, \
	CMAdvPay REAL NOT NULL DEFAULT 0.0, \
	CMContrPay REAL NOT NULL DEFAULT 0.0, \
	CMDateS DATETIME NOT NULL DEFAULT (DATETIME('now')), \
	CMDateC DATE NOT NULL DEFAULT (DATE('now')), \
	CMProdName TEXT NOT NULL DEFAULT 'MISSING FIELD', \
	CMActiv INTEGERS NOT NULL DEFAULT 0, \
	FOREIGN KEY(CMContrID) REFERENCES " + Prefix + "CMContr(CMContrID) \
);";
Conn.execute(SqlScript);

#Company Information
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMCompInf \
( \
	CMCompInfID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMCompID INTEGER, \
	CMCompName TEXT NOT NULL DEFAULT 'MISSING FIELD', \
	CMDateC DATE NOT NULL DEFAULT (DATE('now')), \
	CMLocation TEXT NOT NULL DEFAULT 'MISSING FIELD', \
	CMLocInterest REAL NOT NULL DEFAULT 0.0, \
	CMActiv INTEGERS NOT NULL DEFAULT 0, \
	FOREIGN KEY(CMCompID) REFERENCES " + Prefix + "CMComp(CMCompID) \
);";
Conn.execute(SqlScript);

#Project
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMProj \
( \
	CMProjID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMContrID INTEGER, \
	CMDepID INTEGER, \
	CMCompID INTEGER, \
	CMActiv INTEGERS NOT NULL DEFAULT 0, \
	CMDateC DATE NOT NULL DEFAULT (DATE('now')), \
	FOREIGN KEY(CMContrID) REFERENCES " + Prefix + "CMContr(CMContrID), \
	FOREIGN KEY(CMDepID) REFERENCES " + Prefix + "CMDep(CMDepID), \
	FOREIGN KEY(CMCompID) REFERENCES " + Prefix + "CMComp(CMCompID) \
);";
Conn.execute(SqlScript);

#Task
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMTask \
( \
	CMTaskID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMProjID INTEGER, \
	CMActiv INTEGERS NOT NULL DEFAULT 0, \
	FOREIGN KEY(CMProjID) REFERENCES " + Prefix + "CMProj(CMProjID) \
);";
Conn.execute(SqlScript);

#Task Information
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMTaskInf \
( \
	CMTaskInfID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMTaskID INTEGER, \
	CMName TEXT NOT NULL DEFAULT 'MISSING FIELD', \
	CMPos INTEGER NOT NULL DEFAULT 0, \
	CMNeg INTEGER NOT NULL DEFAULT 0, \
	CMNorm INTEGER NOT NULL DEFAULT 0, \
	CMExp REAL NOT NULL DEFAULT 0, \
	CMVar REAL NOT NULL DEFAULT 0, \
	CMMonth INTEGER NOT NULL DEFAULT 0, \
	CMActiv INTEGERS NOT NULL DEFAULT 0, \
	CMDateC DATE NOT NULL DEFAULT (DATE('now')), \
	FOREIGN KEY(CMTaskID) REFERENCES " + Prefix + "CMTask(CMTaskID) \
);";
Conn.execute(SqlScript);

#Task Dependencies
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMTaskDep \
( \
	CMTaskDepID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMTaskID INTEGER, \
	CMDep INTEGER DEFAULT NULL, \
	CMActiv INTEGERS NOT NULL DEFAULT 0, \
	FOREIGN KEY(CMTaskID) REFERENCES " + Prefix + "CMTask(CMTaskID) \
);";
Conn.execute(SqlScript);

#Department
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMDep \
( \
	CMDepID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMCompID INTEGER, \
	CMActiv INTEGERS NOT NULL DEFAULT 0, \
	FOREIGN KEY(CMCompID) REFERENCES " + Prefix + "CMComp(CMCompID) \
);";
Conn.execute(SqlScript);

#Department Information
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMDepInf \
( \
	CMDepInfID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMDepID INTEGER, \
	CMDepName TEXT NOT NULL DEFAULT 'MISSING FIELD', \
	CMDateC DATE NOT NULL DEFAULT (DATE('now')), \
	CMActiv INTEGERS NOT NULL DEFAULT 0, \
	FOREIGN KEY(CMDepID) REFERENCES " + Prefix + "CMDep(CMDepID) \
);";
Conn.execute(SqlScript);

#Employee
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMEmp \
( \
	CMEmpID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMDepID INTEGER, \
	CMDateC DATE NOT NULL DEFAULT (DATE('now')), \
	CMActiv INTEGERS NOT NULL DEFAULT 0, \
	FOREIGN KEY(CMDepID) REFERENCES " + Prefix + "CMDep(CMDepID) \
);";
Conn.execute(SqlScript);

#Employee Information
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMEmpInf \
( \
	CMEmpInfID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMEmpID INTEGER, \
	CMEmpName TEXT NOT NULL DEFAULT 'MISSING FIELD', \
	CMBirthDate DATE NOT NULL, \
	CMCity TEXT NOT NULL DEFAULT 'MISSING FIELD', \
	CMCivCode TEXT NOT NULL, \
	CMDateC DATE NOT NULL DEFAULT (DATE('now')), \
	CMAvail REAL NOT NULL DEFAULT 0.0, \
	CMActiv INTEGERS NOT NULL DEFAULT 0, \
	FOREIGN KEY(CMEmpID) REFERENCES " + Prefix + "CMEmp(CMEmpID) \
);";
Conn.execute(SqlScript);

#Employee Salary
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMEmpSal \
( \
	CMEmpSalID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMEmpID INTEGER, \
	CMIncome REAL NOT NULL DEFAULT 0, \
	CMDateC DATE NOT NULL, \
	CMActiv INTEGERS NOT NULL DEFAULT 0, \
	FOREIGN KEY(CMEmpID) REFERENCES " + Prefix + "CMEmp(CMEmpID)	\
);";
Conn.execute(SqlScript);

#Employee Unavailable
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMEmpUnav \
( \
	CMEmpUnavID INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMEmpID INTEGER, \
	CMDateS DATE NOT NULL DEFAULT (DATE('now')), \
	CMDateE DATE NOT NULL DEFAULT (DATE('now')), \
	CMActiv INTEGERS NOT NULL DEFAULT 0, \
	FOREIGN KEY(CMEmpID) REFERENCES " + Prefix + "CMEmp(CMEmpID) \
);";
Conn.execute(SqlScript);

#Employee Assigned Task
SqlScript = "CREATE TABLE IF NOT EXISTS " + Prefix + "CMEmpAssigTask \
( \
	CMEmpAssigTask INTEGER PRIMARY KEY AUTOINCREMENT, \
	CMEmpID INTEGER, \
	CMTaskID INTEGER, \
	CMDateC DATE NOT NULL, \
	CMActiv INTEGERS NOT NULL DEFAULT 0, \
	FOREIGN KEY(CMEmpID) REFERENCES " + Prefix + "CMEmp(CMEmpID), \
	FOREIGN KEY(CMTaskID) REFERENCES " + Prefix + 	"CMTask(CMTaskID) \
);";
Conn.execute(SqlScript);

#conn.executescript(SqlScript);

Conn.commit();


print("\nDatabase successfully installed!........i hope......");


print("\nInstall Sample Data?")
print("\n1.Yes",end=None);
print("\n0.No");

UserInput = int(input("\nAwaiting input: "));

if UserInput == 1:

	SqlScript = "INSERT INTO " + Prefix + "CMCompInf(CMCompID,CMCompName,CMDateC,CMLocation,CMLocInterest,CMActiv) \
	VALUES \
	(1,'Special Studio Vancouver','2017-10-16','Vancouver',5.0,1), \
	(2,'Special Studio New York','2016-07-06','New York',7.0,1), \
	(3,'Special Studio Hong Kong','2013-01-21','Hong Kong',14.0,1);";
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMComp(CMActiv) \
	VALUES \
	(1), \
	(1), \
	(1);";
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMContrInf(CMContrID,CMContractor,CMDueDate,CMAdvPay,CMContrPay,CMDateS,CMProdName,CMActiv) \
	VALUES \
	(1,'Microsoft','2014-06-16',5000.0,15000,'2014-02-01','Visual Studio 2015',1), \
	(2,'Ubisoft','2016-06-01',7300.0,25000,'2015-07-01','Far Cry 3',1), \
	(3,'Oracle','2018-04-01',5600.0,87000,'2017-09-30','Java EE 2.5',1);";
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMContr(CMActiv) \
	VALUES \
	(1), \
	(1), \
	(1);";
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMDepInf(CMDepID,CMDepName,CMDateC,CMActiv) \
	VALUES \
	(1,'Designers','2014-02-16',1), \
	(2,'Programmers','2015-07-01',1), \
	(3,'Artist','2017-04-06',1);";
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMDep(CMCompID,CMActiv) \
	VALUES \
	(1,1), \
	(2,1), \
	(2,1);";
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMEmpInf(CMEmpID,CMEmpName,CMBirthDate,CMCity,CMCivCode,CMAvail,CMActiv) \
	VALUES \
	(1,'Charles','1986-10-11','Denmark','123321',0.75,1), \
	(2,'Maria','1973-05-12','Canada','133421',1.0,1), \
	(3,'Caligula','1012-08-31','Rome','000666',1.0,1);";
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMEmpSal(CMEmpID,CMIncome,CMDateC,CMActiv) \
	VALUES \
	(1,1500,'2010-10-06',1), \
	(2,2500,'2011-09-13',1), \
	(3,1250,'2013-07-06',1);";
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMEmpUnav(CMEmpID,CMDateS,CMDateE,CMActiv) \
	VALUES \
	(3,'2015-01-11','2015-07-30',1);";
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMEmp(CMDepID,CMActiv) \
	VALUES \
	(1,1), \
	(2,1), \
	(3,1);";
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMProj(CMContrID,CMDepID,CMCompID,CMActiv) \
	VALUES \
	(1,1,2,1), \
	(2,2,3,1), \
	(3,3,1,1);";
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMTask(CMProjID,CMActiv) \
	VALUES \
	(1,1), \
	(1,1), \
	(1,1);";
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMTaskInf(CMTaskID,CMName,CMPos,CMNeg,CMNorm,CMExp,CMVar,CMMonth,CMActiv) \
	VALUES \
	(1,'TY1',30,120,60,"+str(((30 + (4 * 60) + 120)/6))+","+str(pow(((120-30)/6),2))+",2,1), \
	(2,'TY2',60,120,90,"+str(((60 + (4 * 90) + 120)/6))+","+str(pow(((120-60)/6),2))+",3,1), \
	(3,'TY3',90,150,120,"+str(((90 + (4 * 120) + 150)/6))+","+str(pow(((150-90)/6),2))+",4,1);"
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMTaskDep(CMTaskID,CMDep,CMActiv) \
	VALUES \
	(1,NULL,1), \
	(2,1,1), \
	(3,1,1), \
	(3,2,1);";
	Conn.execute(SqlScript);

	SqlScript = "INSERT INTO " + Prefix + "CMEmpAssigTask(CMEmpID,CMTaskID,CMDateC,CMActiv) \
	VALUES \
	(1,1,'2017-01-05',1), \
	(1,2,'2017-01-05',1), \
	(3,1,'2017-01-05',1);";
	Conn.execute(SqlScript);
	Conn.commit();

Conn.close();
Prefix = None;
SqlScript = None;
Conn = None;
