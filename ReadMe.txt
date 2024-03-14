docker build -t my_image.

docker run -it mu_image .

root@96fb854bb044:/home/doc-bd-a1# touch load.py

root@96fb854bb044:/home/doc-bd-a1# touch dpre.py model.py eda.py vis.py

root@96fb854bb044:/home/doc-bd-a1# python3 load.py train_titanic.csv

#Since we are working on windows not linux We changed final.sh to final.ps1 


# Commands used in powershell

Set-ExecutionPolicy RemoteSigned 
.\final.ps1