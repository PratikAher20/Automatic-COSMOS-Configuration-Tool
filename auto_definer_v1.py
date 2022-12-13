import csv
import pandas as pd
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

cwd = Path.cwd()
config_path = cwd.parent
targets_path = config_path / Path('targets')

# Declaring the Target
target_name = StringVar


def configTarget():
    tar_root = Tk()
    tar_root.iconbitmap("cosmos_icon.ico")
    tar_root.title("Target Configuration")
    tar_root.geometry("300x150")
    label = ttk.Label(tar_root, text="Enter Name of the Target", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    e = Entry(tar_root)
    e.pack()

    def save():
        global target_name
        target_name = e.get()
        system_dir = "system"
        system_path = os.path.join(config_path, system_dir)
        system_txt = open(system_path + "\\" + "system.txt", "r")
        system_lines = system_txt.readlines()
        system_lines[10] = "DECLARE_TARGET " + target_name + "\n"

        system_txt = open(system_path + "\\" + "system.txt", "w")
        system_txt.writelines(system_lines)
        system_txt.close()

        # target_directory = target_name
        # path_of_your_target = os.path.join(targets_path, target_directory)
        # os.mkdir(path_of_your_target)
        #
        # cmd_tlm_dir = "cmd_tlm"
        # cmd_tlm_path = os.path.join(path_of_your_target, cmd_tlm_dir)
        # os.mkdir(cmd_tlm_path)
        #
        # lib_dir = "lib"
        # lib_path = os.path.join(path_of_your_target, lib_dir)
        # os.mkdir(lib_path)

    savebutton = Button(tar_root, text="SAVE", command=save).pack(pady=10)
    okbutton = Button(tar_root, text="OK", command=tar_root.destroy).pack()


# Interfacing the Target

tools_dir = "tools"
tools_path = os.path.join(config_path, tools_dir)
cmd_tlm_server_dir = "cmd_tlm_server"
cmd_tlm_server_path = os.path.join(tools_path, cmd_tlm_server_dir)
cmd_tlm_server_file = open(cmd_tlm_server_path + "\\" + "cmd_tlm_server.txt", 'a')


def tcpipserver():
    tcpc = Tk()
    tcpc.iconbitmap("cosmos_icon.ico")
    tcpc.title("TCPIP SERVER Interface")
    label = Label(tcpc, text="Write Port*").grid(row=0, column=0, pady=20, padx=5)
    label = Label(tcpc, text="Read Port*").grid(row=1, column=0, pady=20, padx=5)
    label = Label(tcpc, text="Write Timeout*").grid(row=2, column=0, pady=20, padx=5)
    label = Label(tcpc, text="Read Timeout*").grid(row=3, column=0, pady=20, padx=5)
    label = Label(tcpc, text="Prototype*").grid(row=4, column=0, pady=20, padx=5)

    e0 = Entry(tcpc)
    e0.grid(row=0, column=1, pady=20, padx=5)
    e1 = Entry(tcpc)
    e1.grid(row=1, column=1, pady=20, padx=5)
    e2 = Entry(tcpc)
    e2.grid(row=2, column=1, pady=20, padx=5)
    e3 = Entry(tcpc)
    e3.grid(row=3, column=1, pady=20, padx=5)
    proto_list = [
        "BURST",
        "FIXED",
        "LENGTH",
        "TERMINATED",
        "PREIDENTIFIED",
        "TEMPLATE"
    ]

    def selected(event):
        if (clicked.get() == "BURST"):
            b = Tk()
            b.iconbitmap("cosmos_icon.ico")
            b.title("BURST Protocol")
            label = Label(b, text="Discard Leading Bytes()").grid(row=0, column=0, pady=20, padx=5)
            label = Label(b, text="Sync Pattern(Hex string representing a byte pattern will be searched)").grid(row=1,
                                                                                                                column=0,
                                                                                                                pady=20,
                                                                                                                padx=5)
            label = Label(b, text="Fill Sync Pattern which will add on top of Outgoing Packet").grid(row=2, column=0,
                                                                                                     pady=20, padx=5)
            ee0 = Entry(b)
            ee0.grid(row=0, column=1, pady=20, padx=5)
            ee1 = Entry(b)
            ee1.grid(row=1, column=1, pady=20, padx=5)
            cc = StringVar()

            def sel(event):
                global target_name
                cmd_tlm_server_file.write(
                    "\nINTERFACE " + target_name + "_INT " + "tcpip_server_interface.rb " + e0.get() + " " + e1.get() + " " + e2.get() + " " + e3.get() + " " + "BURST " + ee0.get() + " " + ee1.get() + " " + cc.get() + "\n  TARGET " + target_name)
                okbutton = Button(b, text="OK", command=b.destroy).grid(row=3, column=1, pady=20, padx=5)

            proto_menu = OptionMenu(b, cc, "true", "false", command=sel).grid(row=2, column=1, pady=20, padx=5)

        if (clicked.get() == "FIXED"):
            b = Tk()
            b.iconbitmap("cosmos_icon.ico")
            b.title("FIXED Protocol")
            label = Label(b, text="Minimum ID_Size(Minimum Amount of bytes needed to identify the packet)").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 pady=20,
                                                                                                                 padx=5)
            label = Label(b, text="Discard Leading Bytes()").grid(row=1, column=0, pady=20, padx=5)
            label = Label(b, text="Sync Pattern(Hex string representing a byte pattern will be searched)").grid(row=2,
                                                                                                                column=0,
                                                                                                                pady=20,
                                                                                                                padx=5)
            label = Label(b, text="Whether the stream is returning Telemetry").grid(row=3, column=0, pady=20, padx=5)
            label = Label(b, text="Fill Sync Pattern which will add on top of Outgoing Packet").grid(row=4, column=0,
                                                                                                     pady=20, padx=5)
            ee0 = Entry(b)
            ee0.grid(row=0, column=1, pady=20, padx=5)
            ee1 = Entry(b)
            ee1.grid(row=1, column=1, pady=20, padx=5)
            ee2 = Entry(b)
            ee2.grid(row=2, column=1, pady=20, padx=5)
            cc0 = StringVar()
            cc1 = StringVar()

            def sel(event):
                global target_name
                cmd_tlm_server_file.write(
                    "\nINTERFACE " + target_name + "_INT " + "tcpip_server_interface.rb " + e0.get() + " " + e1.get() + " " + e2.get() + " " + e3.get() + " " + e4.get() + " " + "FIXED " + ee0.get() + " " + ee1.get() + " " + cc0.get() + " " + cc1.get() + "\n  TARGET " + target_name)
                okbutton = Button(b, text="OK", command=b.destroy).grid(row=5, column=1, pady=20, padx=5)

            proto_menu = OptionMenu(b, cc0, "true", "false").grid(row=3, column=1, pady=20, padx=5)
            proto_menu = OptionMenu(b, cc1, "true", "false", command=sel).grid(row=4, column=1, pady=20, padx=5)

    clicked = StringVar()
    proto_menu = OptionMenu(tcpc, clicked, *proto_list, command=selected).grid(row=4, column=1, pady=20, padx=5)




