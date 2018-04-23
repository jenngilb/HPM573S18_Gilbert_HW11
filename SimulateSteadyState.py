import UrgentCareClasses as Cls
import Parameters as P
import scr.SamplePathClasses as Path
import SingleServerQueue as Queue

# create an urgent care
urgentCare = Cls.UrgentCare(idn=0)

# simulate and urgent care
simOutputs = urgentCare.simulate(P.SIM_DURATION)

# print trace
urgentCare.print_trace()

# print statistics
simOutputs.print_outputs()

# plot sample paths
for path in simOutputs.samplePaths.get_sample_paths():
    Path.graph_sample_path(
        sample_path=path,
        title=path.get_name(),
        x_label='Simulation time (hour)',
        y_label=''
    )

# to compare the estimates from simulation with the theoretical results
if P.N_EXAM_ROOMS == 1:
    Queue.print_outcomes(P.MEAN_ARRIVAL_TIME, P.MEAN_EXAM_DURATION, P.N_EXAM_ROOMS)
