import sys
import subprocess
import time
import pytz
from datetime import datetime

LA_TIMEZONE = pytz.timezone('America/Los_Angeles')

exec_list = [
    'TSP.py', 'BTSP.py', 'GTSP.py', 'KTSP.py',
    'mTSP-sum.py', 'mTSP-minmax.py', 'mTSP-MD_fixed.py', 'mTSP-MD_not_fixed.py', 'CVRP.py'
]

# Not run
# 'mTSP-sum-limit.py'
# 'mTSP-MD_not_fixed.py'
# 'mTSP-minmax.py'


def get_start_time():
    start_time = time.time()
    cur_time = datetime.now(LA_TIMEZONE)
    print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\t...")
    return start_time

def get_end_time(start_time):
    end_time = time.time()
    response_time = end_time - start_time
    cur_time = datetime.now(LA_TIMEZONE)
    print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\tFinished.\tResponse time: {response_time:.2f} seconds.")
    return response_time

def run_code():
    # Iterate through each script and run it
    for script in exec_list:
        start_time = time.time()
        cur_time = datetime.now(LA_TIMEZONE)
        print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\t {script}...")

        try:
            result = subprocess.run(['python', script], capture_output=True, text=True)
            print(f"Output of {script}:\n{result.stdout}")
            if result.stderr:
                print(f"Error in {script}:\n{result.stderr}")
        except Exception as e:
            print(f"Failed to run {script}: {e}")

        get_end_time(start_time=start_time)
        # end_time = time.time()
        # response_time = end_time - start_time
        # cur_time = datetime.now(LA_TIMEZONE)
        # print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\tFinished.\tResponse time: {response_time:.2f} seconds.")


def run_code2():
    for script in exec_list:
        start_time = time.time()
        cur_time = datetime.now(LA_TIMEZONE)
        print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\t {script}...")
        try:
            process = subprocess.Popen(['python', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Print the output and errors in real-time
            while True:
                output = process.stdout.readline()
                if output == b'' and process.poll() is not None:
                    break
                if output:
                    print(output.decode().strip())

            stderr = process.stderr.read().decode()
            if stderr:
                print(f"Error in {script}:\n{stderr}", file=sys.stderr)

        except Exception as e:
            print(f"Failed to run {script}: {e}", file=sys.stderr)


        end_time = time.time()
        response_time = end_time - start_time
        cur_time = datetime.now(LA_TIMEZONE)
        print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\tFinished.\tResponse time: {response_time:.2f} seconds.")


def main():
    run_code2()


if __name__ == '__main__':
    sys.exit(main())
