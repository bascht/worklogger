import PyZenity


class ZenityFrontend:
    @staticmethod
    def query(text, suggestion):
        return PyZenity.GetText(text=text, entry_text=suggestion)
