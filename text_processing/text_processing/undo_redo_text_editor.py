class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def type(self, word):
        self.undo_stack.append(self.text)
        self.text += word
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()

    def show(self):
        print(self.text)

# Test
editor = TextEditor()
editor.type("Hello ")
editor.type("world!")
editor.show()  # Output: Hello world!
editor.undo()
editor.show()  # Output: Hello 
editor.redo()
editor.show()  # Output: Hello world!
