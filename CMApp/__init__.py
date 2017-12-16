from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__);

import os
import sqlite3

from CMApp.modules.InsertMechanism.InsertContract import IContract
from CMApp.modules.InsertMechanism.InsertCompany import ICompany
from CMApp.modules.InsertMechanism.InsertTask import ITask
from CMApp.modules.InsertMechanism.InsertEmployee import IEmployee

from CMApp.modules.GetMechanism.GetTaskForm import GetFormAssignProject
from CMApp.modules.GetMechanism.GetEmpForm import GetFormDepartment
from CMApp.modules.GetMechanism.GetProjects import GetProjectList
from CMApp.modules.GetMechanism.GetTask import GetProjectTask
from CMApp.modules.GetMechanism.GetTask import GetProjectTaskDep
from CMApp.modules.GetMechanism.GetContract import GetContractList
from CMApp.modules.GetMechanism.GetContract import GetContractListByProject

from CMApp.modules.UpdateMechanism.SetProject import SetProjectIsActiv

DATABASE = "CompanyManagmentDB.db";
PREFIX = "RE1201";
PREFIX += "_" ;