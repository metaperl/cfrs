#!/usr/bin/python

import subprocess
import config

subprocess.call(
    [
        config.miner['exe'], 
        config.miner['args'].format(sendto=config.cfrs) 
        ], 
    cwd=config.miner['dir']
    )


