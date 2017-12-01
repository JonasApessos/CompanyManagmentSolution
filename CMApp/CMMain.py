import os
import sqlite3
from flask import *

prefix = "RE1201";
prefix += "_" ;
	
app = Flask(__name__);

@app.route("/")
def index():
	conn = sqlite3.connect(prefix + "CompanyManagmentDB.db");

	index = conn.cursor();

	index.execute("INSERT INTO " + prefix + "CMContrInf(CMContractor,CMDueDate,CMAdvPay,CMContrPay,CMDateS,CMProdName) VALUES('Microsoft','16/10/2011',5000.0,10000.0,'10/5/2010','Visual Studio'),('Oracle','29/7/2015',10000.0,20000.0,'15/10/2012','Java EE 2.1')");

	conn.commit();
	conn.close();
	return render_template("test.html");

@app.route("/test")
def test():
	conn = sqlite3.connect(prefix + "CompanyManagmentDB.db");

	conn.row_factory = sqlite3.Row;

	index = conn.cursor();
	index.execute("SELECT * FROM " + prefix + "CMContrInf");

	rows = index.fetchall();
	
	return render_template("index.html",rows = rows);


if __name__ == '__main__':
	app.run(debug = True);
