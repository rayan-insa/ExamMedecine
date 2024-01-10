import re

def remove_newlines_before_lowercase(text):
    pattern = re.compile(r'\n(?=\D.{1}(?<!\.))')
    modified_text = re.sub(pattern, '', text)
    return modified_text

def save_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    file_path = "qcm_txt.txt"  # Replace with the actual path to your file

    with open(file_path, 'r', encoding='utf-8') as file:
        original_text = file.read()

    modified_text = remove_newlines_before_lowercase(original_text)

    save_path = "qcm_med_clean.txt"
    save_to_file(save_path, modified_text)

    print(f"Modified text saved to {save_path}")
