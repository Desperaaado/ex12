from os import path
from glob import glob
import argparse
import subprocess

paser = argparse.ArgumentParser(
    description='Realize sth like [find] command.'
)
paser.add_argument('-name', help='find by name')
paser.add_argument('-type', help='find by type')
paser.add_argument('-print', action='store_true', help='print the file')
paser.add_argument('path', help='define the search range')
paser.add_argument(
    '-exec',
    help=r'run cmd, end with \;'
)
args = paser.parse_args()

find_path = path.abspath(args.path)

def find_file(mode, keyword, find_path):
    if mode == 'name':
        find_key = keyword
    elif mode == 'type':
        find_key = '*.' + keyword
    else:
        print('ERROR: You can only find by name/type.')

    find_list = glob(path.join(find_path, find_key))
    if find_file:
        for stuff in find_list:
            print(stuff)
    else:
        print('Find Nothing!')
    return find_list

def print_file(file_list):
    print('=' * 10, 'PRINT', '=' * 10)
    
    for file in file_list:
        with open(file) as f:
            content = f.read()
            print('-' * 15, f'<{file}> CONTENT', '-' * 15)
            print(content)
    
    print('=' * 10, 'END PRINT', '=' * 10)

def exec_file(file_list, input_exec):
    print('=' * 10, 'EXECUTE', '=' * 10)

    if input_exec[-1] == r'\;':

        for file in file_list:
            exec_list = []
            input_exec_copy = input_exec[:]
            print('\n' + '-' * 10)

            while input_exec_copy[0] != r'\;':
                pop_thing = input_exec_copy.pop(0)
                if pop_thing == r'{}':
                    exec_list.append(file)
                else:
                    exec_list.append(pop_thing)

            subprocess.call(exec_list, shell=True)
    else:
        print('Wrong command format!')

    print('\n', '=' * 10, 'END EXECUTE', '=' * 10)

if args.name:
    file_list = find_file('name', args.name, find_path)
elif args.type:
    file_list = find_file('type', args.type, find_path)
else:
    print('ERROR: You can only find by name/type!')

if args.print:
    print_file(file_list)

if args.exec:
    exec_file(file_list, args.exec.split(' '))
