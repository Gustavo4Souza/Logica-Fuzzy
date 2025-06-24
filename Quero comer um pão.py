import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

fome = ctrl.Antecedent(np.arange(0, 11, 1), 'fome')
tempo = ctrl.Antecedent(np.arange(0, 31, 1), 'tempo')
dieta = ctrl.Antecedent(np.arange(0, 11, 1), 'dieta')
vontade_pao = ctrl.Consequent(np.arange(0, 11, 1), 'vontade_pao')

fome['baixa'] = fuzz.trimf(fome.universe, [0, 0, 5])
fome['media'] = fuzz.trimf(fome.universe, [2, 5, 8])
fome['alta'] = fuzz.trimf(fome.universe, [5, 10, 10])

tempo['pouco'] = fuzz.trimf(tempo.universe, [0, 0, 10])
tempo['medio'] = fuzz.trimf(tempo.universe, [5, 15, 25])
tempo['muito'] = fuzz.trimf(tempo.universe, [20, 30, 30])

dieta['baixa'] = fuzz.trimf(dieta.universe, [0, 0, 5])
dieta['media'] = fuzz.trimf(dieta.universe, [2, 5, 8])
dieta['alta'] = fuzz.trimf(dieta.universe, [5, 10, 10])

vontade_pao['nao_como'] = fuzz.trimf(vontade_pao.universe, [0, 0, 4])
vontade_pao['talvez'] = fuzz.trimf(vontade_pao.universe, [3, 5, 7])
vontade_pao['como'] = fuzz.trimf(vontade_pao.universe, [6, 10, 10])

# regras fuzzy
regra1 = ctrl.Rule(fome['alta'] & tempo['muito'] & dieta['baixa'], vontade_pao['como'])
regra2 = ctrl.Rule(fome['baixa'] | dieta['alta'], vontade_pao['nao_como'])
regra3 = ctrl.Rule(fome['media'] & tempo['medio'], vontade_pao['talvez'])

sistema = ctrl.ControlSystem([regra1, regra2, regra3])
simulador = ctrl.ControlSystemSimulation(sistema)

# Definindo os valores de entrada
simulador.input['fome'] = 10    # valor de 0 a 10
simulador.input['tempo'] = 8    # valor de 0 a 30
simulador.input['dieta'] = 10   # valor de 0 a 10

simulador.compute()

print(f"Vontade de comer pão: {simulador.output['vontade_pao']:.2f}")

