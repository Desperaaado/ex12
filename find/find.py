import sys
from os import path
from glob import glob
import argparse
import subprocess

def parser_args():
    paser = argparse.ArgumentParser(
        description='Realize sth like [find] command.(make ex6 stronger)'
    )
    paser.add_argument('-name', help='find by name')
    paser.add_argument('-type', help='find by type')
    paser.add_argument('-print', action='store_true', help='print the file')
    paser.add_argument('path', nargs='?', help='define the search range')
    paser.add_argument('-exec', help=r'run cmd, end with \;')
    return paser.parse_args()

def find_file(mode, keyword, find_path):
    if mode == 'name':
        find_key = path.join(r'**', keyword)
    elif mode == 'type':
        find_key = r'**\*.' + keyword
    else:
        print('ERROR: You can only find by name/type.')
        sys.exit(1)

    find_list = glob(path.join(find_path, find_key), recursive=True)
    print('find_path: ', find_path)
    if find_list:
        print('\nWe Find These >>\n')
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

def main():
    # init
    args = parser_args()
    the_path = args.path
    if not the_path:
        the_path = '.'
    find_path = path.abspath(the_path)


    # find by name
    if args.name:
        file_list = find_file('name', args.name, find_path)
    # find by type
    elif args.type:
        file_list = find_file('type', args.type, find_path)
    # ls
    else:
        file_list = find_file('name', '*', find_path) 


    # do print (optional)
    if args.print:
        print_file(file_list)
    # do exec (optional)
    if args.exec:
        exec_file(file_list, args.exec.split(' '))


main()