import subprocess
import time

def Activator():
    subprocess.Popen("pushd ./contracts/chainlink/scripts", shell=True)
    subprocess.Popen("brownie run ./vrf_scripts/deploy_vrf.py  --network kovan", shell=True)
    time.sleep(100)
    subprocess.Popen("brownie run ./vrf_scripts/fund_vrf.py  --network kovan", shell=True)
    time.sleep(100)
    subprocess.Popen("brownie run  ./vrf_scripts/request_randomness.py  --network kovan", shell=True)
    time.sleep(100)
    subprocess.Popen("brownie run  ./vrf_scripts/read_random_number.py  --network kovan", shell=True)