import sqlite3
from flask import Flask, request, render_template, redirect, url_for, session

#from CMApp.modules.InsertMechanism.InsertContract import IContract
#from CMApp.modules.InsertMechanism.InsertCompany import ICompany
#from CMApp.modules.InsertMechanism.InsertTask import ITask
#from CMApp.modules.InsertMechanism.InsertEmployee import IEmployee

#from CMApp.modules.GetMechanism.GetTaskForm import GetFormAssignProject
#from CMApp.modules.GetMechanism.GetEmpForm import GetFormDepartment
#from CMApp.modules.GetMechanism.GetProjects import GetProjectList
#from CMApp.modules.GetMechanism.GetProjects import GetProjectListByID
#from CMApp.modules.GetMechanism.GetProjects import GetProjectContractList
#from CMApp.modules.GetMechanism.GetTask import GetProjectTask
#from CMApp.modules.GetMechanism.GetTask import GetProjectTaskDep
#from CMApp.modules.GetMechanism.GetContract import GetContractList
#from CMApp.modules.GetMechanism.GetContract import GetContractListByProject
#from CMApp.modules.GetMechanism.GetCompany import GetCompanyList
#from CMApp.modules.GetMechanism.GetDepartment import GetDepartmentList
from CMApp.modules.UpdateMechanism.SetProject import SetProjectIsActiv

from CMApp.modules.ProjectFunc import *
from CMApp.modules.TaskFunc import *
from CMApp.modules.ContractFunc import *
from CMApp.modules.CompanyFunc import *
from CMApp.modules.EmployeeFunc import *

app = Flask(__name__);
app.secret_key="77012";

from CMApp.modules import ProjB
from CMApp.modules import TaskB
from CMApp.modules import ContrB
from CMApp.modules import CompB
from CMApp.modules import EmpB

app.register_blueprint(ProjB,url_prefix="/Projects");
app.register_blueprint(TaskB,url_prefix="/Tasks");
app.register_blueprint(ContrB,url_prefix="/Contracts");
app.register_blueprint(CompB,url_prefix="/Company");
app.register_blueprint(EmpB,url_prefix="/Employees");

DATABASE = "CompanyManagmentDB.db";
PREFIX = "RE1201";
PREFIX += "_" ;
DEBUG = True;
PORT = 80;
HOST = "127.0.0.1";
