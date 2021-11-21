set VAR_1=this
start python test.py %1 %VAR_1%
set VAR_1=that
start python test.py %1 %VAR_1%
pause