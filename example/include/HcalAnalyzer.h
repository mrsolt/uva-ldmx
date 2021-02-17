#ifndef ANALYSIS_HCALANALYZER_H
#define ANALYSIS_HCALANALYZER_H

//LDMX Framework
#include "Framework/EventProcessor.h" // Needed to declare processor
#include "Framework/Parameters.h" // Needed to import parameters from configuration file

namespace ldmx {

    /**
     * @class HcalAnalyzer
     * @brief
     */
    class HcalAnalyzer : public framework::Analyzer {
        public:

            HcalAnalyzer(const std::string& name, framework::Process& process) : Analyzer(name, process) {}

            virtual void configure(framework::config::Parameters& ps);

            virtual void analyze(const framework::Event& event);

            virtual void onFileOpen(framework::EventFile&);

            virtual void onFileClose(framework::EventFile&);

            virtual void onProcessStart();

            virtual void onProcessEnd();

        private:

            //Declare private functions and variables here

            double PEthresh_{5}; //PE threshold for vetoing

            //These values are hard-coded for the v12 detector
            double HcalStartZ_{840}; //Z position of the start of the back Hcal for the v12 detector

            double LengthAbs_{25}; //mm Length of absorber

            double LengthSc_{20}; //mm Length of scintillator

            double LengthAir_{2}; //mm Length of air

            float getlambda(float& z);

    };
}

#endif /* ANALYSIS_HCALANALYZER_H */
