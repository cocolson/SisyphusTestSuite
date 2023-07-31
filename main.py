
import sys
import tkinter as tk
import algorithms
import test_cases
import text_redirect
import unittest

def color_text(text_widget, target, color):
    start_idx = "1.0"
    while True:
        start_idx = text_widget.search(target, start_idx, stopindex=tk.END)
        if not start_idx:
            break
        end_idx = f"{start_idx}+{len(target)}c"
        text_widget.tag_add(color, start_idx, end_idx)
        start_idx = end_idx

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sisyphus Test Suite")
    root.geometry("800x600")

    def run_tests():
        output_text.config(state=tk.NORMAL)
        sys.stdout = text_redirect.TextRedirect(output_text)

        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover(start_dir=".", pattern="test_*.py")
        test_runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=0)
        test_result = test_runner.run(test_suite)
        
        sys.stdout = sys.__stdout__

        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, str(test_result))
        
        color_text(output_text, "PASSED", "passed")
        color_text(output_text, "FAILED", "failed")

        output_text.config(state=tk.DISABLED)

    run_button = tk.Button(root, text="Run Tests", command=run_tests)
    run_button.pack(pady=10)

    output_text = tk.Text(root, wrap=tk.WORD, height=20, width=80)
    output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    output_text.tag_configure("passed", foreground="green")
    output_text.tag_configure("failed", foreground="red")

    scrollbar = tk.Scrollbar(root, command=output_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    output_text.config(yscrollcommand=scrollbar.set)

    root.mainloop()