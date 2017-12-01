To create the database you must execute the CMDatabase.py

In order to execute the file you must install python 3.6 and in the command line type -> $python CMDatabase.py(you will have to set the python.exe to global path or set the project folder in the file where the exe residse in order to execute it).

WARNING: This project is based on the flask_12.0 library, if you try to start the CMMain.py without installing the current version of flask, the program will return an error of a missing module or any other kind of error. Trying to use those file for other kinds of projects that don't use flask_12.0 or any other kind of flask will not be possible.(I'm sorry :( ).

The main start point of the application is CMMain.py , this will fire every action nedded to start the server and the event listeners using the following command -> $python CMMain.py

After starting the server use your browser and type on the url "localhost:5000". Local host is the ip address on your local machine where the server is. The "5000" is the port in which the server is listening from, by default the server is listening in the port 5000.