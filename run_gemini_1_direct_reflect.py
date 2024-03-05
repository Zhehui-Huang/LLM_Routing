import subprocess
import sys
import time


def main():
    while True:
        print('1_direct_reflect_gemini: \nStart!')
        return_ans = subprocess.run(['python', 'gemini_1_direct_reflect.py'], stderr=subprocess.PIPE, text=True)
        if return_ans.stderr == "":
            break
        else:
            print('1_direct_reflect_gemini: \nExecution failed, retrying in 10 seconds...')
            time.sleep(30)
            print('1_direct_reflect_gemini: \nError:', return_ans.stderr, sep='\n')
            continue


if __name__ == '__main__':
    sys.exit(main())
