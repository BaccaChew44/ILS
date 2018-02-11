import subprocess
import requests

def getCardUID():
    lines = subprocess.getoutput("/home/pi/libnfc/libnfc-1.7.0/examples/nfc-poll.exe")
    UID = ''
    for line in lines:
        UID = UID + line
    if 'UID (NFCID1)' not in UID:
        UID = 'No Swipe'
        return UID
    UID = (UID.split(':')[5])
    UID = UID.replace(" ", "")
    idx = UID.find('S')
    UID = UID[0:idx-1]
    if UID == '':
        UID = 'Error'
    return UID

	