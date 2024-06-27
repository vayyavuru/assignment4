class Todo_List:
    def __init__(self, owner: str, todo_list: list = []):
        for item in todo_list:
            if not isinstance(item, Todo_Item):
                raise Exception(f"Expected Todo Item, got {type(item)}")
        self.owner = owner
        self.todo_items = todo_list

    def __str__(self):
        pending_high = sum(1 for item in self.todo_items if item.priority == "High" and not item.completed)
        pending_medium = sum(1 for item in self.todo_items if item.priority == "Medium" and not item.completed)
        pending_low = sum(1 for item in self.todo_items if item.priority == "Low" and not item.completed)
        finished = sum(1 for item in self.todo_items if item.completed)

        return f"""Pending Tasks:
High - {pending_high}, Medium - {pending_medium}, Low - {pending_low}
Finished Tasks: {finished}"""

class Todo_Item:
    def __init__(self, description: str, priority: str, completed: bool = False):
        self.description = description
        self.priority = priority
        self.completed = completed

# Example usage
todo_list = Todo_List("nandu", [
    Todo_Item("Task 1", "High"),
    Todo_Item("Task 2", "High"),
    Todo_Item("Task 3", "High"),
    Todo_Item("Task 4", "Medium"),
    Todo_Item("Task 5", "Medium"),
    Todo_Item("Task 6", "Low"),
    Todo_Item("Task 7", "Low"),
    Todo_Item("Task 8", "Low"),
    Todo_Item("Task 9", "Low"),
    Todo_Item("Task 10", "Low"),
    Todo_Item("Task 11", "Low", completed=True),
    Todo_Item("Task 12", "Low", completed=True),
    Todo_Item("Task 13", "Low", completed=True),
    Todo_Item("Task 14", "Low", completed=True),
    Todo_Item("Task 15", "Low", completed=True),
    Todo_Item("Task 16", "Low", completed=True),
])

print(todo_list)





