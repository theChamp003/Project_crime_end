# Criminal detection and recognition project using the LBPH algorithm

## Motivation for the project
   
   Face_train.py is the file that need to be run to begin the running of the project. 

   datasetCreator is the py file to insert a new model to the database 

   DB.py links the mySQL server to the database created 

   Face_train.py contains the code to train the given model 

### Please Note -- 
 Since this project use mysql server you need to create a database namely db in your server and also in where ever we are connecting to mysql 
 you need to provide your user and password to connect. 

 Create a Database in mysql server workbench namely Criminal -- with table records 
 column namely Name,Records,Detech with datatype as varchar
 


## Libraries Used

### openCV2 
OpenCV2 is used for providing a medium to identify frontal_face and fetch facial features using Haarcascade.
> pip install opencv-python

### Pillow
Pillow is used to manage hundreds of criminal images in an ordered manner.
> pip install Pillow

### Numpy
Numpy is used for converting the given dataset to a training model and deploying the plugin in production with ease.
> pip install numpy

### PyMySql
PyMySql is used to refer to the criminal database and ping the collection everytime a criminal is detected by the model.
> pip install PyMySQL



