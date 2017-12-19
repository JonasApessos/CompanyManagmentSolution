import sqlite3
from flask import redirect,request,url_for,session,Blueprint,render_template

ProjB = Blueprint('projb',__name__,template_folder='templates');
TaskB = Blueprint('taskb',__name__,template_folder='templates');
ContrB = Blueprint('contrb',__name__,template_folder='templates');
CompB = Blueprint('compb',__name__,template_folder='templates');
EmpB = Blueprint('empb',__name__,template_folder='templates');

ProjB.secret_key="70012";

DATABASE = "CompanyManagmentDB.db";
PREFIX = "RE1201";
PREFIX += "_" ;