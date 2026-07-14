class History:

    def __init__(self):

        self.undo_stack = []

        self.redo_stack = []


    def add(self, image):

        self.undo_stack.append(
            image.copy()
        )

        self.redo_stack.clear()


    def undo(self):

        if len(self.undo_stack) > 1:

            image = self.undo_stack.pop()

            self.redo_stack.append(
                image
            )

            return self.undo_stack[-1]

        return None


    def redo(self):

        if self.redo_stack:

            image = self.redo_stack.pop()

            self.undo_stack.append(
                image
            )

            return image

        return None