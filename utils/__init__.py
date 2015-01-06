# -*- coding: utf-8 -*-

import pdb
import sys
import getopt


def trace():
    pdb.set_trace()


def stop():
    sys.exit()


def req_input(inputs, init_command):
    if isinstance(inputs, str):
        inputs = [inputs]

    err_msg = init_command + ' ' + ' '.join('--' + i + ' [' + i + ']' for i in inputs)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "", [i + '=' for i in inputs])
    except getopt.error:
        print err_msg
        sys.exit(2)

    values = {}
    for o, a in opts:
        for i in inputs:
            if o == "--" + i:
                values[i] = a

    for i in inputs:
        if i not in values:
            print err_msg
            sys.exit(2)

    return values
