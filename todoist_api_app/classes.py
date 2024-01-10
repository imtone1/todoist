

class Task:
    def __init__(self, content=None, description=None, order=1, priority=1, project_id=None, labels=[], due_date=None, section_id=None, parent_id=None, due_lang="fi", child_tasks=None):
        self.content = content
        self.description = description
        self.order = order
        self.priority = priority
        self.project_id = project_id
        self.labels = labels
        self.due_date = due_date
        self.section_id = section_id
        self.parent_id = parent_id
        self.due_lang=due_lang
        self.child_tasks=child_tasks


class Issue:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date