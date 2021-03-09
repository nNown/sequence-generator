from __future__ import annotations, generators
import os

import tkinter as tk
from tkinter import StringVar, filedialog

from sequence_generator import SequenceGenerator

class Application(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self) -> None:
        self.sequence_list()
        self.limit()
        self.menu()
    
    def sequence_list(self) -> None:
        self.sequencesFrame = tk.Frame(self.master, height=35, width=105)
        self.sequences = tk.Listbox(self.sequencesFrame, width=100, height=35)

        self.scrollbar = tk.Scrollbar(self.sequencesFrame, orient=tk.VERTICAL)
        self.scrollbar.configure(command=self.sequences.yview)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.sequences.pack()
        self.sequencesFrame.pack(side=tk.TOP, padx=30, pady=30)

    def limit(self) -> None:
        self.limit = StringVar()
        self.limit_box = tk.Entry(self.master, textvariable=self.limit, width=25)

        self.limit_box.pack(side=tk.TOP)

    def menu(self) -> None:
        self.menu = tk.Frame(self.master, width="100", height="6")
        self.add_sequence_button = tk.Button(self.menu, width="25", height="3", text="Add Sequence", command=self.add_sequence)
        self.save_sequence_button = tk.Button(self.menu, width="25", height="3", text="Save Sequences", command=self.save_sequences)

        self.add_sequence_button.pack(side=tk.LEFT, padx=30, pady=30)
        self.save_sequence_button.pack(side=tk.RIGHT, padx=30, pady=30)
        self.menu.pack(side=tk.BOTTOM)

    def add_sequence(self) -> None:
        fh = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open protein sequence", filetypes=[("Text Files", "*.txt")])
        fh = open(fh, "r")
        content = fh.read()

        self.sequences.delete(0, tk.END)
        self.generate_sequences(content)
        fh.close()

    def save_sequences(self) -> None:
        fh = filedialog.askopenfilename(initialdir=os.getcwd(), title="Choose file to save sequence to", filetypes=[("Text Files", "*.txt")])
        fh = open(fh, "w")
        for idx in range(self.sequences.size()):
            fh.write(f"{self.sequences.get(idx)}\n")
        fh.close()

    def generate_sequences(self, protein_sequence: str) -> None:
        sequencesLimit = self.validate_limit()
        data = list()

        try:
            self.generator = SequenceGenerator(protein_sequence)
            for i, sequence in enumerate(self.generator, start=1):
                if i > sequencesLimit:
                    break
                data.append("".join(sequence))
        except:
            data.append("Invalid sequence")
        
        self.sequences.insert(tk.END, *data)

    def validate_limit(self) -> int:
        inputData = self.limit.get()

        if inputData.isdigit():
            return int(inputData)
        return 0