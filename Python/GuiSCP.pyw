import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import subprocess
from subprocess import Popen, CREATE_NEW_CONSOLE, check_output
import os
import time

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

class HelloView(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.lIp = tk.StringVar()
        self.lUsername = tk.StringVar()
        self.lPass = tk.StringVar()
        self.lIp = tk.StringVar()
        self.rDir = tk.StringVar( value="flash0")
        self.fName = tk.StringVar(value="name.bin")
        self.rPass = tk.StringVar(value="")
        self.rUsername = tk.StringVar(value="r/s-username")
        self.rIp = tk.StringVar(value="0.0.0.0")

        self.statUs = tk.StringVar()
        self.statUs.set(value="Not complete")
        self.statUs2 = tk.StringVar()
        self.statUs2.set(value="Not complete")
        self.statUs3 = tk.StringVar()
        self.statUs3.set(value="Not complete")
        self.statUs4 = tk.StringVar()
        self.statUs4.set(value="Not complete")
        self.statUs5a = tk.StringVar()
        self.statUs5a.set(value="")
        self.statUs5b = tk.StringVar()
        self.statUs5b.set(value="")
        self.statUs5c = tk.StringVar()
        self.statUs5c.set(value="")
        self.statUs5d = tk.StringVar()
        self.statUs5d.set(value="")
        self.statUs5e = tk.StringVar()
        self.statUs5e.set(value="")
        self.scpCmd = tk.StringVar()
        self.scpCmd.set("SCP Command:")
        self.hello_string = tk.StringVar()
        self.hello_string.set("SCP Command:")



        lIp_label = ttk.Label(self, text="linux box IP:")
        lIp_entry = ttk.Entry(self, textvariable=self.lIp)
        lUsername_label = ttk.Label(self, text="linux box User:")
        lUsername_entry = ttk.Entry(self, textvariable=self.lUsername)
        lPass_label = ttk.Label(self, text="linux box Pass:")
        lPass_entry = ttk.Entry(self, textvariable=self.lPass, show='*')
        rIp_label = ttk.Label(self, text="R/S IP:")
        rIp_entry = ttk.Entry(self, textvariable=self.rIp)
        rUsername_label = ttk.Label(self, text="R/S username:")
        rUsername_entry = ttk.Entry(self, textvariable=self.rUsername)
        rPass_label = ttk.Label(self, text="R/S password:")
        rPass_entry = ttk.Entry(self, textvariable=self.rPass, show='*')
        fName_label = ttk.Label(self, text="file name:")
        fName_entry = ttk.Entry(self, textvariable=self.fName)
        fName_button = tk.Button(self, bg="white", text="       file         ", command=self.on_fname)
        rDir_label = ttk.Label(self, text="R/S directory:")
        rDir_entry = ttk.Entry(self, textvariable=self.rDir)
        stp1_button = ttk.Button(self, text="Step 1",
                               command=self.on_stp1)
        stp1_label = ttk.Label(self, text="SCP to linux box")
        stp1_label2 = tk.Label(self, bg="white", textvariable=self.statUs)
        stp2_button = ttk.Button(self, text="step 2",
                               command=self.on_stp2)
        stp2_label = ttk.Label(self, text="MD5 check linux box file")
        stp2_label2 = tk.Entry(self, bg="gray85", textvariable=self.statUs2)
        stp3_button = ttk.Button(self, text="step 3",
                               command=self.on_stp3)
        stp3_label = ttk.Label(self, text="Display Router SCP Command")
        stp3_label2 = tk.Label(self, bg="white", textvariable=self.statUs3)
        stp4_button = ttk.Button(self, text="step 4",
                                 command=self.on_stp4)
        stp4_label = ttk.Label(self, text="Open session to SCP to R/S")
        stp4_label2 = tk.Label(self, bg="white", textvariable=self.statUs4)
        scpCmd_label = ttk.Label(self, text="SCP Command:")
        scpCmd_entry = ttk.Entry(self, textvariable=self.scpCmd)
        stp6_button = tk.Button(self, bg="white", text=" Copy Text ",
                                 command=self.on_copy)

        stp5_buttonb = tk.Button(self, fg="white", bg="black", text="Close Help",
                                command=self.off_issue)
        stp5_buttonc = tk.Button(self, fg="white", bg="black", text="",
                                 command=self.off_rs)
        stp5_button = tk.Button(self, fg="white", bg="black",text="Open Help",
                                 command=self.on_issue)
        stp5_label1 = tk.Label(self, bg="yellow", textvariable=self.statUs5a)
        stp5_label2 = tk.Label(self, bg="yellow", textvariable=self.statUs5b)
        stp5_label3 = tk.Label(self, bg="yellow", textvariable=self.statUs5c)
        stp5_label4 = tk.Label(self, bg="yellow", textvariable=self.statUs5d)
        stp5_label5 = tk.Label(self, bg="yellow", textvariable=self.statUs5e)



        lIp_label.grid(row=0, column=0, sticky=tk.W)
        lIp_entry.grid(row=0, column=1, sticky=(tk.W + tk.E))
        lUsername_label.grid(row=1, column=0, sticky=tk.W)
        lUsername_entry.grid(row=1, column=1, sticky=(tk.W + tk.E))
        lPass_label.grid(row=2, column=0, sticky=tk.W)
        lPass_entry.grid(row=2, column=1, sticky=(tk.W + tk.E))
        stp1_button.grid(row=0, column=2, sticky=tk.E)
        stp1_label.grid(row=0, column=3, sticky=tk.W)
        stp1_label2.grid(row=0, column=4, sticky=tk.W)
        stp2_button.grid(row=1, column=2, sticky=tk.W)
        stp2_label.grid(row=1, column=3, sticky=tk.W)
        stp2_label2.grid(row=1, column=4, sticky=tk.W)
        stp3_button.grid(row=2, column=2, sticky=tk.W)
        stp3_label.grid(row=2, column=3, sticky=tk.W)
        stp3_label2.grid(row=2, column=4, sticky=tk.W)
        stp4_button.grid(row=3, column=2, sticky=tk.E)
        stp4_label.grid(row=3, column=3, sticky=tk.W)
        stp4_label2.grid(row=3, column=4, sticky=tk.W)
        rIp_label.grid(row=3, column=0, sticky=tk.W)
        rIp_entry.grid(row=3, column=1, sticky=(tk.W + tk.E))
        rUsername_label.grid(row=4, column=0, sticky=tk.W)
        rUsername_entry.grid(row=4, column=1, sticky=(tk.W + tk.E))
        rPass_label.grid(row=5, column=0, sticky=tk.W)
        rPass_entry.grid(row=5, column=1, sticky=(tk.W + tk.E))
        fName_label.grid(row=6, column=0, sticky=tk.W)
        fName_entry.grid(row=6, column=1, sticky=(tk.W + tk.E))
        fName_button.grid(row=6, column=2, sticky=(tk.W))
        rDir_label.grid(row=7, column=0, sticky=tk.W)
        rDir_entry.grid(row=7, column=1, sticky=(tk.W + tk.E))
        scpCmd_label.grid(row=8, column=0,sticky=(tk.W + tk.E))
        scpCmd_entry.grid(row=8, column=1, sticky=(tk.W + tk.E))
        stp5_button.grid(row=7, column=4, sticky=tk.E)
        stp5_buttonb.grid(row=8, column=4, sticky=tk.E)
        stp5_buttonc.grid(row=8, column=4, sticky=tk.W)
        stp6_button.grid(row=8, column=2, sticky=tk.W)
      #  stp5_label1.grid(row=4, column=5, sticky=tk.W)
      #  stp5_label2.grid(row=5, column=5, sticky=tk.W)
        stp5_label3.grid(row=6, column=5, sticky=tk.W)
        stp5_label4.grid(row=7, column=5, sticky=tk.W)
        stp5_label5.grid(row=8, column=5, sticky=tk.W)
        self.columnconfigure(9, weight=1)



    def on_stp1(self):
        Popen("pscp -scp -l " + self.lUsername.get() + " -pw " + self.lPass.get() +
                       " " + self.fName.get() + ' ' + self.lIp.get()
                      + ":", creationflags=CREATE_NEW_CONSOLE)
        self.statUs.set('complete')
        return ;


    def on_stp2(self):
        self.statUs2a = tk.StringVar()
        self.statUs2a.set(value="")
        file_name = os.path.basename(self.fName.get())
        self.fName.set((os.path.splitext(file_name)[0]) + (os.path.splitext(file_name)[1]))
        self.statUs2.set(check_output("plink -ssh -l " + self.lUsername.get() + " -pw " + self.lPass.get() + ' ' +
                                      self.lIp.get() + ' md5sum ' + self.fName.get()))


        return ;

    def on_stp3(self):
        file_name = os.path.basename(self.fName.get())
        self.fName.set((os.path.splitext(file_name)[0]) + (os.path.splitext(file_name)[1]))
        if self.rUsername.get().strip():
            self.scpCmd.set("scp " + self.fName.get() + " " + self.rUsername.get() + "@" +
                            self.rIp.get() + ":" + self.rDir.get() + ":/" + self.fName.get())

        else:
            self.scpCmd.set("SCP Command:")
        self.statUs3.set('Command Displayed')
        return ;

    def on_stp4(self):
        Popen("putty -ssh -l " + self.lUsername.get() + " -pw " + self.lPass.get() + " " + self.lIp.get(),
                        shell=True)
        self.statUs4.set('Session Opened')
        return ;

    def on_fname(self):
        self.fName.set(askopenfilename())

    def on_issue(self):
        self.statUs5c.set("Is SCP enabled on r/s? Do: ip scp server enable")
        self.statUs5d.set("Is directory correct?  Do: Dir command")
        self.statUs5e.set("Is R/S space full? Do: delete flash:filename")

    def off_issue(self):
        self.statUs5c.set("")
        self.statUs5d.set("")
        self.statUs5e.set("")

    def off_rs(self):
        self.statUs4.set("Not complete")
        self.statUs3.set("Not complete")
        self.statUs2.set("Not complete")
        self.statUs.set("Not complete")

    def on_copy(self):
        copy2clip(self.scpCmd.get())



class MyApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("SCP-Tool")
        self.resizable(width=False, height=False)
        HelloView(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)

if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
