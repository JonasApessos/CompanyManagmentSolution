from modules import *

from modules.GetMechanism.GetEmpForm import GetFormDepartment
from modules.GetMechanism.GetEmployee import GetEmpList, GetEmpListByID

from modules.UpdateMechanism.SetEmployee import SetEmployee, SetEmployeeIsActive

from modules.InsertMechanism.InsertEmployee import IEmployee

#//=======================<Employee Functions>=======================//

#The function that will render on entering the url
def EmpForm():

	try:

		TableRows = GetFormDepartment(1);

		#render html with tuple data
		return render_template("Forms/EmployeeForm/EmpForm.html",rows = TableRows);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
EmpB.add_url_rule("/Forms/EmployeeForm","EmpForm",EmpForm);

#Set employee values in the database
def EmpAdd():

	try:

		if request.method == "POST":
		#Data from form
			EmpName = request.form["EmpName"];
			BDay = request.form["BDay"];
			EmpCity = request.form["EmpCity"];
			EmpCivilCode = request.form["EmpCivilCode"];
			EmpAvail = request.form["EmpAvail"];
			EmpDep = request.form["DepOption"];
			EmpSal = request.form["EmpSal"];
			EmpSalDateS = request.form["EmpSalDateS"];

			IEmployee(EmpName, BDay, EmpCity, EmpCivilCode, EmpAvail, EmpDep, EmpSal, EmpSalDateS);

			#render html
		return redirect(url_for("empb.EmpForm"), code=303);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
EmpB.add_url_rule("/Forms/EmployeeForm","EmpAdd",EmpAdd,methods = ["POST"]);

def EmpEdit():

	try:

		if request.method == "POST":
			if "EmpID" in session:

				EmployeeRows = GetEmpListByID(1,session['EmpID']);


		#render html
		return render_template("Forms/EmployeeForm/EmployeeEditForm.html", EmpRows = EmployeeRows, code=303);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
EmpB.add_url_rule("/Forms/EmployeeEdit","EmpEdit",EmpEdit,methods = ["POST"]);

def EmpUpdate():

	try:

		if request.method == "POST":
			if "EmpID" in session:

				EmpName = request.form['EmpName'];
				EmpCity = request.form['EmpCity'];
				EmpCivCode = request.form['EmpCivCode'];
				EmpBDate = request.form['EmpBDate'];
				EmpInc = request.form['EmpInc'];
				print("test");
				SetEmployee(session['EmpID'], EmpName, EmpCity, EmpCivCode, EmpBDate, EmpInc);


		#render html
		return redirect(url_for("empb.EmpEdit"), code=307);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
EmpB.add_url_rule("/Forms/EmployeeUpdate","EmpUpdate",EmpUpdate,methods = ["POST"]);

def EmpDel():

	try:
		print("0");
		if request.method == "POST":
			if "EmpID" in session:
				print("1");
				SetEmployeeIsActive(session['EmpID'], 0);


		#render html
		return redirect(url_for("empb.Employee"), code=303);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
EmpB.add_url_rule("/Forms/EmployeeDelete","EmpDel",EmpDel,methods = ["POST"]);

def EmployeeLoad():

	try:
		print("----");
		if request.method == "POST":
			session['EmpID'] = request.form['EmpID'];

			if "Edit" in request.form:
				print("edit");
				return redirect(url_for("empb.EmpEdit"), code=307);
			elif "Del" in request.form:
				print("del");
				return redirect(url_for("empb.EmpDel"), code=307);

		#render html
		return render_template("/DisplayData/Employee.html", code=303)

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
EmpB.add_url_rule("/Forms/EmployeeLoad", "EmployeeLoad", EmployeeLoad, methods=["POST"]);

def Employee():

	try:
		if "EmpID" in session:
			session.pop("EmpID", None);

		EmployeeRows = GetEmpList(1);

		#render html
		return render_template("/DisplayData/EmployeeOverview.html", EmpRows = EmployeeRows, code=303)

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
EmpB.add_url_rule("/Forms/EmployeeOverview", "Employee", Employee);
