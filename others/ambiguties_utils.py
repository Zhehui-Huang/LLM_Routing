import google.generativeai as genai

from gemini_utils import ask_gemini

GOOGLE_API_KEY = "AIzaSyBruy7vdcDDCHfIrNxgiYkBhAl7g2ajXGA"
genai.configure(api_key=GOOGLE_API_KEY)


def clear_check(client, gpt_model, gpt_prompt_tips, question):
    question_reply = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": f"You are a helpful assistant. {gpt_prompt_tips}"},
            {"role": "user", "content": question},
        ],
        stream=False,
    )
    answer_content = question_reply.choices[0].message.content
    return answer_content


def overall_clear_check(check_count, client, gpt_model, env_and_task, gpt_prompt_tips, gemini_prompt_tips, use_gemini):
    task_descriptions = f"\n{env_and_task}\n"
    real_check_id = -1
    for check_id in range(check_count):
        print(f"Check count: {check_id + 1}")

        question = (
            "### \nQuestion: is the following task description clear enough for you to solve it? "
            "Please ask if you think there are ambiguities. \n"
            "If your answer is yes, please only output: <*** YES!!! ***> \n"
            "If your answer is no, please provide clarification questions that you need me to answer. \n"
            "Language descriptions: \n"
            f"{task_descriptions}"
        )

        # # GPT 4
        gpt4_answer_content = clear_check(
            client=client, gpt_model=gpt_model, gpt_prompt_tips=gpt_prompt_tips, question=question)

        # # Gemini
        # gemini_model = genai.GenerativeModel('gemini-1.0-pro-latest')
        # gemini_chat = gemini_model.start_chat(history=[])
        # gemini_answer_reply = gemini_chat.send_message(f"{question} \n{gemini_prompt_tips}")
        # gemini_answer_content = gemini_answer_reply.text
        if use_gemini:
            gemini_answer_content = ask_gemini(question)
        else:
            gemini_answer_content = None

        print('GPT4 consistent check:    ', gpt4_answer_content, sep='\n')
        print('====================================================================================================')
        if use_gemini:
            print('Gemini consistent check:    ', gemini_answer_content, sep='\n')
            print('====================================================================================================')

        gpt_consistent_bool = "YES!!!" in gpt4_answer_content
        if use_gemini:
            gemini_consistent_bool = "YES!!!" in gemini_answer_content
            all_consistent_bool = gpt_consistent_bool and gemini_consistent_bool
        else:
            all_consistent_bool = gpt_consistent_bool

        if all_consistent_bool is False:
            print('Please clarify the task descriptions:\n')
            clarifications_from_user = input("")
            clarifications_from_user_prex = "\n### Following are clarifications from the user: \n"

            user_answer_modified = f"{clarifications_from_user_prex} {clarifications_from_user} ###"

            clarification_questions = ""
            if gpt_consistent_bool is False:
                clarification_questions += f"\n### Clarification questions: \n{gpt4_answer_content} \n###"
            # if gemini_consistent_bool is False:
            #     clarification_questions += f"\n### Clarification questions set B: \n{gemini_answer_content} \n###"

            task_descriptions += f"\n{clarification_questions} \n{user_answer_modified} \n"

            re_describe_task_reply = client.chat.completions.create(
                model=gpt_model,
                messages=[
                    {"role": "system", "content": f"You are a helpful assistant. {gpt_prompt_tips}"},
                    {"role": "user", "content": f'Please re-describe the task descriptions.\nTask descriptions: \n'
                                                f'{task_descriptions}'},
                ],
                stream=False,
            )
            task_descriptions = re_describe_task_reply.choices[0].message.content
            print('Modified Task descriptions: ', task_descriptions, sep='\n')
            real_check_id = check_id
            continue
        else:
            real_check_id = check_id
            break

    return task_descriptions, real_check_id
