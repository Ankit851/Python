import os
os.system("tput setaf 3")
print("\t\t\t Automating LVM partition")
os.system("tput setaf 7")
way = input("""
Press 1 to create LVM partition
Press 2 to resize the partition
Your choice: """)
way = int(way)
def lvm(name_of_vg,count):
	if count==0:
		alphabet = "b"
	elif count==1:
		alphabet = "c"

	os.system("pvcreate  /dev/sd{}".format(alphabet))
	os.system("pvdisplay  /dev/sd{}".format(alphabet))
	os.system("vgcreate  {} /dev/sd{}".format(name_of_vg,alphabet))
	os.system("vgdisplay  {}".format(name_of_vg))
#3 steps you have  to do to use any storage
def creating_partition(name_of_vg, name_of_partition):
	number=input("Logical volume number : ")	
	print("creating logical volume")
	os.system("lvcreate  --size {}G --name {} {}".format(ch,name_of_partition,name_of_vg))
	os.system("mkfs.ext4 /dev/{}/{}".format(name_of_vg,name_of_partition))
	os.system("mkdir logical_volume{}".format(number))
	os.system("mount /dev/{}/{} 			logical_volume{}".format(name_of_vg,name_of_partition,number))
	#os.system("df  -h")
	os.system("clear")

if way==1:
	#Specify name to volume group 
	vg = input("Write the name of Volume group to be created: ")
		
	# system already has hard disk we have to just create physical volume of it
	count_of_phy_vol=input("How many external hard disk you have attached: ")	
	count = 0
	#Calling the function to make physical volume and volume group
	while count < int(count_of_phy_vol):	
		#count stores the times function is called		
		lvm(vg,count)
		os.system('clear')
		count += 1 
	partition_name = input("Write the name of logical volume: ")
	ch=input("Storage required (in GB): ")
	ch = int(ch)
	# calling function
	creating_partition(vg,partition_name)
	#info
	print("Logical volume of size {}G created".format(ch))
	#displaying lv
	#os.system("lvdisplay {}/{}".format(vg,partition_name))

elif way==2:
	vg = input("Enter the volume group name:" )
	partition_name=input("Enter the logical volume name: ")			
	# on the fly you want to  increase the storage
	volume=input("Storage required (in GB): ")
	os.system("lvextend  --size +{}G /dev/{}/{}".format(volume,vg,partition_name))
	# will format the storage part that is added to the existing partition 
	os.system("resize2fs /dev/{}/{}".format(vg,partition_name))
	os.system("clear")


