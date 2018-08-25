#!/usr/bin/env python
#############################################################
# #----- Simple Mac Changer anay Interface In Linux ------# #
#                                                           #
# #----- Created By : Eng-Mohmed Elsayed ----- #            #
#                                                           #
#############################################################

print("""
#############################################################
# #----- Simple Mac Changer anay Interface In Linux ------# #
#                                                           #
# #----- Created By : Eng-Mohmed Elsayed ----- #            #
#                                                           #
#############################################################
""")
import subprocess
import optparse
parser=optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help=" Set interface to change It's MAC Address")
parser.add_option("-m","--mac",dest="new_mac",help=" Set New MAC Address")

(options,arguments) = parser.parse_args()
interface=options.interface
new_mac= options.new_mac
print("[+]" +" changing MAC Address For The Interface \""+interface +"\"" " To : "+new_mac+"\n\n")
subprocess.call(["sudo", "ifconfig", interface, "down"])
i=subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])








# parser=optparse.OptionParser()
# i = subprocess.call("ifconfig",shell=True)
# for print_all in str(i):
#     print('\n'+str(print_all))
