# port_scanner
A simple port scanner just for learning about the socket library.
# 🔍 Simple Port Scanner with Python

A small and simple script to scan ports of a target (IP or domain).  
I wrote this for practice to learn about sockets and port scanning.

---

## 🚀 How to run?

It's super easy! Just:

1. Make sure Python is installed.
2. Run the file:
```bash
python port_scanner.py
```
3. Enter the IP or domain you want to scan.
4. Enter the start and end port range (between 20 and 100).
5. See the results!

---

## ⚙️ Limitations

To keep the scan light and fast, I added some limits:
- Start port must be at least **20**.
- End port must be at most **100**.
- Only **TCP** ports are checked.

> 💡 I intentionally set these limits to keep the scan quick and simple.

---

## 📸 Sample Output

When you run the program, you'll see something like this:

```text
(: time : 2026-06-19 14:12:45.123456
[+] ip or domain name target : google.com
[+] port start > 20 :20
[+] fnish port < 100 :25
[+] port 80 is open
```

---

## 🧠 What I learned from this?

- Working with the **socket** library in Python
- Getting user input
- Using `for` loops and conditions
- Simple error handling

---

## 📅 History

I wrote this code on **June 19, 2026** and put it on GitHub.

---

## 🙌 Got feedback?

I'd love to hear it!  
Just remember, this is a learning project, not a professional hacking tool!

---

## 📝 Code with Full Comments

```python
# Import socket library for network connections
import socket

# Import datetime library to get the current time
from datetime import datetime

# Display the start time of the scan
print(f" (: time : {datetime.now()}")

# Get the target IP or domain from the user
ip = input("[+] ip or domain name target :")

# Get the start port (must be greater than 20)
port_statr = int(input("[+] port start > 20 :"))

# Get the end port (must be less than 100)
port_fnish = int(input("[+] fnish port < 100 :"))

# Check if start port is less than 20
if port_statr < 20 :
    print("[!] no port start >= 20")
    exit()  # Stop the program
    
# Check if end port is greater than 100
elif port_fnish > 100:
    print("[!] no port fnish <= 100")
    exit()  # Stop the program
    
# Loop through all ports from start to end
for port_sc in range(port_statr, port_fnish):
    
    # Create a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Try to connect to the IP and port
    # If the result is 0, the connection was successful
    connect = s.connect_ex((ip, port_sc))
    
    # If the port is open, print a message
    if connect == 0 :
        print(f"[+] port {port_sc} is open")

# A note for myself to remember when I wrote this code
# date = 6/19/2026 2:12 PM
```

---

## 🛠 A few interesting points

- `connect_ex` doesn't throw an error; it returns a number instead:  
  - `0` means the port is **open**.  
  - Any other number means the port is **closed**.
- This code finishes quickly because it only checks 80 ports (from 20 to 100).

---

## 💡 Ideas to improve it

- Add a `timeout` to make it faster.
- Save the results to a file.
- Use multi-threading to scan more ports at once.