def serial():
    seri = Tk()
    seri.iconbitmap("cosmos_icon.ico")
    seri.title("UDP Interface")
    label = Label(seri, text="Write Port*").grid(row=0, column=0, pady=20, padx=5)
    label = Label(seri, text="Read Port*").grid(row=1, column=0, pady=20, padx=5)
    label = Label(seri, text="Baud Rate*").grid(row=2, column=0, pady=20, padx=5)
    label = Label(seri, text="Parity*").grid(row=3, column=0, pady=20, padx=5)
    label = Label(seri, text="Stop Bits*").grid(row=4, column=0, pady=20, padx=5)
    label = Label(seri, text="Write Timeout*").grid(row=5, column=0, pady=20, padx=5)
    label = Label(seri, text="Read Timwout*").grid(row=6, column=0, pady=20, padx=5)
    label = Label(seri, text="Protocol Type*").grid(row=7, column=0, pady=20, padx=5)

    e0 = Entry(seri)
    e0.grid(row=0, column=1, pady=20, padx=5)
    e1 = Entry(seri)
    e1.grid(row=1, column=1, pady=20, padx=5)
    e2 = Entry(seri)
    e2.grid(row=2, column=1, pady=20, padx=5)

    e4 = Entry(seri)
    e4.grid(row=4, column=1, pady=20, padx=5)
    e5 = Entry(seri)
    e5.grid(row=5, column=1, pady=20, padx=5)
    e6 = Entry(seri)
    e6.grid(row=6, column=1, pady=20, padx=5)
    proto_list = [
        "BURST",
        "FIXED",
        "LENGTH",
        "TERMINATED",
        "PREIDENTIFIED",
        "TEMPLATE"
    ]

    def selected(event):
        if (clicked.get() == "BURST"):
            b = Tk()
            b.iconbitmap("cosmos_icon.ico")
            b.title("BURST Protocol")
            label = Label(b, text="Discard Leading Bytes()").grid(row=0, column=0, pady=20, padx=5)
            label = Label(b, text="Sync Pattern(Hex string representing a byte pattern will be searched)").grid(row=1,
                                                                                                                column=0,
                                                                                                                pady=20,
                                                                                                                padx=5)
            label = Label(b, text="Fill Sync Pattern which will add on top of Outgoing Packet").grid(row=2, column=0,
                                                                                                     pady=20, padx=5)
            ee0 = Entry(b)
            ee0.grid(row=0, column=1, pady=20, padx=5)
            ee1 = Entry(b)
            ee1.grid(row=1, column=1, pady=20, padx=5)
            cc = StringVar()

            def sel(event):
                global target_name
                cmd_tlm_server_file.write(
                    "\nINTERFACE " + target_name + "_INT " + "serial_interface.rb " + e0.get() + " " + e1.get() + " " + e2.get() + " " + clicked0.get() + " " + e4.get() + " " + e5.get() + " " + e6.get() + " " + cc.get() + "\n  TARGET " + target_name)
                okbutton = Button(b, text="OK", command=b.destroy).grid(row=3, column=1, pady=20, padx=5)

            proto_menu = OptionMenu(b, cc, "true", "false", command=sel).grid(row=2, column=1, pady=20, padx=5)

        if (clicked.get() == "FIXED"):
            b = Tk()
            b.iconbitmap("cosmos_icon.ico")
            b.title("FIXED Protocol")
            label = Label(b, text="Minimum ID_Size(Minimum Amount of bytes needed to identify the packet)").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 pady=20,
                                                                                                                 padx=5)
            label = Label(b, text="Discard Leading Bytes()").grid(row=1, column=0, pady=20, padx=5)
            label = Label(b, text="Sync Pattern(Hex string representing a byte pattern will be searched)").grid(row=2,
                                                                                                                column=0,
                                                                                                                pady=20,
                                                                                                                padx=5)
            label = Label(b, text="Whether the stream is returning Telemetry").grid(row=3, column=0, pady=20, padx=5)
            label = Label(b, text="Fill Sync Pattern which will add on top of Outgoing Packet").grid(row=4, column=0,
                                                                                                     pady=20, padx=5)
            ee0 = Entry(b)
            ee0.grid(row=0, column=1, pady=20, padx=5)
            ee1 = Entry(b)
            ee1.grid(row=1, column=1, pady=20, padx=5)
            ee2 = Entry(b)
            ee2.grid(row=2, column=1, pady=20, padx=5)
            cc0 = StringVar()
            cc1 = StringVar()

            def sel(event):
                global target_name
                cmd_tlm_server_file.write(
                    "\nINTERFACE " + target_name + "_INT " + "serial_interface.rb " + e0.get() + " " + e1.get() + " " + e2.get() + " " + e3.get() + " " + e4.get() + " " + "FIXED " + ee0.get() + " " + ee1.get() + " " + cc0.get() + " " + cc1.get() + "\n  TARGET " + target_name)
                okbutton = Button(b, text="OK", command=b.destroy).grid(row=5, column=1, pady=20, padx=5)

            proto_menu = OptionMenu(b, cc0, "true", "false").grid(row=3, column=1, pady=20, padx=5)
            proto_menu = OptionMenu(b, cc1, "true", "false", command=sel).grid(row=4, column=1, pady=20, padx=5)

    clicked0 = StringVar()
    parity = OptionMenu(seri, clicked0, "NONE", "EVENT", "ODD").grid(row=3, column=1, pady=20, padx=5)
    clicked = StringVar()
    proto_menu = OptionMenu(seri, clicked, *proto_list, command=selected).grid(row=7, column=1, pady=20, padx=5)


