import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Define the Bayesian Network
model = BayesianNetwork([('Fire', 'Alarm'), ('Burglary', 'Alarm'), ('Alarm', 'David call'), ('Alarm', 'Sophia call')])

# Define the Conditional Probability Distributions (CPDs)
cpd_fire = TabularCPD(variable='Fire', variable_card=2, values=[[0.999], [0.001]])  # Example values
cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.002], [0.998]])  # Example values
cpd_alarm = TabularCPD(variable='Alarm', variable_card=2, values=[[0.999, 0.05, 0.69, 0.06], [0.001, 0.95, 0.31, 0.94]],
                       evidence=['Fire', 'Burglary'], evidence_card=[2, 2])  # Example values
cpd_david_call = TabularCPD(variable='David call', variable_card=2, values=[[0.95, 0.09], [0.05, 0.91]],
                            evidence=['Alarm'], evidence_card=[2])  # Example values
cpd_sophia_call = TabularCPD(variable='Sophia call', variable_card=2, values=[[0.98, 0.25], [0.02, 0.75]],
                             evidence=['Alarm'], evidence_card=[2])  # Example values

# Add CPDs to the model
model.add_cpds(cpd_fire, cpd_burglary, cpd_alarm, cpd_david_call, cpd_sophia_call)

# Verify the model's structure and CPDs
assert model.check_model()

# Print the structure of the Bayesian network
print("\nBayesian Network Structure:")
print(model.edges())

# Print the CPDs of each variable in the Bayesian network
print("\nConditional Probability Distributions (CPDs):")
for variable in model.nodes():
    cpd = model.get_cpds(variable)
    print(f"\nCPD for {variable}:")
    print(cpd)