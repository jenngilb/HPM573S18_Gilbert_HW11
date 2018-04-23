
def print_outcomes(mean_interarrival_time, mean_service_duration, n_servers):
    """
    prints performance measures for a single-server queue
    :param mean_interarrival_time: mean of patients inter-arrival time
    :param mean_service_duration: mean duration of service
    :param n_servers:
    """
    lamd = 1/mean_interarrival_time         # arrival rate
    mu = n_servers/mean_service_duration    # service rate

    if n_servers > 1:
        raise ValueError('These theoretical results hold only for single-server queues.')
    if lamd > mu:
        raise ValueError('Arrival rate cannot be greater than service rate.')

    print('Theoretical results from analyzing a single-server queue:')
    print('  Average number of patients in the urgent care:', lamd / (mu - lamd))
    print('  Average number of patients in the waiting room:', lamd**2 / mu / (mu - lamd))
    print('  Average amount of time a patient spend in the system:', 1 / (mu - lamd))
    print('  Average amount of time a patient spend in the waiting room:', lamd / mu / (mu - lamd))
    print('  Server utilization:', lamd/mu)
