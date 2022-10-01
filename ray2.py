print("welcome to tool kit for finding emclosure size for modular enclsoures")
print("good luck")
name = input("what is name of the final db ")
print('entered final db name is ' + name)
isolator = input("enter the number of 4p isolator ")
isolator = int(isolator)
poleiso = input("enter number of isolator poles ")
poleiso = int(poleiso)
isolatormodule = isolator * poleiso
isolatormodule = int(isolatormodule)
print("total number of isolator modules is ", isolatormodule)
elcb4p = input("enter the number of 4p elcb ")
elcb4p = int(elcb4p)
poleelcb = input("enter number of 4p elcb poles ")
poleelcb = int(poleelcb)
polele4p = elcb4p * poleelcb
polele4p = int(polele4p)
print("total number of 4p elcb modules is ", polele4p)
elcb2p = input("enter number of 2p elcb poles ")
elcb2p = int(elcb2p)
poleelcb2p = input("enter number of 2p elcb poles ")
poleelcb2p = int(poleelcb2p)
polele2p = elcb2p * poleelcb2p
polele2p = int(polele2p)
print("total number of 2p elcb modules is ", polele2p)
spmcb = input("enter the total number of single pole mcb ")
spmcb = int(spmcb)
print("total number of sp mcb are ", spmcb)
space = input("enter the total number of space ")
space = int(space)
addspace = input("additional space needed/required for cabling and future load ")
addspace = int(addspace)
totalmodules = int(isolatormodule) + int(polele4p) + int(polele2p) + int(spmcb)  + int(space) + int(addspace)
totalmodules = int(totalmodules)
print("total module is  ", totalmodules)
if(totalmodules<=16):
    print("recommended final db enclosure is 1 row 16")
if(32 >= totalmodules >= 17 ):
    print("recommended final db enclosure is 2 row 16")
if(48 >= totalmodules >= 33):
    print("recommended final db enclosure is 3 row 16")
if(64 >= totalmodules >= 49):
    print("recommended final db enclosure is 4 row 16")
if(80 >= totalmodules >= 65):
    print("recommended final db enclosure is 5 row 16")
if(96 >= totalmodules >=81):
    print("recommended final db enclosure is 4 row 24")
if(120 >= totalmodules >=97):
    print("recommended final db enclosure is 5 row 24")









