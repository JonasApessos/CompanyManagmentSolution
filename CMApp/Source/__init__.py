import sys

sys.dont_write_bytecode = 0;

import sqlite3

from flask import Flask, session, render_template

from modules.ProjectFunc import *
from modules.TaskFunc import *
from modules.ContractFunc import *
from modules.CompanyFunc import *
from modules.EmployeeFunc import *
from modules.FileHandleClasses.ErrorHandle import ErrorHandle

from modules import ProjB
from modules import TaskB
from modules import ContrB
from modules import CompB
from modules import EmpB

app = Flask(__name__);
app.secret_key="77012";#the key to encrypt sessions in client and server side.  PS. change it to your own code, this is a default code and it's not secure

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
