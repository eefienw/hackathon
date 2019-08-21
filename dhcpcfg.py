# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   project:       Python
   File Name:     dhcpTest
   Description :
   Author :       ASUS
   date:          2019/7/10 10:10
-------------------------------------------------
   Modify Activity:
                  2019/7/21 19:22
-------------------------------------------------
"""
__author__ = 'wangwei'

########
# fab -f dhcpCrud.py cat
# fab -f dhcpCrud.py CRUD
# fab -f dhcpCrud.py save
# fab -f dhcpCrud.py restart
########
from fabric import Connection


DHCPSERVER = 'itte@10.186.133.56'
DHCPSERVERPWD = 'itte'

def sshconn(host,connpwd):
    connect = Connection(host,connect_kwargs={"password": connpwd})
    return connect

def cat(conn):
    conn.run('cat /etc/dhcp/dhcpd.conf')

def edit(conn):
    conn.run('vi /etc/dhcp/dhcpd.conf')

def save(conn):
    conn.run('Esc:wq')

def restart(conn):
    conn.sudo('service isc-dhcp-server restart')


def CRUD(conn):
    local = 0
    flag = 0
    while flag == 0:

        print("*****************************************************")
        print("   0 --> Add function")
        print("   1 --> Delete function")
        print("   2 --> Modify function ")
        print("   3 --> Find function")
        choice = int(input("Please enter your option："))

        # filePath = r'C:\Users\weiwang\Desktop\dhcp.conf'
        filePath = ('dhcpd.conf')

        if choice == 0:
            print("*****************************************************")
            host_name = str(input("Please enter the host name you want to add： "))
            mac = str(input("Please enter the MAC address you want to add ： "))
            ip = str(input("Please enter the IP address you want to add ： "))
            Add(filePath, host_name, mac, ip)

        elif choice == 1:
            print("*****************************************************")
            print("Delete according to the options below：")
            print("    0 Hostname   -->  MAC address and IP address")
            print("    1 Mac address   -->  Host name and IP address")
            print("    2 Ip address --> Host name and MAC address")
            print("*****************************************************")
            choice_find = int(input("Please enter your option： "))
            local, selection = Find(filePath, choice_find)
            Delete(local, selection, filePath)

        elif choice == 2:
            print("*****************************************************")
            ch = int(input("Modify IP address or MAC address？ 0-ip or 1-mac： "))
            if ch == 0:
                str1 = str(input("Please enter the Ip to be modified： "))
                str2 = str(input("Please enter a new IP address： "))
                Modify(filePath, str1, str2, ch)
            elif ch == 1:
                str1 = str(input("Please enter the Mac to be modified： "))
                str2 = str(input("Please enter a new MAC address： "))
                Modify(filePath, str1, str2, ch)

        elif choice == 3:
            print("*****************************************************")
            print("Find function：")
            print("    0 Hostname   -->  Mac adderss and Ip address")
            print("    1 Mac address   -->  Hostname and Ip address")
            print("    2 Ip address --> Hostname and Mac address")
            print("*****************************************************")
            choice_find = int(input("Please enter the search option： "))
            local, selection = Find(filePath, choice_find)
        else:
            print("Error in input options ！！！")

        flag = int(input("Do you want to continue? ？ 0-Yes or 1-No： "))



"""
FIND function：
    0 Find MAC address and IP address based on host name 
    1 Find host name and IP address based on MAC address
    2 Find host name and MAC address based on IP address 
"""
def Find(filePath, choice_find):
    choice_find = choice_find
    f = open(filePath, "r")  # Setting File Objects
    data = f.readlines()  # Read the file line-by-line directly in the list 
    a = []

    for i in range(len(data)):
        a.append(data[i][:-1])

    if choice_find == 0:
        str0 = str(input("Please enter the host name ： "))
        flag = False # Indicators used to determine whether a successful search has been made 
        local = 0    # Used for storage to find successful locations 

        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j]==" ":
                    continue
                elif a[i][j]=="h" and a[i][j+1]=="o":
                    count = 0
                    for m in range(len(str0)):
                        if a[i][j+5+m] == str0[m]:
                            count = count + 1
                            continue
                        else:
                            break

                    if count == len(str0):
                        flag = True
                        local = i
                        break

        if flag == True:
            print("The information found is as follows： ")
            for i in range(4):
                print(a[local+i])
        else:
            print("No information was found！！！")

    elif choice_find == 2:
        str2 = str(input("Please enter IP address： "))
        flag = False  # Indicators used to determine whether a successful search has been made 
        local = 0  # Used for storage to find successful locations

        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == "#":
                    break
                if a[i][j] == " ":
                    continue
                elif a[i][j] == "f" and a[i][j + 1] == "i" and a[i][j + 2] == "x":
                    count = 0
                    for m in range(len(str2)):
                        if a[i][j + 14 + m] == str2[m]:
                            count = count + 1
                            continue
                        else:
                            break

                    if count == len(str2):
                        flag = True
                        local = i
                        break

        if flag == True:
            print("The information found is as follows： ")
            for i in range(4):
                print(a[local + i - 2])
        else:
            print("No information was found！！！")

    elif choice_find == 1:
        str3 = str(input("Please enter MAC address ： "))
        flag = False  # Indicators used to determine whether a successful search has been made 
        local = 0  # Used for storage to find successful locations 

        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == "#":
                    break
                if a[i][j] == " ":
                    continue
                elif a[i][j] == "h" and a[i][j+1] == "a" and a[i][j+2] == "r" and a[i][j+3] == "d":
                    count = 0
                    for m in range(len(str3)):
                        if a[i][j + 18 + m] == str3[m]:
                            count = count + 1
                            continue
                        else:
                            break

                    if count == len(str3):
                        flag = True
                        local = i
                        break

        if flag == True:
            print("The information found is as follows： ")
            for i in range(4):
                print(a[local + i - 1])
        else:
            print("No information was found ！！！")
    else:
        print("Error in input options ！！！")

    f.close()
    return local, choice_find


"""
Modifying Function Function：
            Modify IP address or MAC address
