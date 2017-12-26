import sys
import inspect

sys.dont_write_bytecode = 1;

from ..FileHandleClasses.ErrorHandle import ErrorHandle
from ..DatabaseClasses.DatabaseQuery import DatabaseQuery

DATABASE = "CompanyManagmentDB.db";
PREFIX = "RE1201";
PREFIX += "_";