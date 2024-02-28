import subprocess
import sys
import time


def main():
    while True:
        print('1_gemini_direct_reflect_ambiguities.py: \nStart!')
        return_ans = subprocess.run(['python', '1_gemini_direct_reflect_ambiguities.py'], stderr=subprocess.PIPE, text=True)
        if return_ans.stderr == "":
            break
        else:
            print('1_gemini_direct_reflect_ambiguities.py: \nExecution failed, retrying in 10 seconds...')
            time.sleep(30)
            print('1_gemini_direct_reflect_ambiguities.py: \nError:', return_ans.stderr, sep='\n')
            continue


if __name__ == '__main__':
    sys.exit(main())
