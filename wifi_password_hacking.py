import subprocess #use system commands
import re #use regex

command_output=subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

#capture the output of the system command and save the contents after decoding from bytes to unicode

profile_names=(re.findall(" All User Profile     : (.*)\r", command_output))

wifi_list=list()

if len(profile_names)!=0 :
    for name in profile_names:
        wifi_profile=dict() #empty dictionary for each wifi connection
        profile_info=subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()

        if re.search(" Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"]=name
            profile_info_password=subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
            
            password=re.search("Key Content            : (.*)\r", profile_info_password)

            if password==None:
                wifi_profile["password"]=None

            else:
                wifi_profile["password"]=password[1]

            wifi_list.append(wifi_profile)

for i in range(len(wifi_list)):
    print(wifi_list[i])