from . import *

class TableDiagram:

	def __init__(self):
		pass;

	def __del__(self):
		pass;

	def CreateTableDiagram(self, TaskRows, TaskDep):
		TableList = [];
		print(type(TaskRows));

		print("\nTasks: " + str(TaskRows));
		print("\nDependencys: " + str(TaskDep));
		LastIndex = 0;

		for i in range(len(TaskDep)):
			#print("\nSTAGE["+str(i)+"]");
			if (TaskDep[i][1] == None):
				TableList.append([TaskDep[i][0], TaskDep[i][1]]);

		for x in range(0,len(TableList)):
			for i in range(0,len(TaskDep)):
				#print("Check["+str(x)+str(TableList[LastIndex]) +"] -> "+ str(TableList[LastIndex][0]) + " == " + str(TaskDep[i][0]) +" IsEqual?: "+ str(TableList[LastIndex][0] == TaskDep[i][0]));
				print(str(TableList[x][0]) + "==" +str(TaskDep[i][1]));

				if(TableList[x][0] == TaskDep[i][1]):
					TableList.insert(x+1,[TaskDep[i][0],TaskDep[i][1]]);
					LastIndex= x;
				elif(TableList[LastIndex][0] == TaskDep[i][1]):
					TableList.insert(LastIndex,TaskDep[i][1]);


		print("TableList Cycle["+str(x)+"]: " + str(TableList));

		#print("List:" + str(TableList));
		return TableList;
