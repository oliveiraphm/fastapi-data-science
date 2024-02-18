import time
from datetime import datetime

from pydantic import BaseModel


class Model(BaseModel): 
    # Don't do this.
    # This example shows you why it doesn't work.
    # A atribuição só acontece uma vez quando a classe é importante e não é feita cada vez que um objeto diferente é instanciado!
    d: datetime = datetime.now()


o1 = Model()
print(o1.d)

time.sleep(1)  # Wait for a second

o2 = Model()
print(o2.d)

print(o1.d < o2.d)  # False