from factory.ii_operande_factory import IOperandeFactory
from instruction.i_operande import IOperande
from instruction.const_operande import ConstOperande
from instruction.simple_operande import SimpleOperande


class OperandeFactory(IOperandeFactory):
    def get_operande(val: str) -> IOperande:
        if val[0] == "0":
            return ConstOperande(int(val, base=16))
        else:
            return SimpleOperande(val)