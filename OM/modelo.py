from pyomo.environ import ConcreteModel, Var, NonNegativeReals, Objective, Constraint, maximize
from pyomo.opt import SolverFactory


model=ConcreteModel()
model.x1=Var(domain=NonNegativeReals)
model.x2=Var(domain=NonNegativeReals)
model.x3=Var(domain=NonNegativeReals)
model.profit=Objective(expr=40*model.x1+20*model.x2+30*model.x3, sense=maximize)
model.r1=Constraint(expr=7*model.x1+3*model.x2+6*model.x3<=150)
model.r1=Constraint(expr=0.4*model.x1+0.4*model.x2+0.5*model.x3<=20)
results=SolverFactory('glpk').solve(model)
results.write()
if results.solver.status=='ok':
    model.pprint()
print('Beneficio=', model.profit())
print('x1=',model.x1())
print('x2=',model.x2())
print('x3=',model.x3())