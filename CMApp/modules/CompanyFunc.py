from . import *

from modules.InsertMechanism.InsertCompany import ICompany

#//=======================<Company Functions>=======================//

def CompForm():

	#render html
	return render_template("Forms/CompanyForm.html");
CompB.add_url_rule("/Forms/CompanyForm","CompForm",CompForm);

def Company():
	
	ICompany();
		
	return redirect(url_for("compb.CompForm"),code=302);
CompB.add_url_rule("/Forms/CompanyForm","Company",Company,methods=["POST"]);