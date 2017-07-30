node = []


class Component(object):
    global node

    def __init__(self, name, **kwargs):
        self.name = name
        self.kwarg = kwargs
        self.active = False  # Set if a component is active or not
        for name, value in kwargs.items():
            if name == 'p0' or name == 'p1' or name == 'p2':
                try:
                    node[value].append(self)
                except IndexError:
                    node.append([])
                    node[value].append(self)


class Source(Component):
    def __init__(self, name, **kwargs):
        Component.__init__(self, name, **kwargs)
        self.active = True
        try:
            self.voltage = kwargs['voltage']
        except:
            try:
                self.current = kwargs['current']
            except:
                self.voltage = 12


class Resistor(Component):
    def __init__(self, name, **kwargs):
        Component.__init__(self, name, **kwargs)
        try:
            self.resistance = kwargs['resistance']
        except:
            self.resistance = 2200


r1 = Resistor('r1', p0=0, p1=1, resistance=1000)
r2 = Resistor('r2', p0=1, p1=2, resistance=1200)
r3 = Resistor('r3', p0=1, p1=2, resistance=4000)
r4 = Resistor('r4', p0=2, p1=3, resistance=5010)
r5 = Resistor('r5', p0=3, p1=0)
k = Source('s0', p0=3, p1=0)

for i in node:
    for k in i:
        print k.name
    print '------'
