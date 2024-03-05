import subprocess
import sys
import time


def main():
    while True:
        print('5_external_tools_direct_gemini: \nStart!')
        return_ans = subprocess.run(['python', 'gemini_5_external_tools_direct.py'], stderr=subprocess.PIPE, text=True)
        if return_ans.stderr == "":
            break
        else:
            print('5_external_tools_direct_gemini: \nExecution failed, retrying in 30 seconds...')
            time.sleep(30)
            print('5_external_tools_direct_gemini: \nError:', return_ans.stderr, sep='\n')
            continue


if __name__ == '__main__':
    sys.exit(main())
