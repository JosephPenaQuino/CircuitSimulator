codeCounter=0
global.componentCounter= 0

class Component():
    def __init__(self):
        self.nodesLinked = []

    def setNodes(self,nodes):
        self.nodesLinked = nodes

class nodes():
    def __init__(self):
        self.code = "xxxx"
        self.name = "-"
        self.componentsInto = []
    def setCode(self,CodeN):
        self.code = CodeN

    def setName(self,nameN):
        self.name = nameN

    def setComponents(self,Component):
        self.componentsInto.append(Component)
        componentCounter = componentCounter + 1


class Resistors(Component):
    def setOhms(self,numbersOhms=2200):
        self.value = numbersOhms
        self.type = 'Res'

class VoltageSource(Component):
    def setVoltage(self,numberVoltage = 22):
        self.value = numberVoltage
        self.type = 'VSource'


#Creating the nodes
node1 = nodes()
node2 = nodes()

#Indexing the nodes
lnode = {
    '1': node1,
    '2': node2

}

#Creating components
r1 = Resistors()
r1.setOhms(1000)

#Creting Sources
v1 = VoltageSource()
v1.setVoltage(6)

lnode['1'].setComponents(r1)
lnode['2'].setComponents(r1)
lnode['1'].setComponents(v1)
lnode['2'].setComponents(v1)

print lnode['1'].componentsInto[0].value
print lnode['1'].componentsInto[1].value
print lnode['2'].componentsInto[0].value
print lnode['2'].componentsInto[1].value

tOhm = 0
tVoltage = 0

# Checking
if lnode['1'].componentsInto[0].type == 'Res' and lnode['1'].componentsInto[0].type == lnode['2'].componentsInto[0].type:
    tOhm += lnode['1'].componentsInto[0].value

if lnode['1'].componentsInto[0].type == 'VSource' and lnode['1'].componentsInto[0].type == lnode['2'].componentsInto[0].type:
    tVoltage += lnode['1'].componentsInto[0].value

print componentCounter
