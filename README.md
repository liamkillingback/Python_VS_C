# Python in C
#### Video Demo: https://youtu.be/s77_BJj_iyc
#### Description:
This project was inspired by looking at the differences between languages and i found that in general, even though python is very user friendly and easy to understand, in a lot of cases python can be slower. intruiged by this i also found that you can call functions written in other languages from python to make runtimes faster. so basically this project is about comparing the speed of various actions between Python and C, written in Python.
# c_.so
c_.so is a shared file created from a .C file which contains functions that i would like to use in my python code. The reason this is necessary is because the python file will need to be able to read a library written in C and interpret it into Python.
# project.py
This contains the main code for the project and documents the time it takes to do a certain mathematical equation, x ammount of times in both languages, and compares the two speeds. Secondly it documents how much faster C is at looping (in this case it adds 1 to itself x ammount of times). in this case, Python seems to be faster at simple mathematical equations if your project is written in python, but if you were to do some pretty sizeable looping, it can be beneficial to implement another language which can be much faster at achieving the same result.
# library.c
This file contains the functions written in C, that i would like to implement into my Python code.
# requirements.txt
This file contains the required libraries to run the program.
# test_project.py
This runs the unit tests on the functions implemented to make sure that they are doing exactly what they are suppose to be doing.

