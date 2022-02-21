from decouple import config
from quidaxapi.quidax import Quidax

quidax = Quidax(config("QUIDAX_SECRET_KEY"))
