# this is part of the IPv6Monitor project.
#
# Release: v1.0-dev3
#
# Copyright (c) 2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#  
# repo: https://github.com/juanBindez


import subprocess
import time
import notify2


notify2.init("IPvMonitor")

TITLE = "IPvMonitor"
MESSAGE_INIT = "O IPvMonitor v1.0-dev3 Foi Iniciado!"
MESSAGE_NOTE = "Esta é uma versão Dev, testa apenas o IPv6 por enquanto!"
MESSAGE_LOST_IP6 = "Conexão IPv6 Perdida!"
MESSAGE_RECONNECTION = "Conexão reestabelecida!"


notify2.Notification(TITLE, MESSAGE_INIT).show()
time.sleep(2)
notify2.Notification(TITLE, MESSAGE_NOTE).show()

# IPv6 do Google
ipv6_address = "2800:3f0:4004:810::200e"

def test_dois():
    while True:
        result = subprocess.run(["ping6", "-c", "4", ipv6_address], stdout=subprocess.DEVNULL)
        if result.returncode != 0:
            notify2.Notification(TITLE, MESSAGE_LOST_IP6).show()
            pass
        elif result.returncode == 0:
            notify2.Notification(TITLE, MESSAGE_RECONNECTION).show()
            break
            pass
            test_dois()

        time.sleep(10)
        

def test_init():
    while True:
        result = subprocess.run(["ping6", "-c", "4", ipv6_address], stdout=subprocess.DEVNULL)
        if result.returncode != 0:
            notify2.Notification(TITLE, MESSAGE_LOST_IP6).show()
            test_dois()
    
        time.sleep(10)

if __name__ == "__main__":
    test_init()
