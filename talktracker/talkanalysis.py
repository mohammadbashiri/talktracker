import talktracker as tt


class TalkAnalysis(object):
    def __init__(self, members, names):
        self._members = {name: member for name, member in zip(names, members)}

    def __getitem__(self, item):
        return self._members[item]

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return self._members[item]

    @property
    def members(self):
        return self._members

    def get_DataFrame(self):
        raise NotimplementedError
