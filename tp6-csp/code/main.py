import backtracking as bt
import forward_checking as fc
import plot_utils as utils
import pandas as pd
sizes = [4,8,10,12,15]
iterations = 1
results_backtracking = utils.PlotUtils().generateResults(sizes,iterations,bt.NReinasBacktracking)
df1 = pd.DataFrame(results_backtracking)
# Guardar los resultados en un archivo Excel
df1.to_excel("backtracking.xlsx", index=False)
print(f"\nResultados guardados en backtracking.xlsx")

results_forward = utils.PlotUtils().generateResults(sizes,iterations,fc.NReinasForwardChecking)
df2 = pd.DataFrame(results_forward)
# Guardar los resultados en un archivo Excel
df2.to_excel("forward.xlsx", index=False)
print(f"\nResultados guardados en forward.xlsx")

# Comparar resultados
utils.PlotUtils().plot_tiempos(results_backtracking, results_forward)
utils.PlotUtils().plot_estados(results_backtracking, results_forward)