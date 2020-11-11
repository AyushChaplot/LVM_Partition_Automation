import subprocess as sp
import names
import os


def lvm():
	os.system("clear")
	d1= input("Enter the name of 1st disk:")
	d2= input("Enter the name of 2nd disk:")

	pv1 = sp.getstatusoutput("pvcreate {}".format(d1))
	pv2 = sp.getstatusoutput("pvcreate {}".format(d2))

		
	if pv1[0]== 0 and pv2[0]==0:
		print("pv created sucessfully...")
		nn = names.get_first_name()
		vg = sp.getstatusoutput("vgcreate {} {} {}".format(nn,d1,d2))
		if vg[0]==0:
			print("vg {} created sucesfully..".format(nn))
			lvm_size = input("Enter the size of partition")
			lvm_name = input("Enter the lvm name")
			sp.getstatusoutput("lvcreate --size {} --name {}{}".format(lvm_size,lvm_name,nn))
			print("Partition of {} created from vg {} sucessfully...".format(lvm_size,nn))

def vg_display():
	out = os.system("vgdisplay")
	print(out)
def lvm_display():
	out = os.system("lvdisplay")
	print(out)


while 1:
	os.system("clear")
	print("\t\t\t\t\tLVM Automation")
	print(48*"-")

	print("""
	Press 1: To create lvm & partition
	Press 2: For details of VG
	Press 3: For details of lvm
	Press 4: Exit
	""")
	opt = int(input("Enter your choice"))


	if opt == 1:
		os.system("clear")
		lvm()
	elif opt == 2:
		os.system("clear")
		vg_display()
	elif opt == 3:
		os.system("clear")
		lvm_display()
	else:
		break
	input()
