#!/bin/bash

sudo apt update
sudo apt full-upgrade
sudo apt install python3-pip python3-pyqt5 python3-flask sqlite3
pip3 install flask pyqt5 prettytable
chmod +x phonebook.py gui.py web.py
echo -e "Successfully completed :)\nnow you can run the phonebook.py with options ( web version and gui version ) or withOut options (cli version)."
