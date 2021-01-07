# HCal Neutral Configs
The following config files shoot 10,000 K-longs and neutrons at 1 GeV at the front face of the HCal. You can run the scripts by doing the following:

```bash
ldmx fire kaons.py <run number> output.root
```
```bash
ldmx fire neutrons.py <run number> output.root
```

Note the run number set the seed, so when running multiple jobs the run number needs to be different for each job submission.
