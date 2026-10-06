import pyomo.environ as pyo

model = pyo.AbstractModel()

# Conjuntos
model.A = pyo.Set()   # tipos de avión
model.V = pyo.Set()   # aldeas

# Parámetros
model.c = pyo.Param(model.A, model.V, within=pyo.NonNegativeReals)  # alimento por viaje
model.viajes = pyo.Param(model.A, within=pyo.NonNegativeIntegers)   # viajes máx. por avión
model.vuelos = pyo.Param(model.V, within=pyo.NonNegativeIntegers)   # vuelos máx. por aldea

# Variables: nº de viajes del avión i a la aldea j
model.x = pyo.Var(model.A, model.V, domain=pyo.NonNegativeIntegers)

# Objetivo: maximizar alimento distribuido por día
def obj_rule(m):
    return sum(m.c[i, j] * m.x[i, j] for i in m.A for j in m.V)

model.OBJ = pyo.Objective(rule=obj_rule, sense=pyo.maximize)

# Restricción: viajes de cada avión
def viajes(m, i):
    return sum(m.x[i, j] for j in m.V) <= m.viajes[i]
model.RViajes = pyo.Constraint(model.A, rule=viajes)

# Restricción: vuelos sobre cada aldea
def vuelos(m, j):
    return sum(m.x[i, j] for i in m.A) <= m.vuelos[j]
model.RVuelos = pyo.Constraint(model.V, rule=vuelos)