import google.generativeai as genai

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


def overall_clear_check(check_count, client, gpt_model, env_and_task, gpt_prompt_tips, gemini_prompt_tips):
    gemini_model = genai.GenerativeModel('gemini-pro')
    question = (
        "### \nQuestion: are following language descriptions clear enough for you to solve the it? \n"
        "If your answer is yes, please only output: <*** YES!!! ***> \n"
        "If your answer is no, please provide clarification questions that you need me to answer. \n"
        "Language descriptions: \n"
        f"{env_and_task} \n###"
    )
    task_descriptions = f"\n{env_and_task} \n"
    for check_id in range(check_count):
        print(f"Check count: {check_id + 1}")
        # # GPT 4
        gpt4_answer_content = clear_check(
            client=client, gpt_model=gpt_model, gpt_prompt_tips=gpt_prompt_tips, question=question)

        # # Gemini
        gemini_chat = gemini_model.start_chat(history=[])
        gemini_answer_reply = gemini_chat.send_message(f"{question} \n{gemini_prompt_tips}")
        gemini_answer_content = gemini_answer_reply.text

        print('GPT4 consistent check:    ', gpt4_answer_content, sep='\n')
        print('====================================================================================================')
        print('Gemini consistent check:    ', gemini_answer_content, sep='\n')
        print('====================================================================================================')

        gpt_consistent_bool = "YES!!!" in gpt4_answer_content
        gemini_consistent_bool = "YES!!!" in gemini_answer_content
        all_consistent_bool = gpt_consistent_bool and gemini_consistent_bool

        if all_consistent_bool is False:
            print('Please clarify the task descriptions:\n')
            clarifications_from_user = input("")
            clarifications_from_user_prex = "\n### Following are clarifications from the user: \n"

            user_answer_modified = f"{clarifications_from_user_prex} {clarifications_from_user} ###"

            clarification_questions = ""
            if gpt_consistent_bool is False:
                clarification_questions += f"\n### Clarification questions set A: \n{gpt4_answer_content} \n###"
            if gemini_consistent_bool is False:
                clarification_questions += f"\n### Clarification questions set B: \n{gemini_answer_content} \n###"

            task_descriptions += f"\n{clarification_questions} \n{user_answer_modified} \n"
            print('Modified Task descriptions: ', task_descriptions, sep='\n')
            continue
        else:
            break

    return task_descriptions
