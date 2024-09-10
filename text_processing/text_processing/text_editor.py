class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_item = self.top.value
            self.top = self.top.next
            return popped_item

    def is_empty(self):
        return self.top is None


class TextEditor:
    def __init__(self):
        self.content = ""
        self.undo_stack = Stack()

    def add_text(self, text):
        self.content += text
        self.undo_stack.push(len(text))

    def undo(self):
        if not self.undo_stack.is_empty():
            length = self.undo_stack.pop()
            self.content = self.content[:-length]

    def display_content(self):
        print("Current content: ")
        print(self.content)


editor = TextEditor()
editor.add_text("Hello ")
editor.add_text("World!")
editor.display_content()

editor.undo()
editor.display_content()


