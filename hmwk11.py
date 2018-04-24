print("Hmwk Q1, Part 1:")
print("Annual all-cause mortality = 18/1000")
print("-ln(1-(18/1000))= 0.01816397 = all-cause mortality modeling rate")
print("Annual death rate for stroke = 36.2/100,000")
print("-ln(1-(36.2/100,000))= 0.00036207 = stroke annual mortality modeling rate")
print("Non-stroke associated annual mortality rate = (18*100) – 36.2 per 100,000 = 1763.8/100,000")
print("-ln(1-(1763.8/100,000)) = 0.01779540311 = non-stroke associated annual mortality modeling rate")
print("Part 2:")
print("Rate of new cases of stroke = 15/1000. Assume everyone is diagnosed")
print("-ln(1-(15/1000)) = 0.01511363781 = annual rate of stroke events for our population")
print("Part 3:")
print("P(survive stroke) = .9, P(stroke death) = .1")
print("-ln(1-((15)/(1-.9)/1000)) = 0.16251892949 = annual rate of transition from well to stroke")
print("-ln(1-((15)/(1-.1)/1000)) = 0.01680711831 = annual rate of transition from well to stroke death")
print("Part 4:")
print("-ln(1-((15)/(1-.17)/1000)) = 0.01823758754 = annual rate of recurrent strokes")
print("Part 5:")
print("P(survive recurrent stroke) = .8, P(recurrent stroke death) = .2")
print("-ln(1-(0.01823758754)/(1-.8)) = 0.09561695832 = annual rate of transition from post-stroke to stroke")
print("-ln(1-(0.01823758754)/(1-.2)) = 0.02306085366 = annual rate of transition from post-stroke to stroke death")
print("Part 6:")
print("-ln(1-(0.01823758754)/(52/1) = 0.00035078435 = annual rate of transition from stroke to post-stroke")
