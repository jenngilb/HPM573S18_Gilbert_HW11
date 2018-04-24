POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 15         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03

ADD_BACKGROUND_MORT = True  # if background mortality should be added
DELTA_T = 5       # years - unsure if this is correct way to set it

PSA_ON = True      # if probabilistic sensitivity analysis is on


# transition matrix
TRANS_MATRIX = [
    [(1-0.16251892949-0.01680711831-0.01779540311),  0.16251892949,   0.01680711831,    0.01779540311],   # Well
    [0,     0.0,    0.00035078435,    (1-0.00035078435)],   # Stroke
    [0,     0.09561695832,   0.02306085366,   (1.0-0.02306085366-0.09561695832)],   # Post-Stroke
    [0.0,   0.0,    0.0,    1.0,    0.0],   # Dead
    [0.0,   0.0,    0.0,    0.0,    1.0],   # All-cause dead
    ]

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05

HEALTH_UTILITY = [
    1,  # well
    0.8865,  # stroke ONLY WHEN THE CYCLE LENGTH IS 1 YEAR
    0.9,  # post-stroke
    0  # dead
]

HEALTH_COST = [
    0,
    5000,  # stroke
    200,  # post-stroke /year
    0
]

Anticoag_COST = 2000

# annual probability of background mortality (number per year per 1,000 population)
ANNUAL_PROB_BACKGROUND_MORT = 18 / 1000
