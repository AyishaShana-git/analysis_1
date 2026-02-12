
import ROOT

# Open file
f = ROOT.TFile.Open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
if not f or f.IsZombie():
    print("Error opening file")

# Get tree
tree = f.Get("pdblipana/anatree")
if not tree:
    print("Tree not found")

# Create histogram
h = ROOT.TH1F(
    "h_blip_energy",
    "Blip Energy;Energy (MeV);Entries",
    100, 0, 5
)

# Fill histogram
for event in tree:
    for E in event.blip_energy:
        h.Fill(E)

# Draw
c = ROOT.TCanvas("c", "BlipEnergy", 800, 600)
h.Draw()
c.SaveAs("blip_energy_pyroot.pdf")
  
