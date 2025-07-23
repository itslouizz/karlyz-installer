import os
import sys
import subprocess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def install_tool(tool, system):
    clear()
    print(f"\033[31mInstalling {tool} on {system}...\033[0m")
    try:
        if tool in ["maxphisher", "zphisher"]:
            if system == "Kali Linux":
                subprocess.run(['sudo', 'git', 'clone', f'https://github.com/{tool}/{tool}.git', f'/opt/{tool}'], check=True)
                subprocess.run(['sudo', 'chmod', '-R', '755', f'/opt/{tool}'], check=True)
                subprocess.run(['sudo', 'bash', f'/opt/{tool}/install.sh'], check=True)
            elif system == "Termux":
                subprocess.run(['git', 'clone', f'https://github.com/{tool}/{tool}.git', f'~/../usr/opt/{tool}'], check=True)
                subprocess.run(['chmod', '-R', '755', f'~/../usr/opt/{tool}'], check=True)
                subprocess.run(['bash', f'~/../usr/opt/{tool}/install.sh'], check=True)
        elif tool == "gophish":
            if system == "Kali Linux":
                subprocess.run(['sudo', 'wget', 'https://github.com/gophish/gophish/releases/download/v0.12.1/gophish-v0.12.1-linux-64bit.zip', '-O', '/opt/gophish.zip'], check=True)
                subprocess.run(['sudo', 'unzip', '/opt/gophish.zip', '-d', '/opt/gophish'], check=True)
                subprocess.run(['sudo', 'chmod', '+x', '/opt/gophish/gophish'], check=True)
            elif system == "Termux":
                print("\033[31mGoPhish is not recommended for Termux due to size constraints\033[0m")
                input("\nPress Enter to continue...")
                return
        else:
            if system == "Kali Linux":
                cmd = ['sudo', 'apt', 'install', '-y', tool]
            elif system == "Termux":
                cmd = ['pkg', 'install', '-y', tool]
            elif system == "Docker":
                cmd = ['docker', 'run', '-it', 'kalilinux/kali-rolling:latest', 'apt', 'install', '-y', tool]
            elif system == "Arch Linux":
                cmd = ['sudo', 'pacman', '-S', '--noconfirm', tool]
            subprocess.run(cmd, check=True)
        print(f"\033[31m{tool} installed successfully!\033[0m")
    except Exception as e:
        print(f"\033[31mFailed to install {tool}: {str(e)}\033[0m")
    input("\nPress Enter to continue...")

def select_os(tool):
    while True:
        clear()
        if tool in ["maxphisher", "zphisher"]:
            choice = input("\033[31mSelect your system:\n--\n[1] Kali Linux\n[2] Termux\n[3] Back\n~~> \033[0m")
            systems = {"1": "Kali Linux", "2": "Termux"}
        elif tool == "gophish":
            choice = input("\033[31mSelect your system:\n--\n[1] Kali Linux\n[2] Back\n~~> \033[0m")
            systems = {"1": "Kali Linux"}
        else:
            choice = input("\033[31mSelect your system:\n--\n[1] Kali Linux\n[2] Termux\n[3] Docker\n[4] Arch Linux\n[5] Back\n~~> \033[0m")
            systems = {"1": "Kali Linux", "2": "Termux", "3": "Docker", "4": "Arch Linux"}
        
        if choice == str(len(systems)+1):
            break
        elif choice in systems:
            install_tool(tool, systems[choice])

def tools_menu():
    tools = {
        "1": "nmap",                "15": "gobuster",           "29": "hashcat",            "43": "sublist3r",
        "2": "metasploit-framework", "16": "wifite",             "30": "feroxbuster",        "44": "amass",
        "3": "wireshark",           "17": "reaver",             "31": "ghidra",             "45": "whatweb",
        "4": "burpsuite",           "18": "yersinia",           "32": "binwalk",            "46": "wpscan",
        "5": "john",                "19": "openvas",            "33": "stegseek",           "47": "joomscan",
        "6": "hydra",               "20": "bloodhound",         "34": "stegcracker",        "48": "droopescan",
        "7": "sqlmap",              "21": "crackmapexec",       "35": "fcrackzip",          "49": "snmp-check",
        "8": "aircrack-ng",         "22": "impacket-scripts",   "36": "hashid",             "50": "onesixtyone",
        "9": "nikto",               "23": "sherlock",           "37": "netcat",             "51": "braa",
        "10": "maltego",            "24": "dnsenum",            "38": "socat",              "52": "cewl",
        "11": "theharvester",       "25": "routersploit",       "39": "enum4linux",         "53": "crunch",
        "12": "responder",          "26": "maxphisher",         "40": "smbclient",          "54": "cupp",
        "13": "setoolkit",          "27": "zphisher",           "41": "wfuzz",              "55": "evil-winrm",
        "14": "commix",             "28": "gophish",            "42": "dirb",               "56": "rdesktop"
    }
    while True:
        clear()
        choice = input("""\033[31mKarlyz Installer v1 | itslouizz on github
--
[1] Nmap               [15] Gobuster           [29] Hashcat            [43] Sublist3r
[2] Metasploit         [16] Wifite             [30] Feroxbuster        [44] Amass
[3] Wireshark          [17] Reaver             [31] Ghidra             [45] WhatWeb
[4] Burp Suite         [18] Yersinia           [32] Binwalk            [46] WPScan
[5] John the Ripper    [19] OpenVAS            [33] Stegseek           [47] Joomscan
[6] Hydra              [20] BloodHound         [34] Stegcracker        [48] Droopescan
[7] SQLmap             [21] CrackMapExec       [35] Fcrackzip          [49] SNMP-Check
[8] Aircrack-ng        [22] Impacket           [36] Hashid             [50] Onesixyone
[9] Nikto              [23] Sherlock           [37] Netcat             [51] Braa
[10] Maltego           [24] DNSenum            [38] Socat              [52] CeWL
[11] TheHarvester      [25] RouterSploit       [39] Enum4linux         [53] Crunch
[12] Responder         [26] MaxPhisher         [40] Smbclient          [54] Cupp
[13] SEToolkit         [27] Zphisher           [41] Wfuzz              [55] Evil-WinRM
[14] Commix            [28] GoPhish            [42] Dirb               [56] Rdesktop
[57] Back
~~> \033[0m""")
        
        if choice == "57":
            break
        elif choice in tools:
            select_os(tools[choice])

def main_menu():
    while True:
        clear()
        choice = input("\033[31mKarlyz Installer v1 | itslouizz on github\n--\n[1] Install Tools\n[2] Exit\n~~> \033[0m")
        
        if choice == "1":
            tools_menu()
        elif choice == "2":
            sys.exit(0)

if __name__ == "__main__":
    main_menu()