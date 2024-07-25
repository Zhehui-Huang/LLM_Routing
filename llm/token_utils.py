import tiktoken


def input_num_tokens(messages, model):
    """Return the number of tokens used by a list of messages."""
    encoding = tiktoken.encoding_for_model(model)

    tokens_per_message = 3
    tokens_per_name = 1

    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3
    return num_tokens


def calculate_output_token(content, model):
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(content))
    return num_tokens


def calculate_token_num(messages, response_content, model, token_file_path, notes):
    input_token_num = input_num_tokens(messages=messages, model=model)
    output_token_num = calculate_output_token(content=response_content, model=model)
    total_token_num = input_token_num + output_token_num

    with open(token_file_path, 'a') as file:
        file.write(f"@@@@@\n")
        file.write(f"Notes: {notes}\n")
        file.write(f"input_token_num: {input_token_num}\n")
        file.write(f"output_token_num: {output_token_num}\n")
        file.write(f"total_token_num: {total_token_num}\n")
        file.write("@@@@@\n\n")

    print('@@@@@')
    print(f"Notes: {notes}")
    print(f"input_token_num: {input_token_num}")
    print(f"output_token_num: {output_token_num}")
    print(f"total_token_num: {total_token_num}")
    print('@@@@@\n\n')

    return input_token_num, output_token_num, total_token_num
