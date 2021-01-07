# uva-ldmx
A repository of instructions and script specific to the University of Virginia LDMX group.

Instructions for UVA Rivanna

These instructions are taken from the LDMX wiki and adapted to the UVA Rivanna computers.
https://ldmx-software.github.io

ldmx-sw

Operating ldmx-sw in the container (which contains all the correct versions of the required software) is the simplest and cleanest way to build and run the LDMX software. ldmx-sw uses a Docker image, but this requires sudo privileges on Rivanna. However, docker images can be downloaded and converted using singularity. First, make sure you are operating in a bash terminal and then type

	module load singularity/3.6.1

If you will be a frequent user, you should add the singularity module to your bash rc. Next, clone the ldmx-sw repository.

	git clone --recursive https://github.com/LDMX-Software/ldmx-sw.git

Note: the recursive flag is important because there are several necessary parts stored in separate git repositories.

Next, source the ldmx-env.sh script. This will grab the latest docker image and enable you to work inside the container. This may take a few minutes for the first time (and will create a .sif file), but also must be re-run every time a new terminal is opened.

	source ldmx-sw/scripts/ldmx-env.sh

Now you can work inside the container by starting all commands with ldmx. Next, build ldmx-sw.

	cd ldmx-sw; mkdir build; cd build;

	ldmx cmake ..

	ldmx make install

You will have to re-build every time a change is made to ldmx-sw. Now you can run with the ldmx fire command where ldmx operates inside the container and fire is the ldmx-sw specific command that executes the python configuration files. Try one of the examples on the LDMX wiki to see if it works.ldmx-analysis

Sometimes, you may want to make changes to the LDMX software or simply perform analysis without changing the core code in ldmx-sw. For this, it is recommended that you use ldmx-analysis. This also enables a faster build if these changes can be made within ldmx-analysis. ldmx-analysis is intended to be built and run alongside ldmx-sw.

You first need to get access to the ldmx-analysis repository. For access, email Omar Moreno at SLAC with your Github account info. Then, clone the repository.

	git clone --recursive https://github.com/LDMX-Software/ldmx-analysis.git

Note: the recursive flag is important because there are several necessary parts stored in separate git repositories.

Before building ldmx-analysis, ldmx-sw needs to be built following the instructions above. Build ldmx-analysis inside the container.

	cd ldmx-analysis; mkdir build; cd build;

	ldmx cmake ..

	ldmx make install

Note: the cmake flags reflect the current CMakeLists.txt files and may change in the future.

You can run ldmx-analysis in the same way as running ldmx-sw with the ldmx fire command followed by a python configuration script. Try one of the ldmx-analysis examples in the config directory.
