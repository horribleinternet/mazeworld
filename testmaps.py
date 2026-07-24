from block import Block, VoidBlock

def S():
    return Block()

def V():
    return VoidBlock()

testmap1 = [
    [ S(), S(), S(), S(), S(), S(), S() ],
    [ S(), S(), S(), V(), V(), S(), S() ],
    [ S(), S(), S(), V(), V(), V(), S() ],
    [ S(), V(), V(), V(), S(), V(), S() ],
    [ S(), S(), S(), V(), S(), V(), S() ],
    [ S(), S(), S(), V(), V(), V(), S() ],
    [ S(), S(), S(), S(), S(), S(), S() ]
]
