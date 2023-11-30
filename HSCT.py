# Hosts Syntax Convert Tool
# HSCT.v1.20231201.1
print("HSCT.v1.20231201.1")
print("--------------------")
org_file_path = str(input("List path: "))
with open(org_file_path, 'r') as f:
    lines = f.readlines()
with open(org_file_path, 'w') as f:
    for line in lines:
        f.write('DOMAIN,' + line)