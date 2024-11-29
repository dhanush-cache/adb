from pathlib import Path

import adb
from packages import disable, install, uninstall

# Connect
if not adb.is_connected():
    url = input("URL: ")
    adb.connect(url)
    if not adb.is_connected():
        print("Seems like the device isn't paired.")
        pairing_url = input("Pairing URL: ")
        code = input("Pairing code: ")
        adb.pair(pairing_url, code)
        adb.connect(url)

# Freeze
for package in disable:
    if not adb.is_enabled(package):
        continue
    print(f"Disabling: {package}...", end=" ")
    try:
        adb.clear_data(package)
        adb.disable(package)
    except:
        print("Failed!!!")
    else:
        print("Done!")

# Uninstall
target = Path.home() / "sapps"
target.mkdir(parents=True, exist_ok=True)
for package in uninstall:
    if not adb.is_installed(package):
        continue
    print(f"Uninstalling: {package}...", end=" ")
    try:
        adb.clear_data(package)
        adb.extract(package, target)
        adb.uninstall(package)
    except:
        print("Failed!!!")
    else:
        print("Done")
