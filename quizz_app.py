import tkinter as tk
from create_dico import read_qcm_file
from tkinter import messagebox


class QuizApp:
    def __init__(self, master, quiz_dict):
        self.master = master
        self.quiz_dict = quiz_dict
        self.current_question = None

        self.question_label = tk.Label(master, text="")
        self.question_label.pack(pady=10)

        self.selected_answers = []

        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.load_question()

    def next_question(self):
        if self.current_question is not None:
            user_answers = [option for option, var in self.selected_answers if var.get() == 1]
            correct_answers = [option for option, correctness in self.quiz_dict[self.current_question].items() if correctness == "V"]

            if set(user_answers) == set(correct_answers):
                messagebox.showinfo("Result", "Your answer is correct!")
            else:
                messagebox.showinfo("Result", "Your answer is incorrect!")

            self.selected_answers = []
            # Remove the current question from the dictionary
            del self.quiz_dict[list(self.quiz_dict.keys())[0]]
            self.load_question()
        else:
            messagebox.showwarning("Warning", "Please select at least one answer.")

    def load_question(self):
        if not self.quiz_dict:
            messagebox.showinfo("Quiz Completed", "You have completed the quiz.")
            self.master.destroy()
            return

        question_key = list(self.quiz_dict.keys())[0]
        self.current_question = question_key

        self.question_label.config(text=question_key)

        # Clear previous options
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Checkbutton):
                widget.destroy()

        # Load new options
        self.selected_answers = []
        for option, correctness in self.quiz_dict[question_key].items():
            var = tk.IntVar()
            checkbox = tk.Checkbutton(self.master, text=option, variable=var)
            checkbox.pack()
            self.selected_answers.append((option, var))

        

def main():
    quiz_dict = read_qcm_file("qcm_med_clean.txt")

    root = tk.Tk()
    root.title("Quiz App")
    app = QuizApp(root, quiz_dict)
    root.mainloop()

if __name__ == "__main__":
    main()
