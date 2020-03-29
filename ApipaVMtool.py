#This script will check for APIPA addresses for all virtual machines in a host, apipa Addresses are usually assigned when a VM fails to obtain a valid IP.
#@Author: Carlos Avalos

from pyVim.connect import SmartConnect
from pyVmomi import vim
import re
import os
import ssl
import time
arr = []
pwr = []
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context
serviceInstance = SmartConnect(host="host",user="user",pwd="pwd")
content = serviceInstance.RetrieveContent()
vm_view = content.viewManager.CreateContainerView(content.rootFolder,[vim.VirtualMachine],True)

def apipaFind():
    def apipaOff(new):
        i = 0
        while( i < len(new)):
            searchIndex = serviceInstance.RetrieveContent().searchIndex
            vms = searchIndex.FindAllByIp(ip= new[i], vmSearch=True)
            for vm in vms:
                pwr.append(vm.name)
                vm.PowerOff
                i+=1
        print("Task Completed, VM's reset due to APIPA IP: ", pwr)
    for vm in vm_view.view:
        ip = vm.guest.ipAddress
        newIp = str(ip)
        arr.append(newIp)
        r = re.compile(".*169.254")
        new = list(filter(r.match,arr))
    apipaOff(new)
    
        

try:
    while True:
        apipaFind()
        time.sleep(300)
except KeyboardInterrupt:
    print('Manual break by user')
    

