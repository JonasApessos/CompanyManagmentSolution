import sys

sys.dont_write_bytecode = 1;

from ..FileHandleClasses.ErrorHandle import ErrorHandle
from ..DatabaseClasses.DatabaseQuery import DatabaseQuery
from flask import request
#import sqlite3

DATABASE = "CompanyManagmentDB.db";
PREFIX = "RE1201";
PREFIX += "_";
VERSION = "0.0.8.3";