"""
def Modify(filePath, str1, str2, ch):
    str1 = str1 # IP to be modified (check first and delete later)
    str2 = str2  # IP to be modified (direct increase) 

    f = open(filePath, 'r+')
    lines = f.readlines()
    f.seek(0, 0)

    for line in lines:
        line_new = line.replace(str1, str2)
        f.write(line_new)
    f.close()

    if ch == 0:
        flag = False  # Indicators used to determine whether a successful search has been made 
        local = 0  #Used for storage to find successful locations 
        f = open(filePath, "r")  # Setting File Objects
        data = f.readlines()  # Read the file line-by-line directly in the list
        a = []

        for i in range(len(data)):
            a.append(data[i][:-1])

        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == "#":
                    break
                if a[i][j] == " ":
                    continue
                elif a[i][j] == "f" and a[i][j + 1] == "i" and a[i][j + 2] == "x":
                    count = 0
                    for m in range(len(str2)):
                        if a[i][j + 14 + m] == str2[m]:
                            count = count + 1
                            continue
                        else:
                            break

                    if count == len(str2):
                        flag = True
                        local = i
                        break

        host_name1 = a[local-2][14:-1]
        mac_name = a[local-1][34:-1]
        ip_name = a[local][30:-1]
        Delete(local, 2, filePath)
        Add(filePath, host_name1, mac_name, ip_name)

    print("Modify Successfully ！！！")


"""
Adding Function Function ：
            Add a message (host name, Mac address, IP address) 
"""


def Add(filePath, host_name, mac, ip):
    location = 0
    host_name = host_name
    mac = mac
    ip = ip
    ip_1 = int(ip[7:10])
    ip_2 = int(ip[11:])

    f = open(filePath, "r")  # Setting File Objects
    data = f.readlines()  # Read the file line-by-line directly in the list
    a = []

    for i in range(len(data)):
        a.append(data[i][:-1])

    count1 = count2 = count = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == "#":
                break
            if a[i][j] == " ":
                continue
            elif a[i][j] == "f" and a[i][j + 1] == "i" and a[i][j + 2] == "x":
                if a[i][j + 21] == '1' and a[i][j + 22] == '3' and a[i][j + 23] == '3':
                    count1 = count1 + 1
                if a[i][j + 21] == '1' and a[i][j + 22] == '9' and a[i][j + 23] == '8':
                    count2 = count2 + 1

    flag = 0
    isEnd = False
    for i in range(len(a)):
        if flag == 0:
            for j in range(len(a[i])):
                if a[i][j] == "#":
                    break
                if a[i][j] == " ":
                    continue
                elif a[i][j] == "f" and a[i][j + 1] == "i" and a[i][j + 2] == "x":
                    if ip_1 == int(a[i][j + 21:j + 24]) and ip_1 == 133:
                        if ip_2 > int(a[i][j + 25:-1]):
                            count = count + 1
                            # print("count: " + str(count))
                            if count1 == count:
                                location = i + 2
                                break
                        elif ip_2 == int(a[i][j + 25:-1]):
                            print("The IP address you entered already exists！！！")
                        elif ip_2 < int(a[i][j + 25:-1]):
                            location = i - 2
                            flag = 1
                            break

                    elif ip_1 == int(a[i][j + 21:j + 24]) and ip_1 == 198:
                        if ip_2 > int(a[i][j + 25:-1]):
                            count = count + 1
                            if count2 == count:
                                location = i + 1
                                isEnd = True
                        elif ip_2 == int(a[i][j + 25:-1]):
                            print("The IP address you entered already exists ！！！")
                        elif ip_2 < int(a[i][j + 25:-1]):
                            location = i - 2
                            flag = 1
                            break
        else:
            break

    f.close()

    lines = []
    f1 = open(filePath, 'r')
    for line in f1.readlines():
        lines.append(line)
    f1.close()

    if isEnd:
        lines.append("\n")
        lines.append("         host " + host_name + "{\n")
        lines.append("                hardware ethernet " + mac + ";\n")
        lines.append("                fixed-address " + ip + ";\n")
        lines.append("        }")
    else:
        lines.insert(location, "         host " + host_name + "{\n")
        lines.insert(location + 1, "                hardware ethernet " + mac + ";\n")
        lines.insert(location + 2, "                fixed-address " + ip + ";\n")
        lines.insert(location + 3, "        }\n")

    fp = open(filePath, 'w')
    for s in lines:
        fp.write(s)
    fp.close()
    print("Add Successfully ！！！")


"""
Delete function ：
            Delete a message (host name, Mac address, IP address) 
"""
def Delete(local, selection, filePath):
    f = open(filePath, 'r')
    LIST = f.readlines()

    if selection == 0: # Delete information according to host name 
        for i in range(4):
            del LIST[local]
    elif selection == 1: # Delete information according to MAC address 
        for i in range(4):
            del LIST[local-1]
    elif selection == 2: # Delete information according to IP address 
        for i in range(4):
            del LIST[local-2]

    f.close()
    f1 = open(filePath, 'w')
    f1.writelines(LIST)
    f1.close()
    print("Delete Successfully ！！！")

if __name__ == '__main__':
    conn1=sshconn(DHCPSERVER, DHCPSERVERPWD)
    cat(conn1)
    CRUD(conn1)





