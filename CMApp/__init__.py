from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__);

import os
import sqlite3

from CMApp.modules.InsertMechanism.InsertContract import IContract
from CMApp.modules.InsertMechanism.InsertCompany import ICompany
from CMApp.modules.InsertMechanism.InsertTask import ITask
from CMApp.modules.InsertMechanism.InsertEmployee import IEmployee

from CMApp.modules.GetMechanism.GetTaskFormData import GetFormAssignProject
from CMApp.modules.GetMechanism.GetEmpFormData import GetFormDepartment
from CMApp.modules.GetMechanism.GetProjects import GetProjectList
from CMApp.modules.GetMechanism.GetTaskData import GetProjectTaskData

Database = "CompanyManagmentDB.db";
Prefix = "RE1201";
Prefix += "_" ;