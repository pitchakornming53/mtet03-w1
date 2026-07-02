import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("360x580")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a0000")

        self.expression = ""
        self.display_var = tk.StringVar(value="0")
        self.sub_var = tk.StringVar(value="")

        self._build_ui()

    def _build_ui(self):
        sub = tk.Label(
            self.root, textvariable=self.sub_var,
            font=("Segoe UI", 13), bg="#1a0000", fg="#cc3333",
            anchor="e", padx=18
        )
        sub.pack(fill="x", pady=(24, 0))

        display = tk.Label(
            self.root, textvariable=self.display_var,
            font=("Segoe UI", 42, "bold"), bg="#1a0000", fg="#ff4444",
            anchor="e", padx=18
        )
        display.pack(fill="x")

        tk.Frame(self.root, bg="#5c0000", height=2).pack(fill="x", pady=8)

        buttons = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["00", "0", ".", "="],
        ]

        frame = tk.Frame(self.root, bg="#1a0000")
        frame.pack(fill="both", expand=True, padx=12, pady=8)

        for r, row in enumerate(buttons):
            frame.grid_rowconfigure(r, weight=1)
            for c, label in enumerate(row):
                frame.grid_columnconfigure(c, weight=1)
                btn = self._make_button(frame, label)
                btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

    def _make_button(self, parent, label):
        if label == "=":
            bg, fg, abg = "#cc0000", "#ffffff", "#ff2222"
        elif label in ("÷", "×", "−", "+"):
            bg, fg, abg = "#8b0000", "#ff9999", "#aa0000"
        elif label in ("C", "±", "%"):
            bg, fg, abg = "#3d0000", "#ff6666", "#550000"
        else:
            bg, fg, abg = "#2b0000", "#ff8888", "#3d0000"

        btn = tk.Button(
            parent, text=label,
            font=("Segoe UI", 20, "bold"),
            bg=bg, fg=fg, activebackground=abg, activeforeground="#ffffff",
            relief="flat", cursor="hand2", bd=0,
            command=lambda l=label: self._on_click(l)
        )
        btn.bind("<Enter>", lambda e, b=btn, c=abg: b.configure(bg=c))
        btn.bind("<Leave>", lambda e, b=btn, c=bg: b.configure(bg=c))
        return btn

    def _on_click(self, label):
        if label == "C":
            self.expression = ""
            self.display_var.set("0")
            self.sub_var.set("")

        elif label == "±":
            try:
                val = -float(self._safe_eval(self.expression))
                self.expression = self._fmt(val)
                self.display_var.set(self.expression)
            except Exception:
                pass

        elif label == "%":
            try:
                val = float(self._safe_eval(self.expression)) / 100
                self.expression = self._fmt(val)
                self.display_var.set(self.expression)
            except Exception:
                self.display_var.set("Error")

        elif label == "=":
            try:
                self.sub_var.set(self._display_expr(self.expression) + " =")
                result = self._safe_eval(self.expression)
                self.display_var.set(self._fmt(result))
                self.expression = self._fmt(result)
            except Exception:
                self.display_var.set("Error")
                self.expression = ""

        else:
            sym_map = {"÷": "/", "×": "*", "−": "-"}
            char = sym_map.get(label, label)

            if label in ("÷", "×", "−", "+"):
                if self.expression and self.expression[-1] in "/*-+":
                    self.expression = self.expression[:-1]
                if not self.expression:
                    self.expression = "0"
            elif label == ".":
                last_num = self.expression.replace("(", "").split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]
                if "." in last_num:
                    return
            elif label == "00":
                if not self.expression or self.expression == "0":
                    return

            self.expression += char
            self.display_var.set(self._display_expr(self.expression))

    def _safe_eval(self, expr):
        allowed = set("0123456789.+-*/() ")
        if not all(c in allowed for c in expr):
            raise ValueError("Invalid expression")
        return eval(expr)

    def _fmt(self, val):
        if isinstance(val, float) and val.is_integer():
            return str(int(val))
        return str(round(val, 10)).rstrip("0").rstrip(".")

    def _display_expr(self, expr):
        result = expr.replace("*", "×").replace("/", "÷").replace("-", "−")
        return result[-16:] if len(result) > 16 else result


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
