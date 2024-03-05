import subprocess
import sys


def main():

    # middle_under_evaluate_list = [
    #     '1_direct_reflect_v3', '2_math_reflect_v3', '5_external_tools_direct_v3',
    #     '5_external_tools_math_v3', '1_direct_reflect_ambiguities_v3_ambiguities',
    #     'gemini_1_direct_reflect_v3', 'gemini_2_math_reflect_v3', 'gemini_5_external_tools_direct_v3',
    #     'gemini_5_external_tools_math_v3'
    # ]
    middle_under_evaluate_list = [
        'z_v2_fix_bug_1_direct_reflect_v3',
        'z_v2_fix_bug_2_math_reflect_v3',
        'z_v2_fix_bug_5_external_tools_direct_v3',
        'z_v2_fix_bug_5_external_tools_math_v3', 'z_v2_fix_bug_1_direct_reflect_ambiguities_v3_ambiguities',
        'Y_v2_gemini_1_direct_reflect_fix_bug_v3', 'Y_v2_gemini_2_math_reflect_fix_bug_v3',
        'Y_v2_gemini_5_external_tools_direct_fix_bug_v3',
        'Y_v2_gemini_5_external_tools_math_fix_bug_v3',
        'Y_v2_gemini_ambiguities_1_direct_reflect_fix_bug_v3_ambiguities'
    ]

    py_plots_script = ['final_results/make_plot_tsp_1.py', 'final_results/make_plot_tsp_1_optimal.py']

    for middle_under_evaluate in middle_under_evaluate_list:
        print('middle_under_evaluate:', middle_under_evaluate, sep='\n')
        for py_script in py_plots_script:
            subprocess.run(['python', py_script, '--root_dir', f'{middle_under_evaluate}'])


if __name__ == '__main__':
    sys.exit(main())
