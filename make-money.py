#!/usr/bin/python

import argparse
import subprocess

import config

def parse_command_line():
    parser = argparse.ArgumentParser(
        description='Run bitcoin miner',
        epilog='With no arguments start miner based on config.py'                             
        )

    parser.add_argument("--show",  action="store_true", help='Show command line')
    parser.add_argument("--batch", action="store_true", help='Create batch-file command line')
    args = parser.parse_args()
    return args

def create_cmd():
    cmdline_args =  config.miner['args'].format(
        sendto=config.cfrs, threads=config.miner['threads']).split()

    lis =  [ config.miner['exe'] ]
    lis.extend(cmdline_args)
    return lis

def batch_cmd_line(lis):
    lis[0] = 'start "idle miner" {0}\{1}'.format(config.miner['dir'], lis[0])
    print(" ".join(lis))

def echo_cmd_line(lis):
    print(" ".join(lis))

def make_money(lis):

    print "View stats at http://eligius.st/~artefact2/7/{0}".format(config.cfrs)

    subprocess.call(
        lis,
        cwd=config.miner['dir'],
        shell=True
        )


if __name__ == '__main__':

    args = parse_command_line()

    lis = create_cmd()
    if args.show:
        echo_cmd_line(lis)
    elif args.batch:
        batch_cmd_line(lis)
    else:
        make_money(lis)

