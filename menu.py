import os
import getpass
import webbrowser

os.system("tput setaf 3")
print("\t\t\t Welcome to my App !!")
os.system("tput setaf 7")
print("\t\t\t----------------------")

passwd = getpass.getpass("Enter your  password : ")
if passwd != "joker":
    print("Invalid Password")
    exit()

Wish= input("Where you  to want to run this menu ? (local/remote) :")
print(Wish)

while True:
    os.system("clear")
    print("""
    \n
    Press 1: to run date
    Press 2: to run cal
    Press 3: to reboot
    Press 4: to user create
    Press 5: to exit
    Press 6: to start Voice Assistant
    Press 7: to check IPV4 i.e IP address
    Press 8: to ping Google
    Press 9: to open Github
    Press 10:to open Linkedin
    Press 11:to open dockerhub
    Press 12: to open aws management console
    Press 13: For creating a file
    Press 14: Starting httpd Server
    Press 15: Stopping httpd server
    Press 16: Checking status of httpd server
    Press 17: Downloading a image in the docker
    Press 18: Checking the images
    Press 19: Launching a docker Container
    Press 20: Checking the number of os running or Stopped

    """)
    Choice = input("Enter your Choice")
    print(Choice)

    if Wish == "local":
        if int(Choice) == 1:
            os.system("date")
        elif int(Choice) == 2:
            os.system("cal")
        elif int(Choice) == 3:
            os.system("reboot")
        elif int(Choice) == 4:
            os.system("useradd Joker")
        elif int(Choice) == 5:
            exit()
        elif int(Choice) == 6:
            os.system("espeak-ng 'Hi I am Alexa What would you like to run'")
        elif int(Choice) == 7:
            os.system("ifconfig enp0s3")
        elif int(Choice) == 8:
            os.system("ping goo.gl -c 4")
        elif int(Choice) == 9:
            webbrowser.open("https://github.com")
        elif int(Choice) == 10:
            webbrowser.open("https://www.linkedin.com/feed/")
        elif int(Choice) == 11:
            webbrowser.open("https://hub.docker.com")
        elif int(Choice) == 12:
            webbrowser.open("https://aws.amazon.com")
        elif int(Choice) == 13:
            i= input("Write file name:")
            os.system("gedit {}".format(i))
        elif int(Choice) == 14:
            os.system("systemctl start httpd")
        elif int(Choice) == 15:
            os.system("systemctl stop httpd")
        elif int(Choice) == 16:
            os.system("systemctl status httpd")
        elif int(Choice) == 17:
            y= input("Enter the image name")
            d= input("Enter the Version name")
            os.system("docker pull {}:{}".format(y,d))
        elif int(Choice) == 18:
            os.system("docker images")
        elif int(Choice) == 19:
            j = input("Enter the name of Container")
            k = input("Enter the name of image")
            l = input("Enter the image version ")
            os.system("docker run -it --name {} {}:{}".format(j,k,l))
        elif int(Choice) == 20:
            os.system("docker ps -a")




        else:
            print("not supported")

    elif Wish == "remote":
       ip = input("Enter remote ip :")
       print(ip)
       if int(Choice) == 1:
           os.system("ssh {} date".format(ip))
       elif int(Choice) == 2:
           os.system("ssh {} cal".format(ip))
       elif int(Choice) == 3:
            os.system("ssh {} reboot".format(ip))
       elif int(Choice) == 4:
           os.system("ssh {} useradd Tiger".format(ip))
       elif int(Choice) == 5:
           os.system("ssh {} exit()".format(ip))
       elif int(Choice) == 6:
           os.system("ssh {} espeak-ng 'Hello Dynamo here what would you like to run'".format(ip))
       elif int(Choice) == 7:
           os.system("ssh {} ifconfig enp0s3".format(ip))
       elif int(Choice) == 8:
           os.system("ssh {} ping goo.gl -c 4".format(ip))
       elif int(Choice) == 9:
           webbrowser.open("ssh {} https://github.com".format(ip))
       elif int(Choice) == 10:
           webbrowser.open("https://www.linkedin.com/feed/")
       elif int(Choice) == 11:
           webbrowser.open("https://hub.docker.com".format(ip))
       elif int(Choice) == 12:
           webbrowser.open("https://aws.amazon.com".format(ip))
       elif int(Choice) == 13:
           v= input("Enter file name")
           os.system("ssh {} gedit {}".format(ip,v))
       elif int(Choice) == 14:
           os.system("ssh {} systemctl start httpd".format(ip))
       elif int(Choice) == 15:
           os.system("ssh {} systemctl stop httpd".format(ip))
       elif int(Choice) == 16:
           os.system("ssh {} systemctl status httpd".format(ip))
       elif int(Choice) == 17:
           z= input("Enter the image name")
           x= input("Enter the image Version name")
           os.system("ssh {} docker pull {}:{}".format(ip,z,x))
       elif int(Choice) == 18:
          os.system("ssh {} docker images".format(ip))
       elif int(Choice) == 19:
           u= input("Enter the name of Container")
           v= input("Enter the image name")
           h= input("Enter the name of Version")
           os.system("ssh {} docker run -it --name {} {}:{}".format(ip,u,v,h))
       elif int(Choice) == 20:
          os.system("ssh {} docker ps -a".format(ip))
       



           

    else:
        print("not supported login")

    input("\n Plz enter to cont..........")






