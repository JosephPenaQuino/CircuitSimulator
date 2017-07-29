codeCounter = 0
componentCounter = 0


class Component(object):
    def __init__(self):
        self.nodesLinked = []
        self.value = 0
        self.type = 'none'

    def set_nodes(self, nodes):
        self.nodesLinked = nodes


class Nodes(object):
    def __init__(self):
        self.code = "xxxx"
        self.name = "-"
        self.componentsInto = []

    def set_code(self, code_n):
        self.code = code_n

    def set_name(self, name_n):
        self.name = name_n

    def set_components(self, component):
        global componentCounter
        self.componentsInto.append(component)
        componentCounter = componentCounter + 1


class Resistors(Component):
    def set_ohms(self, numbers_ohms=2200):
        self.value = numbers_ohms
        self.type = 'Res'


class VoltageSource(Component):
    def set_voltage(self, number_voltage=22):
        self.value = number_voltage
        self.type = 'VSource'


# Creating the nodes
node1 = Nodes()
node2 = Nodes()

# Indexing the nodes
l_node = {
    '1': node1,
    '2': node2

}

# Creating components
r1 = Resistors()
r1.set_ohms(1000)

# Creating Sources
v1 = VoltageSource()
v1.set_voltage(6)

l_node['1'].set_components(r1)
l_node['2'].set_components(r1)
l_node['1'].set_components(v1)
l_node['2'].set_components(v1)

print l_node['1'].componentsInto[0].value
print l_node['1'].componentsInto[1].value
print l_node['2'].componentsInto[0].value
print l_node['2'].componentsInto[1].value

tOhm = 0
tVoltage = 0

# Checking
if l_node['1'].componentsInto[0].type == 'Res' and \
                l_node['1'].componentsInto[0].type == l_node['2'].componentsInto[0].type:
    tOhm += l_node['1'].componentsInto[0].value

if l_node['1'].componentsInto[0].type == 'VSource' and \
                l_node['1'].componentsInto[0].type == l_node['2'].componentsInto[0].type:
    tVoltage += l_node['1'].componentsInto[0].value

print componentCounter
