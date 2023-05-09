# this is part of the IPv6Monitor project.
#
# Release: v1.0-dev2
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

notify2.init("IPv6Monitor")
title = "IPv6 Parou"


title1 = "IPV6Monitor"
message1 = "O IPV6 Monitor v1.0-dev1 Foi Iniciado!"

title2 = "IPV6Monitor"
message2 = "Conexão IPv6 Perdida!"

title3 = "IPV6Monitor"
message3 = "Conexão reestabelecida!"

notify2.Notification(title1, message1).show()

ipv6_address = "2800:3f0:4004:810::200e"


def test_dois():
    while True:
        result = subprocess.run(["ping6", "-c", "1", ipv6_address], stdout=subprocess.DEVNULL)
        if result.returncode != 0:
            notify2.Notification(title2, message2).show()
            pass
        elif result.returncode == 0:
            notify2.Notification(title3, message3).show()
            break
            pass
            test_dois()

        time.sleep(10)
        

def test_init():
    while True:
        result = subprocess.run(["ping6", "-c", "1", ipv6_address], stdout=subprocess.DEVNULL)
        if result.returncode != 0:
            notify2.Notification(title2, message2).show()
            test_dois()
    
            
        time.sleep(10)

if __name__ == "__main__":
    test_init()
