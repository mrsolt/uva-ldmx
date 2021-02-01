"""Configuration class for HcalAnalyzer

You can put several of these class definitions in the
same file if you want. Helps condense the python module.
"""

from LDMX.Framework.ldmxcfg import Analyzer

class HcalAnalyzer(Analyzer):
    """Configuration class for HcalAnalyzer

    Attributes
    ----------
    Document your parameters here!
    """

    def __init__(self, name = 'myana') :
        super().__init__(name,'ldmx::HcalAnalyzer', 'Analysis')

        #Put parameters and their defaults here, for example
        self.PEthresh_ = 5.; #PE threshold for vetoing
        #These values are hard-coded for the v12 detector
        self.HcalStartZ_ = 840.; #Z position of the start of the back Hcal for the v12 detector
        self.LengthAbs_ = 25.; #mm Length of absorber
        self.LengthSc_ = 20.; #mm Length of scintillator
        self.LengthAir_ = 2.; #mm Length of air

        #Define histograms

        #SimParticle Histograms
        self.build1DHistogram("SimParticleEnergy",  "SimParticleEnergy", 100, 0, 5000);
        self.build1DHistogram("SimParticlePdgID",  "SimParticlePdgID", 100, -50, 3000);
        self.build1DHistogram("SimParticleX",  "SimParticleX", 100, -1500, 1500);
        self.build1DHistogram("SimParticleY",  "SimParticleY", 100, -1500, 1500);
        self.build1DHistogram("SimParticleZ",  "SimParticleZ", 100, 0, 5000);
        self.build1DHistogram("SimParticleEndX",  "SimParticleEndX", 100, -1500, 1500);
        self.build1DHistogram("SimParticleEndY",  "SimParticleEndY", 100, -1500, 1500);
        self.build1DHistogram("SimParticleEndZ",  "SimParticleEndZ", 100, 0, 5000);
        self.build1DHistogram("SimParticlePx",  "SimParticlePx", 100, -1000, 1000);
        self.build1DHistogram("SimParticlePy",  "SimParticlePy", 100, -1000, 1000);
        self.build1DHistogram("SimParticlePz",  "SimParticlePz", 100, -1000, 4000);
        #self.build1DHistogram("SimParticleEndPx",  "SimParticleEndPx", 100, -1000, 1000);
        #self.build1DHistogram("SimParticleEndPy",  "SimParticleEndPy", 100, -1000, 1000);
        #self.build1DHistogram("SimParticleEndPz",  "SimParticleEndPz", 100, -1000, 4000);

        #Hcal Reconstruction Histograms
        self.build1DHistogram("section",  "section", 5, 0, 5);
        self.build1DHistogram("layer",  "layer", 100, 0, 100);
        self.build1DHistogram("strip",  "strip", 100, 0, 100);
        self.build1DHistogram("amplitude",  "amplitude", 100, 0, 5000);
        self.build1DHistogram("energy",  "energy", 100, 0, 500);
        self.build1DHistogram("time",  "time", 100, 0, 100);
        self.build1DHistogram("x",  "x", 100, -1500, 1500);
        self.build1DHistogram("y",  "y", 100, -1500, 1500);
        self.build1DHistogram("z",  "z", 100, 0, 5000);
        self.build1DHistogram("PE",  "PE", 100, 0, 5000);
        self.build1DHistogram("minPE",  "minPE", 100, 0, 5000);
        self.build1DHistogram("sumPE",  "sumPE", 100, 0, 5000);

        #Hcal Veto Histograms
        self.build1DHistogram("passveto",  "passveto", 2, 0, 2);
        self.build1DHistogram("maxPEsection",  "maxPEsection", 5, 0, 5);
        self.build1DHistogram("maxPElayer",  "maxPElayer", 100, 0, 100);
        self.build1DHistogram("maxPEstrip",  "maxPEstrip", 100, 0, 100);
        self.build1DHistogram("maxPEamplitude",  "maxPEamplitude", 100, 0, 5000);
        self.build1DHistogram("maxPEenergy",  "maxPEenergy", 100, 0, 500);
        self.build1DHistogram("maxPEtime",  "maxPEtime", 100, 0, 100);
        self.build1DHistogram("maxPEx",  "maxPEx", 100, -1500, 1500);
        self.build1DHistogram("maxPEy",  "maxPEy", 100, -1500, 1500);
        self.build1DHistogram("maxPEz",  "maxPEz", 100, 0, 5000);
        self.build1DHistogram("maxPE",  "maxPE", 100, 0, 5000);
        self.build1DHistogram("minZ",  "minZ", 100,0,4000);
        self.build1DHistogram("lambda",  "lambda", 100,0,16);
