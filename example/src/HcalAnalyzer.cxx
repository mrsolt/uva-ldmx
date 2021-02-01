#include "Analysis/HcalAnalyzer.h"
#include "SimCore/Event/SimParticle.h"
#include "DetDescr/HcalID.h"
#include "Framework/NtupleManager.h"

namespace ldmx {

    void HcalAnalyzer::configure(Parameters& ps) {

        PEthresh_ = ps.getParameter<double>("PEthresh_"); //PE threshold for vetoing
        //These values are hard-coded for the v12 detector
        HcalStartZ_ = ps.getParameter<double>("HcalStartZ_"); //Z position of the start of the back Hcal for the v12 detector
        LengthAbs_ = ps.getParameter<double>("LengthAbs_"); //Length of Absorber
        LengthSc_ = ps.getParameter<double>("LengthSc_"); //Length of Scintillator
        LengthAir_ = ps.getParameter<double>("LengthAir_"); //Length of Air
        return;
    }

    void HcalAnalyzer::analyze(const Event& event) {

        //Grab the SimParticle Map
        auto particle_map{event.getMap<int, ldmx::SimParticle>("SimParticles")};

        //Loop over all SimParticles
        for (auto const& it : particle_map) {
          SimParticle p = it.second;
          int pdgid = p.getPdgID();
          histograms_.fill("SimParticlePdgID", pdgid);
          //Only select the neutron for now
          //Note other neutrons can be created in the event, currently I don't distinguish between them for now
          if(pdgid == 2112){
            std::vector<double> vert = p.getVertex();
            std::vector<double> endvert = p.getEndPoint();
            std::vector<double> mom = p.getMomentum();
            //std::vector<double> endmom = p.getEndMomentum();

            //Fill SimParticle Histograms
            histograms_.fill("SimParticleEnergy", p.getEnergy());
            histograms_.fill("SimParticleX", vert[0]);
            histograms_.fill("SimParticleY", vert[1]);
            histograms_.fill("SimParticleZ", vert[2]);
            histograms_.fill("SimParticleEndX", endvert[0]);
            histograms_.fill("SimParticleEndY", endvert[1]);
            histograms_.fill("SimParticleEndZ", endvert[2]);
            histograms_.fill("SimParticlePx", mom[0]);
            histograms_.fill("SimParticlePy", mom[1]);
            histograms_.fill("SimParticlePz", mom[2]);
            //histograms_.fill("SimParticleEndPx", endmom[0]);
            //histograms_.fill("SimParticleEndPy", endmom[1]);
            //histograms_.fill("SimParticleEndPz", endmom[2]);

            //Fill SimParticle Tuple Variables
            ntuple_.setVar<float>("neutron_energy", p.getEnergy());
            ntuple_.setVar<float>("neutron_startX", vert[0]);
            ntuple_.setVar<float>("neutron_startY", vert[1]);
            ntuple_.setVar<float>("neutron_startZ", vert[2]);
            ntuple_.setVar<float>("neutron_endX", endvert[0]);
            ntuple_.setVar<float>("neutron_endY", endvert[1]);
            ntuple_.setVar<float>("neutron_endZ", endvert[2]);
            ntuple_.setVar<float>("neutron_startPx", mom[0]);
            ntuple_.setVar<float>("neutron_startPy", mom[1]);
            ntuple_.setVar<float>("neutron_startPz", mom[2]);
          }
        }

        //Grad the HcalVeto collection and the associated max PE hit
        auto hcalVeto{event.getObject<HcalVetoResult>("HcalVeto")};
        auto maxPEHit{hcalVeto.getMaxPEHit()};

        //Grab maxPEHit info
        HcalID maxPEdetID(maxPEHit.getID());
        int maxPEsection = maxPEdetID.getSection(); //Front, back, side, etc.
        int maxPEstrip = maxPEdetID.getStrip();
        int maxPElayer = maxPEdetID.getLayerID();

        int maxPE = maxPEHit.getPE();
        int minPE = maxPEHit.getMinPE();
        float maxPEenergy = maxPEHit.getEnergy();
        float maxPEtime = maxPEHit.getTime();
        float maxPEamplitude = maxPEHit.getAmplitude();
        float maxPEx = maxPEHit.getXPos();
        float maxPEy = maxPEHit.getYPos();
        float maxPEz = maxPEHit.getZPos();

        //Fill HcalVeto Histograms
        histograms_.fill("passveto", hcalVeto.passesVeto());
        histograms_.fill("maxPEsection", maxPEsection);
        histograms_.fill("maxPElayer", maxPElayer);
        histograms_.fill("maxPEstrip", maxPEstrip);
        histograms_.fill("maxPEamplitude", maxPEamplitude);
        histograms_.fill("maxPEenergy", maxPEenergy);
        histograms_.fill("maxPEtime", maxPEtime);
        histograms_.fill("maxPEx", maxPEx);
        histograms_.fill("maxPEy", maxPEy);
        histograms_.fill("maxPEz", maxPEz);
        histograms_.fill("maxPE", maxPE);

        //Fill HcalVeto Tuple Variables
        ntuple_.setVar<int>("passveto", hcalVeto.passesVeto());
        ntuple_.setVar<int>("maxPEsection", maxPEsection);
        ntuple_.setVar<int>("maxPElayer", maxPElayer);
        ntuple_.setVar<int>("maxPEstrip", maxPEstrip);
        ntuple_.setVar<float>("maxPEamplitude", maxPEamplitude);
        ntuple_.setVar<float>("maxPEenergy", maxPEenergy);
        ntuple_.setVar<float>("maxPEtime", maxPEtime);
        ntuple_.setVar<float>("maxPEx", maxPEx);
        ntuple_.setVar<float>("maxPEy", maxPEy);
        ntuple_.setVar<float>("maxPEz", maxPEz);
        ntuple_.setVar<int>("maxPE", maxPE);

        //Grab the Hcal Reconstructed Hits
        std::vector<HcalHit> hcalHits = event.getCollection<HcalHit>("HcalRecHits");

        int sumPE = 0;
        float minZ = 9999; //Minimum z is the minimum amount of material required to veto event
        for (const HcalHit &hit : hcalHits ) {
            //Grab the hit information
            HcalID detID(hit.getID());
            int section = detID.getSection(); //Front, back, side, etc.
            int strip = detID.getStrip();
            int layer = detID.getLayerID();
            int PE = hit.getPE();
            int minPE = hit.getMinPE();
            float energy = hit.getEnergy();
            float time = hit.getTime();
            float amplitude = hit.getAmplitude();
            float x = hit.getXPos();
            float y = hit.getYPos();
            float z = hit.getZPos();

            //Fill the Hcal Reconstructed Hits Histograms
            histograms_.fill("section", section);
            histograms_.fill("layer", layer);
            histograms_.fill("strip", strip);
            histograms_.fill("amplitude", amplitude);
            histograms_.fill("energy", energy);
            histograms_.fill("time", time);
            histograms_.fill("x", x);
            histograms_.fill("y", y);
            histograms_.fill("z", z);
            histograms_.fill("PE", PE);
            histograms_.fill("minPE", minPE);
            //Is this a minimum z?
            if(z < minZ && PE >= PEthresh_ && z >= HcalStartZ_){
              minZ = z;
            }
            sumPE += PE;
          }

        //Calculate the lambda for the minimum z
        float lambda = getlambda(minZ);

        //Fill Hcal Veto Histograms
        histograms_.fill("sumPE", sumPE);
        histograms_.fill("minZ", minZ);
        histograms_.fill("lambda", lambda);

        //Fill Hcal Veto tuple variables
        ntuple_.setVar<int>("sumPE", sumPE);
        ntuple_.setVar<float>("minZ", minZ);
        ntuple_.setVar<float>("lambda", lambda);

        return;
    }

