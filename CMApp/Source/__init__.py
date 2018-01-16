import sys

#in production this should always be set to 1
sys.dont_write_bytecode = 0;

#import flask framework
from flask import Flask, session, render_template

#all functions that exists in EmpB namespace
from modules.DepartmentFunc import *
#all functions that exists in ProjB namespace
from modules.ProjectFunc import *
#all functions that exists in TaskB namespace
from modules.TaskFunc import *
#all functions that exists in ContrB namespace
from modules.ContractFunc import *
#all functions that exists in CompB namespace
from modules.CompanyFunc import *
#all functions that exists in EmpB namespace
from modules.EmployeeFunc import *
#Spacial handle for the logical errors to be registered in a log file
from modules.FileHandleClasses.ErrorHandle import ErrorHandle

#The blueprint namespaces
from modules import ProjB
from modules import TaskB
from modules import ContrB
from modules import CompB
from modules import EmpB
from modules import DepB

#init the flask framework
app = Flask(__name__);
#the key to encrypt sessions in client and server side.  PS. change it to your own code, this is a default code and it's not secure
app.secret_key="77012";

#Register all blueprint namespaces to the flask application
app.register_blueprint(ProjB,url_prefix="/Projects");
app.register_blueprint(TaskB,url_prefix="/Tasks");
app.register_blueprint(ContrB,url_prefix="/Contracts");
app.register_blueprint(CompB,url_prefix="/Company");
app.register_blueprint(EmpB,url_prefix="/Employees");
app.register_blueprint(DepB,url_prefix="/Department");

#Macros
DATABASE = "CompanyManagmentDB.db";
PREFIX = "RE1201";
PREFIX += "_" ;
DEBUG = True;
PORT = 80;
HOST = "127.0.0.1";
VERSION = "0.0.8.3";
