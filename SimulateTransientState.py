import UrgentCareClasses as Cls
import Parameters as P
import scr.SamplePathClasses as Path

# create a collection of urgent care
colUrgentCares = Cls.ColOfUrgentCares(
    ids=range(P.N_SIM_REPLICATS))

# simulate and urgent care
colUrgentCares.simulate()

# print statistics
colUrgentCares.print_outputs()

# plot sample paths for the number of patients in urgent care
if P.N_SIM_REPLICATS <= 10:
    Path.graph_sample_paths(
        sample_paths=colUrgentCares.nPatientsSamplePaths,
        title='Number of patients in urgent care',
        x_label='Simulation time (hour)',
        y_label='',
        transparency=0.75
    )
