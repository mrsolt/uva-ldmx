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
    class HcalAnalyzer : public Analyzer {
        public:

            HcalAnalyzer(const std::string& name, Process& process) : Analyzer(name, process) {}

            virtual void configure(Parameters& ps);

            virtual void analyze(const Event& event);

            virtual void onFileOpen(EventFile&);

            virtual void onFileClose(EventFile&);

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
