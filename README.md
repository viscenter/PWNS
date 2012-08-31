READ ME FILE

7/11/2012

The python programs included on this folder have specified functionallities for the configuration
methods used in the Calib3.0 program and have been developed for the current notation in the text 
files used during the process.

This should not be used in any other documents which these programs where not intended to work 
with.

Modifications for compatibility with other files are permitted by specifying the porpouse of 
the modified versions in a comment block section at the top of the file.

7/31/2012

The program that was used to create the calibration files is called Calib3.0 and it is located on 
C:\Calib3.0-relesaae folder. They can be loaded as a batch of 3 within the program after running these commands:

>ProjectorController_Con.exe
>ProhectorController.exe -p 1337
>ProhectorController.exe -p 1338
>ProhectorController.exe -p 1339

The files ending with Pxx_Cxx.txt are configuration files that contain different calibrations.
The default save files are those starting at P00_C00.txt and only those. The others are either 
backups or previous attempts. It is important to point out that a final version of the configuration 
files are saved in /FINAL folder withing this one. They should not be replaced and eventually 
catalogued by date.

2/08/2012
Desktop/PWNS folder contains every file use for the development of this project