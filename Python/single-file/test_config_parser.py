"""
testAccountService library
"""
#!/usr/bin/python3

import configparser

cf = configparser.ConfigParser()

cf.read("/etc/lightdm/lightdm.conf")

try:
    name = cf.get("SeatDefaults", "autologin-user")
    if name is not None:
        print("lucky %s, autologin next time!" % name)
except configparser.NoSectionError:
    print("No Section Error!")
except Exception as error_reason:
    print("failed: %s" % error_reason)
