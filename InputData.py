POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03

ADD_BACKGROUND_MORT = True  # if background mortality should be added
DELTA_T = 15       # years - unsure if this is correct way to set it

PSA_ON = True      # if probabilistic sensitivity analysis is on

#hmwk q2
#transition matrix for anticoagulation
TRANS_MATRIX = [
    [(1-0.16251892949-0.01680711831-0.01779540311),  0.16251892949,   0.01680711831,    0.01779540311],   # Well
    [0,     0.0,    0.00035078435,    (1-0.00035078435)],   # Stroke
    [0,     0.09561695832,   0.02306085366,   (1.0-0.02306085366-0.09561695832)],   # Post-Stroke
    [0.0,   0.0,    0.0,    1.0,    0.0],   # Dead
    [0.0,   0.0,    0.0,    0.0,    1.0],   # All-cause dead
    ]

#Use RR code from class to modify TRANSITION MATRIX, or build a new matrix and incorporate it with the parameter class.
# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.25
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = .05

HEALTH_UTILITY = [
    1,  # well
    0.2,  # stroke
    0.9,  # post-stroke
    0  # dead
]

HEALTH_COST = [
    0,
    5000,  # stroke
    200,  # post-stroke /year
    0
]

Anticoag_COST = 750

# annual probability of background mortality (number per year per 1,000 population)
ANNUAL_PROB_BACKGROUND_MORT = 18 / 1000
