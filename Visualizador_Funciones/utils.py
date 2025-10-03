from sympy.calculus.util import continuous_domain
from sympy.sets import Reals, Intersection, Interval , Union
from sympy import symbols , sympify, lambdify, SympifyError, diff  , oo
from numpy import linspace, array


x = symbols('x')

def fnc_input():
    x = symbols('x')
    entrada = input("Introduce una función de x (ej: sin(x)**2 + log(x)): ")
    try:
        # Parsear string a fncesión simbólica segura
        fnc = sympify(entrada)
        der = diff(fnc, x)

        # Convertir a función evaluable con numpy
        f = lambdify(x, fnc, modules=['numpy'])
        d = lambdify(x, der, modules=['numpy'])

        return f, fnc, der , d

    except SympifyError:
        raise SympifyError("La función no se pudo interpretar como una fncesión válida.")

def determinar_dominio(expr):
    try:
        dom = continuous_domain(expr, x, Reals) # 1. Dominio donde la función es continua sobre ℝ
        return dom
    except Exception as e:
        print(f"⚠️ No se pudo determinar el dominio: {e}")
        return None

def interval_to_numpy(dom, steps=10000, upper_limit=10):
    """
    Convierte un dominio simbólico (Interval o Union) a arreglos de NumPy para graficar.
    Si el dominio es una unión de intervalos, se filtra la malla completa.
    """
    if isinstance(dom, Interval):
        a = float(dom.start) if dom.start != -oo else -upper_limit
        b = float(dom.end) if dom.end != oo else upper_limit
        return linspace(a, b, steps)
    
    elif isinstance(dom, Union):
        return filtrar_dominio(dom, steps, -upper_limit, upper_limit)
    
    else:
        raise ValueError(f"Tipo de dominio no soportado: {type(dom)}")

def filtrar_dominio(dom, steps=10000, lower=-10, upper=10):
    """
    Devuelve un array de puntos x dentro del dominio `dom` (Union, Interval, Complement, etc.)
    Evaluando si cada punto pertenece al conjunto.
    """
    x_vals = linspace(lower, upper, steps)
    
    # Optimizamos usando boolean array + numpy para más velocidad
    x_validos = [xi for xi in x_vals if dom.contains(xi)]
    
    return array(x_validos)
