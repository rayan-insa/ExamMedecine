def read_qcm_file(file_path):
    questions = {}
    current_question = None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line[0].isdigit():
                # New question
                parts = line.split('. ', 1)
                if len(parts) > 1:
                    question_number, question_text = parts
                    current_question = question_text
                    questions[current_question] = {}
                current_question = question_text
                questions[current_question] = {}
            elif line:
                # Answer for the current question
                answer = line[2:]
                questions[current_question][answer] = "V"  # Set all answers to "V" for now

    return questions

if __name__ == "__main__":
    file_path = "qcm_med_clean.txt"  # Replace with the actual path to your file

    quiz_dict = read_qcm_file(file_path)

    print(quiz_dict)
    print(len(quiz_dict))
