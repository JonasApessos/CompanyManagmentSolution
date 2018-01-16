from modules import *

from modules.UpdateMechanism.SetDepartment import SetDepartment, SetDepartmentIsActive

from modules.GetMechanism.GetDepartment import GetDepartmentList, GetDepartmentListByComp

from modules.InsertMechanism.InsertDepartment import IDepartment

def DepDel():
    try:
        if request.method == "POST":

            if "DepID" in session:

                SetDepartmentIsActive(session['DepID'], 0);

        return redirect(url_for("depb.Department"));
    except Exception as Error:

        Handle = ErrorHandle("ErrorLog/Log.txt", "a");

        Handle.SaveErrorToLogNoComment(Error);

        Handle.CloseStream();

        return render_template("ErrorIndex.html");
DepB.add_url_rule("/DepartmentDelete","DepDel",DepDel,methods=["POST"]);

def DepEdit():

    try:
        if request.method == "POST":

            if "DepID" in session:

                DepartmentRows = GetDepartmentListByID(session['DepID'], 1);

                return render_template("Forms/DepartmentForm/DepartmentEditForm.html", DepRows = DepartmentRows);
        return redirect(url_for("depb.Department"), code=303);
    except Exception as Error:

        Handle = ErrorHandle("ErrorLog/Log.txt", "a");

        Handle.SaveErrorToLogNoComment(Error);

        Handle.CloseStream();

        return render_template("ErrorIndex.html");
DepB.add_url_rule("/DepartmentEdit","DepEdit",DepEdit,methods=["POST"]);

def DepUpdate():

    try:
        if request.method == "POST":

            if "DepID" in session:

                DepName = request.form['DepName'];

                SetDepartment(session['DepID'],DepName);

        return redirect(url_for("depb.DepEdit"), code=307);
    except Exception as Error:

        Handle = ErrorHandle("ErrorLog/Log.txt", "a");

        Handle.SaveErrorToLogNoComment(Error);

        Handle.CloseStream();

        return render_template("ErrorIndex.html");

DepB.add_url_rule("/DepartmentUpdate","DepUpdate",DepUpdate,methods=["POST"]);

def DepForm():
    try:
        return render_template("Forms/DepartmentForm/DepartmentForm.html", code=303);
    except Exception as Error:

        Handle = ErrorHandle("ErrorLog/Log.txt", "a");

        Handle.SaveErrorToLogNoComment(Error);

        Handle.CloseStream();

        return render_template("ErrorIndex.html");
DepB.add_url_rule("/DepartmentForm","DepForm",DepForm);

def DepAdd():

    try:
        if request.method == "POST":
            if "CompID" in session:
                print(session["CompID"]);
                DepName = request.form['DepName'];
                IDepartment(session["CompID"],DepName);

        return redirect(url_for("depb.DepForm"), code=303);
    except Exception as Error:

        Handle = ErrorHandle("ErrorLog/Log.txt", "a");

        Handle.SaveErrorToLogNoComment(Error);

        Handle.CloseStream();

        return render_template("ErrorIndex.html");
DepB.add_url_rule("/DepartmentAdd","DepAdd",DepAdd,methods=["POST"]);

def DepartmentLoad():

    try:
        if request.method == "POST":

            session['DepID'] = request.form['DepID'];

            if "Edit" in request.form:
                return redirect(url_for("depb.DepEdit"), code=307);
            elif "Del" in request.form:
                return redirect(url_for("depb.DepDel"), code=307);

        return redirect(url_for("depb.Department"), code=303);
    except Exception as Error:

        Handle = ErrorHandle("ErrorLog/Log.txt", "a");

        Handle.SaveErrorToLogNoComment(Error);

        Handle.CloseStream();

        return render_template("ErrorIndex.html");
DepB.add_url_rule("/DepartmentLoad","DepartmentLoad",DepartmentLoad,methods=["POST"]);

def Department():

    try:
        if "DepID" in session:
            session.pop("DepID", None);

        DepartmentsRows = GetDepartmentListByComp(session['CompID'],1);

        return render_template("DisplayData/DepartmentOverview.html", DepRows = DepartmentsRows);
    except Exception as Error:

        Handle = ErrorHandle("ErrorLog/Log.txt", "a");

        Handle.SaveErrorToLogNoComment(Error);

        Handle.CloseStream();

        return render_template("ErrorIndex.html");
DepB.add_url_rule("/DisplayData/DepartmentOverview","Department",Department);
