import eel
eel.init('E:/Academics/6thSemester/IR/A2/IR_A2k18-1053/Project')
import numpy as np
import sys
from ipaddress import IPv4Address, IPv4Network


def octManip(str1,str2,operator="+"):
	list1,list2,list3=str1.split('.'),str2.split('.'),[]
	# print(list1)
	# print(list2)
	# print(list3)
	upOne=False

	for i in range(len(list1)-1,-1,-1):
		list1[i]=int(list1[i])
		list2[i]=int(list2[i])
		if operator == '+':
			solution=int(list1[i]).__add__(int(list2[i]))
		elif operator == '-':
			solution=int(list1[i]).__sub__(int(list2[i]))
		elif operator == '*':
			solution=int(list1[i]).__mul__(int(list2[i]))
		elif operator == '/':
			solution=int(list1[i]).__div__(int(list2[i]))
		if upOne:
			solution=int(solution).__add__(1)
			upOne=True
		if solution>=256:
			solution=0
			upOne=True
		list3.append(solution)
	list3.reverse()
	dotDec='.'.join(map(str,list3))
	return dotDec
#####################################################
def NetID(ip,subnetmask):
	mask=subnetmask.split('.')
	ip=ip.split('.')
	netid=''
	for oct in range(len(ip)):
		netid+=str(np.bitwise_and(int(ip[oct]),int(mask[oct])))+'.'
	netid=netid.strip('.')
	return netid
#####################################################
def cidr2mask(cidr):
	powersrev=[2**x for x in range(8)]
	powersrev.reverse()
	blockSize=[sum(powersrev[:x]) for x in range(1,len(powersrev)+1)]
	octetOfInterest=0
	cidr=int(cidr)
	# print(cidr)
	mask=''
	count=0
	
	for i in range(cidr//8):
		mask+='255.'
		count+=1
	for x in range(cidr%8):
		octetOfInterest=blockSize[x]
	count+=1
	mask+=str(octetOfInterest)
	
	while count<4:
		mask+='.0'
		count+=1
	return mask


# Main Body of Program:            - if run directly

def checkclass(ipad):
	classA = IPv4Network(("10.0.0.0", "255.0.0.0"))  # or IPv4Network("10.0.0.0/8")
	classB = IPv4Network(("172.16.0.0", "255.240.0.0"))  # or IPv4Network("172.16.0.0/12")
	classC = IPv4Network(("192.168.0.0", "255.255.0.0"))  # or IPv4Network("192.168.0.0/16")
	ip1 = IPv4Address(ipad)
	if ip1 in classA:
		return('A')
	elif ip1 in classB:
		return('B')
	elif ip1 in classC:
		return('C')
	else:
		return("None")

@eel.expose
def main(ipadd):
    # ANS=ipadd
	try:
		ANS=sys.argv[1]
	except:
		# print("Enter IP and CIDR [ex. xxx.xxx.xxx.xxx/xx]: ")
		ANS=ipadd

	if '/' not in ANS:
		ANS+='/32'

	IP,CIDR=ANS.split('/')

	ipclass=checkclass(IP)
	eel.IPclass(ipclass)

	subnetmask=cidr2mask(CIDR)
	eel.subnett(subnetmask)

	netid=NetID(IP,subnetmask)

	wildmask=octManip('255.255.255.255',subnetmask,'-')
	eel.wildcard(wildmask)

	broadcast=octManip(netid,wildmask)
	eel.broadcast(broadcast)

	first=octManip(netid,'0.0.0.1')
	eel.firstnet(first)

	last=octManip(broadcast,'0.0.0.1','-')
	eel.lastnet(last)

	nextnet=octManip(broadcast,'0.0.0.1')
	eel.nextnet(nextnet)
    
	eel.cidr(CIDR)

eel.start('homee.html')