    void HcalAnalyzer::onFileOpen(EventFile&) {

        return;
    }

    void HcalAnalyzer::onFileClose(EventFile&) {

        return;
    }

    void HcalAnalyzer::onProcessStart() {

        //Define tuple
        ntuple_.create("HcalAna");

        //Define branches for the Tuple

        //Define SimParticle tuple branches for neutrons
        ntuple_.addVar<float> ("HcalAna", "neutron_energy");
        ntuple_.addVar<float> ("HcalAna", "neutron_startX");
        ntuple_.addVar<float> ("HcalAna", "neutron_startY");
        ntuple_.addVar<float> ("HcalAna", "neutron_startZ");
        ntuple_.addVar<float> ("HcalAna", "neutron_endX");
        ntuple_.addVar<float> ("HcalAna", "neutron_endY");
        ntuple_.addVar<float> ("HcalAna", "neutron_endZ");
        ntuple_.addVar<float> ("HcalAna", "neutron_startPx");
        ntuple_.addVar<float> ("HcalAna", "neutron_startPy");
        ntuple_.addVar<float> ("HcalAna", "neutron_startPz");

        //Define tuple branches for HcalVeto
        ntuple_.addVar<int> ("HcalAna", "passveto");
        ntuple_.addVar<int> ("HcalAna", "maxPEsection");
        ntuple_.addVar<int> ("HcalAna", "maxPElayer");
        ntuple_.addVar<int> ("HcalAna", "maxPEstrip");
        ntuple_.addVar<float> ("HcalAna", "maxPEamplitude");
        ntuple_.addVar<float> ("HcalAna", "maxPEenergy");
        ntuple_.addVar<float> ("HcalAna", "maxPEtime");
        ntuple_.addVar<float> ("HcalAna", "maxPEx");
        ntuple_.addVar<float> ("HcalAna", "maxPEy");
        ntuple_.addVar<float> ("HcalAna", "maxPEz");
        ntuple_.addVar<int> ("HcalAna", "maxPE");
        ntuple_.addVar<int> ("HcalAna", "sumPE");
        ntuple_.addVar<float> ("HcalAna", "minZ");
        ntuple_.addVar<float> ("HcalAna", "lambda");

        return;
    }

