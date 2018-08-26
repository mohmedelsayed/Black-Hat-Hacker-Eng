#!/usr/bin/env python
#############################################################
# #----- Simple Mac Changer anay Interface In Linux ------# #
#                                                           #
# #----- Created By : Eng-Mohmed Elsayed ----- #            #
#                                                           #
#############################################################
import subprocess
import optparse
import time

try:
    subprocess.call(["clear"])
    print("""
    #############################################################
    # #----- Simple Mac Changer anay Interface In Linux ------# #
    #                                                           #
    # #----- Created By : Eng-Mohmed Elsayed ----- #            #
    #                                                           #
    #############################################################
    """)

    enter= '-\n-\n-\n-'
    len_word="You Must Wtite :==> python MacChanger.py -i [Your Interface as wlan0 or  eth0 or wlan1...etc] -m [New Mac But Sure That The Mac Is Valid]"
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help=" Set interface to change It's MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help=" Set New MAC Address")
    print(len_word)
    print(enter)
    (options, arguments) = parser.parse_args()
    interface = options.interface
    new_mac = options.new_mac
    print("[+]" + " changing MAC Address For The Interface \"" + interface + "\"" " To : " + new_mac +enter)
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    i = subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
except Exception as error:
    print ("Please wait !")
    time.sleep(3)
    print("""
    Some Error Found ===> """+str(error))
    time.sleep(2)
    print('Note')
    print("----")
    print("To Solve all Problem =====>")
    time.sleep(2)
    print(enter+"Make Sure That You Didn't write : ==>python MacChanger.py")
    time.sleep(3)
    print(enter+"You Must Wtite :==> python MacChanger.py -i [Your Interface as wlan0 or  eth0 or wlan1...etc] -m [New Mac But Sure That The Mac Is Valid]"+enter)










# parser=optparse.OptionParser()
# i = subprocess.call("ifconfig",shell=True)
# for print_all in str(i):
#     print('\n'+str(print_all))
