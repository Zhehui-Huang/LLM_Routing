import subprocess
import sys


def main():

    middle_under_evaluate_list = [
        '1_direct_reflect_v3', '2_math_reflect_v3', '5_external_tools_direct_v3',
        '5_external_tools_math_v3', '1_direct_reflect_ambiguities_v3_ambiguities']

    py_plots_script = ['final_results/make_plot_tsp_1.py', 'final_results/make_plot_tsp_1_optimal.py']

    for middle_under_evaluate in middle_under_evaluate_list:
        print('middle_under_evaluate:', middle_under_evaluate, sep='\n')
        for py_script in py_plots_script:
            subprocess.run(['python', py_script, '--root_dir', f'{middle_under_evaluate}'])


if __name__ == '__main__':
    sys.exit(main())
