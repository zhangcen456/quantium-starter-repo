#!/bin/bash
chromedriver=%1
venv\Scripts\activate.bat
export PATH=$PATH:$chromedriver
pytest test_app.py

if [ $? -eq 0 ]; then
  exit 0
else
  exit 1
fi