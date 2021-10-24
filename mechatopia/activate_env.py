import os
from pathlib import Path
print("\n###   activate venv!   ###")
pp = os.getcwd()+"\\..\\.venv_project\\Scripts\\activate";
#print(pp)
os.system('cmd /k ' + pp)


#print('getcwd:      ', os.getcwd())
#print('__file__:    ', __file__)
#os.system('cmd /k "C:\\Users\\Administrator\\Desktop\\cn331_project_mechatopia\\.venv_project\\Scripts\\activate"')