    void HcalAnalyzer::onProcessEnd() {

        return;
    }

    //TODO: This function has hardcoded geometry info from the v12 detector
    //This also assumes every layer has the same absorber length
    float HcalAnalyzer::getlambda(float &z){
        //Hcal back starts at 840 mm
        float start_hcal = HcalStartZ_;
        float lambda_abs = 167;
        float lambda_sc = 800;
        //The absorber length is 25 mm
        float length_abs = LengthAbs_;
        //The scintillator length is 20 mm
        float length_sc = LengthSc_;
        float length_air = LengthAir_;

        //The width of a single layer is 49 mm
        float width = 2 * length_air + length_sc + length_abs;
        float z_new = z - start_hcal;
        float start2 = length_sc + length_air;
        float start3 = start2 + 2 * length_air + length_abs + length_sc;

        float z_abs = 0;
        float z_sc = 0;

        //If z is behind the front face of the back Hcal, return 0
        if(z_new <= 0){
            return 0;
        }

        float n_lay = z_new / width;
        int n = std::floor(n_lay); //Calculate the Hcal layer numbers
        float depth = (n_lay - n) * width; //calculate the depth in the given Hcal layer

        //Is the z in the absorber?
        if(depth < length_abs){
            z_abs = (length_abs * n) + depth;
            z_sc = n * length_sc;
        }
        //Is the z in air?
        else if(depth >= length_abs && depth < length_abs + length_air){
            z_abs = (n + 1) * length_abs;
            z_sc = n * length_sc;
        }
        //Is the z in scintillator?
        else if(depth >= length_abs + length_air && depth < length_abs + length_air + length_sc){
            z_abs = (n + 1) * length_abs;
            z_sc = n * length_sc + (depth - length_abs - length_air);
        }
        //Is the z in air?
        else if(depth >= length_abs + length_air + length_sc){
            z_abs = (n + 1) * length_abs;
            z_sc = (n + 1) * length_sc;
        }

        float lambda = z_sc / lambda_sc + z_abs / lambda_abs; //Calculate lambda
        return lambda;
    }
}

DECLARE_ANALYZER_NS(ldmx, HcalAnalyzer)
