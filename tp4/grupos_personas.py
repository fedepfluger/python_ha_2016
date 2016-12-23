class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __repr__(self):
        return "<Person '{}'>".format(self.name)

    def __add__(self, p):
        assert isinstance(p, Person)
        return Group((self, p))

    def __eq__(self):
        return (
            isinstance(p, Person) and
            self.name == p.name and
            self.age == p.age)

    def __ne__(self, p):
        return not self == p

    def __hash__(self):
        return hash(self.name) + hash(self.age)

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age



class Group(object):

    def __init__(self, people):
        assert all([isinstance(p, Person) for p in people])
        self.people = frozenset(people)

    def __repr__(self):
        return "<Group with {} people>".format(len(self))

    def __eq__(self, g):
        return isinstance(g, Group) and self.people == g.people

    def __ne__(self, g):
        return not self == g

    def __add__(self, obj):
        assert isinstance(obj, (Person, Group))
        if isinstance(obj, Person):
            obj = [obj]
        return Group(list(self) + list(obj))

    def __sub__(self, obj):
        assert isinstance(obj, (Person, Group))
        if isinstance(obj, Person):
            obj = [obj]
        return Group([p for p in self if p not in obj])

    def __contains__(self, obj):
        assert isinstance(obj, Person)
        return obj in self.people

    def __iter__(self):
        return iter(self.people)

    def __len__(self):
        return len(self.people)
