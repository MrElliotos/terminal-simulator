ports = [22, 80, 443]
logs = ["System boot OK", "User admin logged in"]
def show_ports(item_list) :
    print("your list of ports")
    for item in item_list:
        print(f"-", {item})
def add_port(item_list) :
    try:
     xol = int(input("Provide the port number to add it"))
     if xol not in item_list:
                item_list.append(xol)
                print(f"Your port {xol} has been added")
     else :
            print(f"This port {xol} is already in the list")
    except ValueError :
        print("Please write numbers, not letters")
def show_logs(item_list) :
    print("your list of logs")
    for item in item_list :
        print(f"-, {item}")
def add_log(item_list, log_text) :
    log1 = f"[Log]: {log_text}"
    item_list.append(log1)
while True:
    print("=== SERVER TERMINAL v1.0 ===")
    dad = input("Enter a command (ports / open / logs / clear / exit): Open ").strip().lower()
    if dad == 'ports' :
        show_ports(ports)
    elif dad == 'open' :
        add_port(ports)
    elif dad == 'logs' :
        show_logs(logs)
    elif dad == 'clear':
        logs.clear()
        add_log(logs, "Logs cleared")
        print("Logs successfully cleared!")
    elif dad == 'exit' :
        print("OK, exiting")
        break
