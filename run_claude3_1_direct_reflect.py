import subprocess
import sys
import time


def main():
    while True:
        print('claude3_1_direct_reflect: \nStart!')
        return_ans = subprocess.run(['python', 'claude3_1_direct_reflect.py'], stderr=subprocess.PIPE, text=True)
        if return_ans.stderr == "":
            break
        else:
            print('claude3_1_direct_reflect: \nExecution failed, retrying in 10 seconds...')
            time.sleep(10)
            print('claude3_1_direct_reflect: \nError:', return_ans.stderr, sep='\n')
            continue


if __name__ == '__main__':
    sys.exit(main())
