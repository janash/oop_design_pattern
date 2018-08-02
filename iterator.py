"""
    Iterator class in Python. 
"""

class Iterator(object):

    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        # any pre init
        self.current = self.start

        # you have to return iter object
        return self

    def __next__(self):
        """ return the next data in order """
        # stopping
        if self.current >= self.end:
            raise StopIteration

        tmp = self.current
        self.current += self.step
        return tmp

class Molecule():

    def __init__(self, atoms: list):
        self.atoms = atoms

        # ...lots of other stuff...

    def __iter__(self):
        return iter(self.atoms)
#---------------------------------------------------------

iterator = Iterator(1, 10, 1)

for i in iterator:
    print(i)

molecule = Molecule(['C', 'C', 'H', 'O'])

for atom in molecule:
    print(atom)

