import sys

sys.dont_write_bytecode = 1;

import sqlite3
from flask import redirect,request,url_for,session,Blueprint,render_template
from modules.FileHandleClasses.ErrorHandle import ErrorHandle

ProjB = Blueprint('projb',__name__,template_folder='templates');
TaskB = Blueprint('taskb',__name__,template_folder='templates');
ContrB = Blueprint('contrb',__name__,template_folder='templates');
CompB = Blueprint('compb',__name__,template_folder='templates');
EmpB = Blueprint('empb',__name__,template_folder='templates');
DepB = Blueprint('depb',__name__,template_folder='templates');

ProjB.secret_key="70012";#the key to encrypt sessions in client and server side.  PS. change it to your own code, this is a default code and it's not secure

DATABASE = "CompanyManagmentDB.db";
PREFIX = "RE1201";
PREFIX += "_" ;
VERSION = "0.0.8.3";
