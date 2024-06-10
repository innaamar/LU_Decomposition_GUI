import numpy as np
import customtkinter as ctk
from tkinter import messagebox


class LUDecompositionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LU Decomposition Solver")

        self.matrix_label = ctk.CTkLabel(
            root, text="Enter matrix A (comma-separated rows):"
        )
        self.matrix_label.pack(pady=10)
        self.matrix_entry = ctk.CTkEntry(root, width=400)
        self.matrix_entry.pack(pady=10)

        self.vector_label = ctk.CTkLabel(root, text="Enter vector b (comma-separated):")
        self.vector_label.pack(pady=10)
        self.vector_entry = ctk.CTkEntry(root, width=400)
        self.vector_entry.pack(pady=10)

        self.method_label = ctk.CTkLabel(root, text="Choose LU decomposition method:")
        self.method_label.pack(pady=10)
        self.method_var = ctk.StringVar(value="Doolittle")
        self.doolittle_radio = ctk.CTkRadioButton(
            root, text="Doolittle", variable=self.method_var, value="Doolittle"
        )
        self.doolittle_radio.pack(pady=5)
        self.crout_radio = ctk.CTkRadioButton(
            root, text="Crout", variable=self.method_var, value="Crout"
        )
        self.crout_radio.pack(pady=5)

        self.solve_button = ctk.CTkButton(root, text="Solve", command=self.solve)
        self.solve_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(root, text="Solution x:")
        self.result_label.pack(pady=10)
        self.result_text = ctk.CTkTextbox(root, height=200, width=400)
        self.result_text.pack(pady=10)

    def parse_matrix(self, matrix_str):
        try:
            matrix = [list(map(float, row.split(","))) for row in matrix_str.split(";")]
            return np.array(matrix)
        except ValueError:
            messagebox.showerror("Input Error", "Invalid matrix format")
            return None

    def parse_vector(self, vector_str):
        try:
            vector = list(map(float, vector_str.split(",")))
            return np.array(vector)
        except ValueError:
            messagebox.showerror("Input Error", "Invalid vector format")
            return None

    def solve(self):
        A_str = self.matrix_entry.get()
        b_str = self.vector_entry.get()
        method = self.method_var.get()

        A = self.parse_matrix(A_str)
        b = self.parse_vector(b_str)

        if A is None or b is None:
            return

        if method == "Doolittle":
            L, U, steps = self.doolittle_lu(A)
        elif method == "Crout":
            L, U, steps = self.crout_lu(A)

        if L is None or U is None:
            return

        try:
            y = np.linalg.solve(L, b)
            x = np.linalg.solve(U, y)
        except np.linalg.LinAlgError:
            messagebox.showerror(
                "Error", "Failed to solve linear equations. Please check your inputs."
            )
            return

        self.result_text.delete(1.0, ctk.END)
        self.result_text.insert(ctk.END, "Intermediate Steps:\n")
        self.result_text.insert(ctk.END, steps)
        self.result_text.insert(ctk.END, "\nSolution x:\n")
        self.result_text.insert(ctk.END, str(x))

    def doolittle_lu(self, A):
        n = A.shape[0]
        L = np.zeros((n, n))
        U = np.zeros((n, n))
        steps = ""

        try:
            for i in range(n):
                for k in range(i, n):
                    sum_ = sum(L[i][j] * U[j][k] for j in range(i))
                    U[i][k] = A[i][k] - sum_
                    steps += f"U[{i}][{k}] = {U[i][k]}\n"

                for k in range(i, n):
                    if i == k:
                        L[i][i] = 1
                    else:
                        sum_ = sum(L[k][j] * U[j][i] for j in range(i))
                        L[k][i] = (A[k][i] - sum_) / U[i][i]
                    steps += f"L[{k}][{i}] = {L[k][i]}\n"
        except ZeroDivisionError:
            messagebox.showerror("Error", "Singular matrix")
            return None, None, None

        return L, U, steps

    def crout_lu(self, A):
        n = A.shape[0]
        L = np.zeros((n, n))
        U = np.identity(n)
        steps = ""

        try:
            for j in range(n):
                for i in range(j, n):
                    sum_ = sum(L[i][k] * U[k][j] for k in range(j))
                    L[i][j] = A[i][j] - sum_
                    steps += f"L[{i}][{j}] = {L[i][j]}\n"

                for i in range(j + 1, n):
                    sum_ = sum(L[j][k] * U[k][i] for k in range(j))
                    U[j][i] = (A[j][i] - sum_) / L[j][j]
                    steps += f"U[{j}][{i}] = {U[j][i]}\n"
        except ZeroDivisionError:
            messagebox.showerror("Error", "Singular matrix")
            return None, None, None

        return L, U, steps


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = LUDecompositionApp(root)
    root.mainloop()
