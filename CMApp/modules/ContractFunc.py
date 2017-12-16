from . import *

from modules.InsertMechanism.InsertContract import IContract

#//=======================<Contract Functions>=======================//

def ContrForm():

	#render html
	return render_template("Forms/ContractForm.html");
ContrB.add_url_rule("/Forms/ContractForm","ContrForm",ContrForm);
	
def Contract():

	IContract();

	return redirect(url_for("contrb.ContractForm"), code=302);
ContrB.add_url_rule("/Forms/ContractForm","Contract",Contract,methods=["POST"]);