from modules import *

from modules.InsertMechanism.InsertCompany import ICompany

from modules.UpdateMechanism.SetCompany import SetCompany, SetCompanyIsActive

from modules.GetMechanism.GetCompany import GetCompanyList, GetCompanyListByID

#//=======================<Company Functions>=======================//

#The function that will render on entering the url
def CompForm():

	try:

		#render html
		return render_template("Forms/CompanyForm/CompanyForm.html");

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
CompB.add_url_rule("/Forms/CompanyForm","CompForm",CompForm);

#Set the company values in the database
def CompAdd():

	try:
		if request.method == "POST":
			CompName = str(request.form["CompName"]);
			Country = str(request.form["Country"]);
			IR = str(request.form["IR"]);

			ICompany(CompName, Country, IR);

		return redirect(url_for("compb.CompForm"), code=303);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
CompB.add_url_rule("/Forms/CompanyForm", "CompAdd", CompAdd, methods=["POST"]);

def CompEdit():

	try:
		if request.method == "POST":
			if "CompID" in session:

				CompanyRows = GetCompanyListByID(1,session['CompID'])

		return render_template("Forms/CompanyForm/CompanyEditForm.html", CompRows = CompanyRows, code=303);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
CompB.add_url_rule("/Forms/CompanyEdit", "CompEdit", CompEdit, methods=["POST"]);

def CompUpdate():

	try:
		if request.method == "POST":
			if "CompID" in session:
				CompName = request.form['CompName'];
				CompLoc = request.form['CompLoc'];
				CompLocI = request.form['CompLocI'];

				SetCompany(session['CompID'], CompName, CompLoc, CompLocI);

		return redirect(url_for("compb.CompEdit"),code=307);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
CompB.add_url_rule("/Forms/CompanyUpdate", "CompUpdate", CompUpdate, methods=["POST"]);

def CompDel():

	try:
		if request.method == "POST":
			if "CompID" in session:

				SetCompanyIsActive(session['CompID'], 0);

		return redirect(url_for("compb.Company"),code=303);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
CompB.add_url_rule("/Forms/CompanyDelete", "CompDel", CompDel, methods=["POST"]);

def CompanyLoad():
	try:

		if request.method == "POST":
			session['CompID'] = request.form['CompID'];
			if "Load" in request.form:
				return redirect(url_for("depb.Department"), code=303);
			if "Edit" in request.form:
				return redirect(url_for("compb.CompEdit"), code=307);
			elif "Del" in request.form:
				return redirect(url_for("compb.CompDel"), code=307);

		return render_template("DisplayData/CompanyOverview.html", code=303);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
CompB.add_url_rule("/Display/CompanyLoad", "CompanyLoad", CompanyLoad, methods=['POST']);

def Company():
	try:
		if "CompID" in session:
			session.pop("CompID", None);

		CompanyRows = GetCompanyList(1);

		return render_template("DisplayData/CompanyOverview.html", CompRows = CompanyRows, code=303);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html");
CompB.add_url_rule("/Display/CompanyOverview", "Company", Company);
