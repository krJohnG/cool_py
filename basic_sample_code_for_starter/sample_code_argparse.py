#-*- coding:utf-8 -*-
import argparse

parser = argparse.ArgumentParser(description='[...]')
parser.add_argument('arg_1', help='[arg_1 is ...]')
parser.add_argument('arg_2', help='[arg_2 is ...]')
parser.add_argument('arg_3', help='[arg_3 is ...]')
parser.add_argument('-i', help='[ ... ]',nargs='?', const=1, type=int)
args = parser.parse_args()

# check option '-i'
if args.i:
    GLOBAL_OPTION_I = True
else:
    GLOBAL_OPTION_I = False

# use common print
print('- View sample common')
print('[*] arg_1 : ' + str(args.arg_1))
print('[*] arg_2 : ' + str(args.arg_2))
print('[*] arg_3 : ' + str(args.arg_3))
print(' ')

# use print with option '-i'
print('- View sample with option')
if GLOBAL_OPTION_I:
    print('[*] arg_1 : ' + str(args.arg_1))
    print('[*] arg_2 : ' + str(args.arg_2))
    print('[*] arg_3 : ' + str(args.arg_3))
else:
    print('[*] arg_1 : ' + str(args.arg_1))
    print('[*] arg_2 : ****** (view with option -i)')
    print('[*] arg_3 : ****** (view with option -i)')
