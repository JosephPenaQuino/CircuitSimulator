node = []


class Component(object):
    global node

    def __init__(self, name, **kwargs):
        self.name = name
        self.kwarg = kwargs
        self.active = False
        for name, value in kwargs.items():
            try:
                node[value].append(self)
            except:
                node.append([])
                node[value].append(self)


class Source(Component):
    def __init__(self):
        Component.__init__(self)

        self.active = True

# class Resistor(Component):
#     def __init__(self):
#         Component.__init__(self)
#         try:
#             self.ohm = self.kwarg['Ohm']
#         except:
#             self.ohm = 0
#             print 'No Ohms?'

r1 = Component('r1', p0=0, p1=1)
r2 = Component('r2', p0=1, p1=2)
r3 = Component('r3', p0=1, p1=2)
r4 = Component('r4', p0=2, p1=3)
r5 = Component('r5', p0=3, p1=0)
k = Source('s0',p0=3,p1=0)