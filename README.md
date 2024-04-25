# Tasks

Step 0:  
Set up virtual environment. It can be done through your IDE like
PyCharm or you can do it in cmd.

Unix:   

    $ python3 -m venv <name_of_env>
    $ source ./<name_of_env>/bin/activate

Window:

    $ python -m venv <name_of_env>
    $ .\<name_of_env>\Scripts\activate.bat

If you have any problems with setting up the virtual environment,
try to search in internet or use your normal python interpreter.

Step 1:  
Install requirements. If you are using IDE than probably it can
install all requirements on its self. Otherwise, use command

    $ pip install -r requirements.txt

Step 2:   
For FastAPI we use ASGI server. You need install it separately.

    $ pip install "uvicorn[standard]"

And when you want to launch the server then type following:

    $ uvicorn <file_name_wo_extention>:app --reload

The flag "--reload" means that after each your saving of the file 
will be launched again. Remember that all your previous request 
actions will be deleted.

## Task 1: Flask

You will find TODO instructions in the server_flask.py
file. Complete the missing lines of code and launch the 
test file test_flask.py. It uses testing framework pytest.

Either use you cmd to run all flask tests

    $ pytest

or if you have IDE like PyCharm simply run the whole file.

If all test are completed successfully then it is working 
Code. But! Remember that tests cannot prove absence of bugs.


## Task 2: FastApi

#### Start server: uvicorn server_fastapi:app --reload
