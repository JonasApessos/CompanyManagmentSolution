from modules import *

from modules.InsertMechanism.InsertContract import IContract

from modules.UpdateMechanism.SetContract import SetContract, SetContractIsActive

from modules.GetMechanism.GetContract import GetContractList, GetContractListID

#//=======================<Contract Functions>=======================//

#The function that will render on entering the url
def ContrForm():

	try:

		#render html
		return render_template("Forms/ContractForm/ContractForm.html");

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html", code=303);
ContrB.add_url_rule("/Forms/ContractForm","ContrForm",ContrForm);

#Set the contract values in the database
def ContrAdd():

	try:

		IContract();

		return redirect(url_for("contrb.ContrForm"), code=303);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html", code=303);
ContrB.add_url_rule("/Forms/ContractForm","ContrAdd",ContrAdd,methods=["POST"]);

def ContrEdit():

	try:

		if request.method == "POST":

			if "ContrID" in session:
				ContractRows = None;

				ContractRows = GetContractListID(1,session['ContrID']);
				return render_template("Forms/ContractForm/ContractEditForm.html", ContrRows = ContractRows, code=303);

		return redirect(url_for("contrb.Contract"), code=303);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html", code=303);
ContrB.add_url_rule("/Forms/ContractEditForm","ContrEdit",ContrEdit,methods=["POST"]);

def ContrUpdate():

	try:
		if request.method == "POST":
			if "ContrID" in session:
				Contractor = request.form['Contractor'];
				ProdName = request.form['ProdName'];
				ContrPay = request.form['ContrPay'];
				ContrAdvPay = request.form['AdvPay'];
				DDate = request.form['DDate'];
				DStart = request.form['DStart'];


				SetContract(session['ContrID'], Contractor, ProdName, ContrPay, ContrAdvPay, DDate, DStart);

				return redirect(url_for('contrb.ContrEdit'), code=307);

		return redirect(url_for("contrb.Contract"), code=303);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html", code=303);
ContrB.add_url_rule("/Forms/ContractUpdate","ContrUpdate",ContrUpdate,methods=["POST"]);

def ContrDel():

	try:
		if request.method == "POST":
			if "ContrID" in session:
				SetContractIsActive(session['ContrID'], 0);

		return redirect(url_for("contrb.Contract"), code=303);
	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html", code=303);
ContrB.add_url_rule("/Forms/ContractDelete","ContrDel",ContrDel,methods=["POST"]);

def ContrLoad():

	try:

		if request.method == "POST":
			session['ContrID'] = request.form['ContrID'];
			if "Edit" in request.form:
				return redirect(url_for("contrb.ContrEdit"), code=307);
			elif "Del" in request.form:
				return redirect(url_for("contrb.ContrDel"), code=307);

		return redirect(url_for("contrb.ContractOverview"), code=303);
	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt", "a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html", code=303);
ContrB.add_url_rule("/Forms/ContractLoad", "ContrLoad", ContrLoad, methods=["POST"]);

def Contract():
	try:
		if "ContrID" in session:
			session.pop("ContrID", None);

		ContractRows = GetContractList(1);

		return render_template("DisplayData/ContractOverview.html", ContrRows = ContractRows, code=303);

	except Exception as Error:

		Handle = ErrorHandle("ErrorLog/Log.txt","a");

		Handle.SaveErrorToLogNoComment(Error);

		Handle.CloseStream();

		return render_template("ErrorIndex.html", code=303);
ContrB.add_url_rule("/Contract/ContractOverview","Contract",Contract);
