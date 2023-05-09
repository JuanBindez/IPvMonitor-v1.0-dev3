import subprocess
import time
import notify2

title1 = "Iniciado"
message1 = "O IPV6 Monitor v1.0-dev1 Foi Iniciado!"

notify2.init("IPv6 Monitor")
title = "IPv6 Parou"
message = "A conexão IPv6 foi perdida!"

notify2.Notification(title1, message1).show()

ipv6_address = "2800:3f0:4004:810::200e"


while True:
    result = subprocess.run(["ping6", "-c", "1", ipv6_address], stdout=subprocess.DEVNULL)
    if result.returncode != 0:
        notify2.Notification(title, message).show()
        
    time.sleep(30)