# cmd_tlm_server_content = cmd_tlm_server_file.readlines()
#
# #INTERFACE target_name_INT tcpip_server_interface.rb 50000 50001 2 100 BURST 16 "92A65A624040608486A8404040E103F0"
# interface= "INTERFACE "+ target_name + "_INT " +
# cmd_tlm_server_file.write('')


root = Tk()
# widthxHeight
root.title("Automatic COSMOS Configuration Tool")
root.iconbitmap("cosmos_icon.ico")
root.geometry("1100x400")
cos_img = PhotoImage(file="COSMOS.png", )
cos_label = Label(image=cos_img)
cos_label.pack(side=LEFT)

text2 = Text(root, height=400, width=300)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Verdana', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 16, 'bold'))
text2.tag_configure('color',
                    foreground='#476042',
                    font=('Verdana', 12, 'bold'))
text2.tag_bind('follow',
               '<1>',
               lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
text2.insert(END, '\nHow to Use\n', 'big')
quote = """
This application can be used to configure 
COSMOS Ground Station Software. Follow the 
following steps to confiure your Target! :

1. Click Target-> Enter the name of your target. 
   Click-> Save. Click->Ok
2. Click Interface-> Select the type of Interface
    Fill all the required parameters and Click->Ok. You can close the interface tab.
3. Click Configure-> Select the Excel File which is saved in this Project's Directory.

DONE!! Your COSMOS Target is ready to use.

"""
text2.insert(END, quote, 'color')
text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

menu = Menu(root)
root.config(menu=menu)
targetmenu = Menu(menu)
menu.add_cascade(label="Target", menu=targetmenu)
targetmenu.add_command(label="Configure Target", command=configTarget)

interfacemenu = Menu(menu)
menu.add_cascade(label="Interface", menu=interfacemenu)
interfacemenu.add_command(label="TCPIP SERVER INTERFACE", command=tcpipserver)
interfacemenu.add_command(label="SERIAL INTERFACE", command=serial)


def popupmsg(title, msg):
    popup = Tk()
    popup.wm_title(title)
    popup.iconbitmap("cosmos_icon.ico")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


# Configuring the Packet Definition

def configure():
    filename = (filedialog.askopenfilename(initialdir=cwd, title="Select a File"))

    target_directory = target_name
    path_of_your_target = os.path.join(targets_path, target_directory)
    os.mkdir(path_of_your_target)

    cmd_tlm_dir = "cmd_tlm"
    cmd_tlm_path = os.path.join(path_of_your_target, cmd_tlm_dir)
    os.mkdir(cmd_tlm_path)

    lib_dir = "lib"
    lib_path = os.path.join(path_of_your_target, lib_dir)
    os.mkdir(lib_path)

    ccsds_def = pd.read_excel(filename, sheet_name='ccsds_def')
    ccsds_def.to_csv('ccsds_def.csv', index=False)
    packet_def = pd.read_excel(filename, sheet_name='packet_def')
    packet_def.to_csv('packet_def.csv', index=False)
    ccsds_def = pd.read_excel(filename, sheet_name='packet_list')
    ccsds_def.to_csv('packet_list.csv', index=False)

    ccsds = open(r'ccsds_def.csv', 'r')
    target = open(cmd_tlm_path + "\\" + "_ccsds_tlm.txt", 'w')
    ccsdsread = csv.reader(ccsds)
    next(ccsdsread)
    for row in ccsdsread:
        if row[0] == 'CCSDSAPID':
            str = 'APPEND_ID_ITEM'
            for i in range(4):
                str += '\t'
                if i == 3:
                    str += ('<%= apid %>' + '\t')
                if i == 3:
                    str += '\"'
                str += row[i]
                if i == 3:
                    str += '\"'
            target.write(str + '\n')
            continue
        str = 'APPEND_ITEM'
        for i in range(5):
            str += '\t'
            if i == 3:
                str += '\"'
            str += row[i]
            if i == 3:
                str += '\"'
        target.write(str + '\n')
    ccsds.close()
    target.close()

    pkts = open(r'packet_def.csv', 'r')
    target2 = open(cmd_tlm_path + "\\" + "packets_tlm.txt", 'w')
    pktid = open(r'packet_list.csv', 'r')
    ccsdsread = csv.reader(pkts)
    pktidread = csv.reader(pktid)
    next(ccsdsread)
    next(pktidread)
    units = {'C': 'CELSIUS', 'A': 'AMPERE', 'V': 'VOLTAGE', 'W': 'POWER', 'RPM': 'ROTATIONS_PER_MINUTE'}
    for row in ccsdsread:
        if row[1]:
            strn = 'APPEND_ITEM'
            for i in range(5):
                strn += '\t'
                if i == 1:
                    row[i] = '{}'.format(int(float(row[i])))
                if i == 3:
                    strn += '\"'
                strn += row[i]
                if i == 3:
                    strn += '\"'
            target2.write(strn + '\n')
            if row[5]:
                states = row[5].split()
                for state in states:
                    str1 = '\t' + 'STATE'
                    splitstate = state.split('/')
                    str1 += '\t' + splitstate[1]
                    str1 += '\t' + splitstate[0]
                    target2.write(str1 + '\n')
            if row[6]:
                str3 = '\t' + 'UNITS '
                str3 += (units[row[6]] + ' ')
                str3 += row[6]
                target2.write(str3 + '\n')
            if row[7]:
                str2 = '\t' + 'POLY_READ_CONVERSION'
                str2 += (' ' + row[7])
                if row[8]:
                    str2 += (' ' + row[8])
                    if row[9]:
                        str2 += (' ' + row[9])
                        if row[10]:
                            str2 += (' ' + row[10])
                            if row[11]:
                                str2 += (' ' + row[11])
                target2.write(str2 + '\n')
        else:
            target2.write('\n')
            row = next(pktidread)
            str3 = 'TELEMETRY IS1 '
            str3 += row[0]
            str3 += ' BIG_ENDIAN'
            target2.write(str3 + '\n' + '\n')
            str4 = '<%= render "_ccsds_tlm.txt", locals: {apid: '
            str4 += row[1]
            str4 += '} %>'
            target2.write(str4 + '\n')
    pktid.close()
    pkts.close()
    target2.close()
    popupmsg("Successfull", "DONE!! COSMOS IS READY TO LAUNCH")


configmenu = Menu(menu)
menu.add_cascade(label="Configure", menu=configmenu)
configmenu.add_command(label="Select Excel File", command=configure)


def about():
    popupmsg("About", "COSMOS Automatic Configuration GUI: -\n"
                      "Created By: - Pratik Aher & Samedh Kari\n ")


helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

root.mainloop()


