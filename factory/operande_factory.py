from factory.ii_operande_factory import IOperandeFactory
from instruction.i_operande import IOperande
from instruction.const_operande import ConstOperande
from instruction.simple_operande import SimpleOperande
from instruction.memory_operande import MemoryOperande
from instruction.repere_operande import RepereOperande


class OperandeFactory(IOperandeFactory):
    def get_operande(val: str) -> IOperande:
        if val[0] == "0":
            return ConstOperande(int(val, base=16))
        elif val[0] == "[":
            val = val.replace('[','')
            val = val.replace(']','')
            a = val.split('+')
            if len(a) == 1:
                if a[0][0] == "0":
                    return MemoryOperande("null", "null", 0, int(a[0], base=16))
                elif '*' in a[0]:
                    b = a[0].split('*')
                    return MemoryOperande("null", b[0], int(b[1], base=16), 0)
                else:
                    return MemoryOperande(a[0], "null", 0, 0)
            elif len(a) == 2:
                if '*' in a[0]:
                    b = a[0].split('*')
                    return MemoryOperande("null", b[0], int(b[1], base=16), int(a[1], base=16))
                elif '*' in a[1]:
                    b = a[1].split('*')
                    return MemoryOperande(a[0], b[0], int(b[1], base=16), 0)
                else:
                    return MemoryOperande(a[0], "null", 0, int(a[1], base=16))
            else:
                b = a[1].split('*')
                return MemoryOperande(a[0], b[0], int(b[1], base=16), int(a[2], base=16))     
        elif val[0] == '@':
            return RepereOperande(val[1:])
        else:
            return SimpleOperande(val)