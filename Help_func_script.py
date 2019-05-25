#!/usr/bin/env python3
# coding: utf-8

import os
import sys

if len(sys.argv) != 2:
    print("None Parameter. Need transport param at terminal.")
else:
    file_name = "help_%s.txt" % sys.argv[1]

    sys_out = sys.stdout
    out_file = open(file_name, "w")
    sys.stdout = out_file
    try:
        print(help(sys.argv[1]))
    except Exception as e:
        sys.stdout = sys_out
        out_file.close()
        print(e)
    finally:
        sys.stdout = sys_out
        out_file.close()

    os.system("%s; quit" %file_name)
    print("Done...")
    sys.exit()
