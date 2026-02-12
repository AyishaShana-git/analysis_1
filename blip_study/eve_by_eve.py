
import uproot

# Open ROOT file
file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
tree = file["pdblipana/BlipRecoAlg/matchtree"]

# Read branches as arrays
qA = tree["qA"].array(library="np")
dt = tree["dt"].array(library="np")

n_events = len(qA)

print("Total events in tree:", n_events)

# Loop over events one by one
for i in range(n_events):
    charge = qA[i]
    time   = dt[i]

    # Example cut
    if time < 10:
        print(f"Event {i}: qA = {charge:.2f}, dt = {time:.2f}  --> PASSED")
    else:
        print(f"Event {i}: qA = {charge:.2f}, dt = {time:.2f}  --> FAILED")
