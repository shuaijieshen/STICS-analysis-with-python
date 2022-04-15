import numpy as np
import os
import nlopt
from xml.dom.minidom import parse
import paramchange as pc

class ModelRerunner(object):
    """Reruns a given model with different values of parameters.
    
    Returns simulation results of the model with given parameter values.
    """
    
    def __init__(self, workspace, usm):
        self.workspace = workspace
        self.usm = usm
        
    def __call__(self, par_values):
        model_files = r'E:\material\STICS_training\JavaSTICS-1.41-stics-9.1'
        plant_DOMTree = parse(os.path.join(model_files, r'plant\cornnew_plt.xml')) #读取文件为树
        origin_plant = plant_DOMTree.documentElement
        soil_DOMTree = parse(os.path.join(workspace, 'sols.xml'))
        origin_siol = soil_DOMTree.documentElement

        par_names = ['tcmax', 'adil', 'udlaimax', 'teoptbis']
        for i in range(len(par_names)):
            pc.parset(par_names[i], par_values[i], os.path.join(model_files, r'plant\cornnew_plt.xml'))
        # run model
        
        os.chdir(model_files)
        os.system(r'JavaSticsCmd.exe %s %s %s' % ('--run',workspace, usm))
        
        with open(r'E:\material\STICS_training\WUQIAOmaizeSA\mod_rapport.sti') as outtext:
            outlines = outtext.readlines()
            newline = outlines[-1].replace(' ', '')
            spice = newline.split(';')  
        # clear overrides
        with open(os.path.join(model_files, r'plant\cornnew_plt.xml'), 'w') as f:
            origin_plant.writexml(f)
        with open(os.path.join(workspace, 'sols.xml'), 'w') as f:
            origin_siol.writexml(f)
        return np.array(spice[-7:-1]).astype(float)
    
    
class ObjectiveFunctionCalculator(object):
    """Computes the objective function.
    
    This class runs the simulation model with given parameter values and returns the objective
    function as the sum of squared difference between observation and simulation.
    """
    
    def __init__(self, workspace, usm, observations):
        self.modelrerunner = ModelRerunner(workspace, usm)
        self.df_observations = observations
        self.n_calls = 0
       
    def __call__(self, par_values, grad=None):
        """Runs the model and computes the objective function for given par_values.
        
        The input parameter 'grad' must be defined in the function call, but is only
        required for optimization methods where analytical gradients can be computed.
        """
        self.n_calls += 1
        print(".", end="")
        # Run the model and collect output
        self.df_simulations = self.modelrerunner(par_values)
        # compute the differences by subtracting the DataFrames
        # Note that the dataframes automatically join on the index (dates) and column names
        df_differences_yield = self.df_observations[0] - self.df_simulations[0]
        df_differences_biomass = self.df_observations[1] - self.df_simulations[1]
        # Compute the RMSE on the LAI column
        obj_func = (np.sqrt(np.mean(df_differences_yield**2))+
                    np.sqrt(np.mean(df_differences_biomass**2)))
        return obj_func

    
workspace = r'E:\WUQIAOmaizeSA'
usm = 'WM_T_M2017'
obs = [8, 15]

tcmax_range = [27, 37]
adil_range = [2.5, 4.5]
udlaimax_range = [2, 3]
teoptbis_range = [20, 30]
objfunc_calculator = ObjectiveFunctionCalculator(workspace, usm, obs)
# Start optimizer with the SUBPLEX algorithm for two parameters
opt = nlopt.opt(nlopt.LN_SBPLX, 4)
# Assign the objective function calculator
opt.set_min_objective(objfunc_calculator)
# lower bounds of parameters values
opt.set_lower_bounds([tcmax_range[0], adil_range[0], udlaimax_range[0], teoptbis_range[0]])
# upper bounds of parameters values
opt.set_upper_bounds([tcmax_range[1], adil_range[1], udlaimax_range[1], teoptbis_range[1]])
# the initial step size to compute numerical gradients
opt.set_initial_step([2, 0.2, 0.3, 2])
# Maximum number of evaluations allowed
opt.set_maxeval(3000)
# Relative tolerance for convergence
opt.set_stopval(0.5)
# opt.set_ftol_rel(3000)
# Start the optimization with the first guess
firstguess = [35, 3, 3, 25]
x = opt.optimize(firstguess)
print("\noptimum at tcmax: %s, adil: %s, udlaimax: %s, teoptbis: %s" % (x[0], x[1], x[2], x[3]))
print("minimum value = ",  opt.last_optimum_value())
print("result code = ", opt.last_optimize_result())
print("With %i function calls" % objfunc_calculator.n_calls)
