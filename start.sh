#!/usr/bin/env bash
$(which python) manage.py runserver 192.168.1.1:8000
chromium-browser --kiosk http://192.168.1.1:8000/ILSA
