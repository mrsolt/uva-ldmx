# This allows matplotlib plots to be shown inline
#%matplotlib inline

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#plt.rcParams["text.latex.preamble"].join([
#        r"\usepackage{dashbox}",
#        r"\setmainfont{xcolor}",
#])
#plt.rcParams['text.latex.preamble'] = [
#       r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
#       r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
#       r'\usepackage{helvet}',    # set the normal font here
#       r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
#       r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
#]
#plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['text.usetex'] = False
import math

# Set the hatching style used for the plots
hatching = '\\\\\\\\\\\\'

matplotlib.rcParams['axes.facecolor'] = 'white'
#plt.rc('text', usetex=True)

## Container for all current results and projections
current_results = []

##
##  HPS Results
##

# HPS 2015 engineering run reach - 0.5 mm data only
## -- Bump hunt
engrun2015 = np.genfromtxt('contours/engineering_run2015_reach.csv',
                           dtype=[('mass',    'f8'), # GeV
                                  ('epsilon', 'f8')], # epsilon^2
                           delimiter=',')
current_results.append(engrun2015)

# HPS 2015 engineering run reach with bug fix
## -- Bump hunt
engrun2015fix = np.genfromtxt('contours/engineering_run2015_fix.csv',
                           dtype=[('mass',    'f8'), # MeV
                                  ('epsilon', 'f8')], # epsilon^2
                           delimiter=',')
#current_results.append(engrun2015fix)

# HPS 2016 engineering run reach
## -- Bump hunt
engrun2016 = np.genfromtxt('contours/engineering_run2016_reach.csv',
                           dtype=[('mass',    'f8'), # MeV
                                  ('epsilon2', 'f8')], # epsilon^2
                           delimiter=',')
current_results.append(engrun2016)

##
## HPS Projections
##

#
# Bump hunt projections
#

# HPS 1.1 GeV, 4 weeks bump hunt projection - positron trigger + L0 upgrades
hps_1pt1_bh_proj_pos_l0 = np.genfromtxt('contours/hps_1pt1_4weeks_bh_proj_pos_trig_l0.csv',
                                 dtype=[('mass', 'f8'),
                                        ('eps', 'f8')],
                                 delimiter=',')

# HPS 2.2 GeV, 4 weeks bump hunt projection - positron trigger + L0 upgrades
hps_2pt2_bh_proj_pos_l0 = np.genfromtxt('contours/hps_2pt2_4weeks_bh_proj_pos_trig_l0.csv',
                                 dtype=[('mass', 'f8'),
                                        ('eps', 'f8')],
                                 delimiter=',')


# HPS 4.4 GeV, 4 weeks bump hunt projection - positron trigger + L0 upgrades
hps_4pt4_bh_proj_pos_l0 = np.genfromtxt('contours/hps_4pt4_4weeks_bh_proj_pos_trig_l0.csv',
                                 dtype=[('mass', 'f8'),
                                        ('eps', 'f8')],
                                 delimiter=',')

# HPS 1.1 GeV, 4 weeks bump hunt projection - positron trigger
hps_1pt1_bh_proj_pos = np.genfromtxt('contours/hps_1pt1_4weeks_bh_proj_pos_trig.csv',
                                 dtype=[('mass', 'f8'),
                                        ('eps', 'f8')],
                                 delimiter=',')

# HPS 2.2 GeV, 4 weeks bump hunt projection - positron trigger
hps_2pt2_bh_proj_pos = np.genfromtxt('contours/hps_2pt2_4weeks_bh_proj_pos_trig.csv',
                                 dtype=[('mass', 'f8'),
                                        ('eps', 'f8')],
                                 delimiter=',')


# HPS 4.4 GeV, 4 weeks bump hunt projection - positron trigger
hps_4pt4_bh_proj_pos = np.genfromtxt('contours/hps_4pt4_4weeks_bh_proj_pos_trig.csv',
                                 dtype=[('mass', 'f8'),
                                        ('eps', 'f8')],
                                 delimiter=',')

# HPS 1.1 GeV, 4 weeks bump hunt projection - Nominal
hps_1pt1_bh_proj_nominal = np.genfromtxt('contours/hps_1pt1_4weeks_bh_proj_nominal.csv',
                                 dtype=[('mass', 'f8'),
                                        ('eps', 'f8')],
                                 delimiter=',')

# HPS 2.2 GeV, 4 weeks bump hunt projection - Nominal
hps_2pt2_bh_proj_nominal = np.genfromtxt('contours/hps_2pt2_4weeks_bh_proj_nominal.csv',
                                 dtype=[('mass', 'f8'),
                                        ('eps', 'f8')],
                                 delimiter=',')


# HPS 4.4 GeV, 4 weeks bump hunt projection - Nominal
hps_4pt4_bh_proj_nominal = np.genfromtxt('contours/hps_4pt4_4weeks_bh_proj_nominal.csv',
                                 dtype=[('mass', 'f8'),
                                        ('eps', 'f8')],
                                 delimiter=',')

# 2019 Physics Run vertex projection
phys2019_vertex_proj_low = np.genfromtxt('contours/hps_physics_run2019_vertex_proj.csv',
                                     dtype=[('mass', 'f8'),
                                            ('eps2', 'f8')],
                                     delimiter=',')

phys2019plus2021_vertex_proj_low = np.genfromtxt('contours/hps_physics_run2019plus2021_vertex_proj.csv',
                                     dtype=[('mass', 'f8'),
                                            ('eps2', 'f8')],
                                     delimiter=',')

# Full luminosity reach
hps_full_lumi = np.genfromtxt('contours/hps_full_lumi.csv', dtype = [('mass', 'f8'), ('eps2', 'f8')], delimiter=',')

ldmx_phase1 = np.genfromtxt('output_4e+14eot_4gev_50-500cm_9bkg_50eff.csv', dtype = [('mass', 'f8'), ('eps2', 'f8')], delimiter=',')
ldmx_phase2 = np.genfromtxt('output_1e+16eot_8gev_50-500cm_9bkg_50eff.csv', dtype = [('mass', 'f8'), ('eps2', 'f8')], delimiter=',')

#
# Vertex projections
#

# HPS 1.1 GeV, 4 weeks vertex projection - positron trigger + L0 upgrades
hps_1pt1_vtx_proj_pos_l0 = np.genfromtxt('contours/hps_1pt1_4weeks_vtx_proj_pos_trig_l0.csv',
                                  dtype=[('mass', 'f8'),
                                         ('eps', 'f8')],
                                  delimiter=',')

# HPS 2.2 GeV, 4 weeks vertex projection - positron trigger + L0 upgrades
hps_2pt2_vtx_proj_pos_l0 = np.genfromtxt('contours/hps_2pt2_4weeks_vtx_proj_pos_trig_l0.csv',
                                  dtype=[('mass', 'f8'),
                                         ('eps', 'f8')],
                                  delimiter=',')


# HPS 4.4 GeV, 4 weeks vertex projection - positron trigger + L0 upgrades
hps_4pt4_vtx_proj_pos_l0 = np.genfromtxt('contours/hps_4pt4_4weeks_vtx_proj_pos_trig_l0.csv',
                                  dtype=[('mass', 'f8'),
                                         ('eps', 'f8')],
                                  delimiter=',')

# HPS 2.2 GeV, 4 weeks vertex projection - positron trigger
hps_2pt2_vtx_proj_pos = np.genfromtxt('contours/hps_2pt2_4weeks_vtx_proj_pos_trig.csv',
                                  dtype=[('mass', 'f8'),
                                         ('eps', 'f8')],
                                  delimiter=',')


# HPS 4.4 GeV, 4 weeks vertex projection - positron trigger
hps_4pt4_vtx_proj_pos = np.genfromtxt('contours/hps_4pt4_4weeks_vtx_proj_pos_trig.csv',
                                  dtype=[('mass', 'f8'),
                                         ('eps', 'f8')],
                                  delimiter=',')


# HPS 1.1, 2.2 and 4.4 GeV vertex reach from proposal
hps_2014_vertex = np.genfromtxt('contours/hps_2014_prop_vertex_proj.csv',
                              dtype=[('mass', 'f8'),
                                     ('eps', 'f8')],
                              delimiter=',')

##
## Results from other experiments
##

#
# BaBar
#
babar = np.genfromtxt('contours/babar.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')
current_results.append(babar)

#
# NA48/2
#
na48 = np.genfromtxt('contours/2015_na482_rescaled_to_95cl.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')
current_results.append(na48)

#
# APEX
#

#--- APEX projections
apex_proj = np.genfromtxt('contours/apex_proj.csv',
                          dtype=[('mass', 'f8'),
                                 ('eps', 'f8')],
                          delimiter=',')

#--- APEX proposal projections
apex_proj_pac37 = np.genfromtxt('contours/apex_proj_pac37.csv',
                                dtype=[('mass', 'f8'),
                                       ('eps', 'f8')],
                                delimiter=',')


#--- Test run
apex_test = np.genfromtxt('contours/apex_test_run.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')
current_results.append(apex_test)

#--- Projection for 2019 physics run
apex2019 = np.genfromtxt('contours/apex_2019_physics_run.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')

#
# 2014 KLOE
#
kloe2014 = np.genfromtxt('contours/2014_kloe.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')
current_results.append(kloe2014)

#
# KLOE
#
kloe = np.genfromtxt('contours/kloe.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')
current_results.append(kloe)


#
# HADES
#
hades = np.genfromtxt('contours/hades.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')
current_results.append(hades)


#
# MAINZ
#
mainz = np.genfromtxt('contours/2014_mainz.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')
current_results.append(mainz)


#
# PHENIX
#
phenix = np.genfromtxt('contours/2014_phenix.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')
current_results.append(phenix)


#
# Constraints from muon g-2
#
amu_2sigma_high = np.genfromtxt('contours/amu_2sigma_high.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')

amu_2sigma_low = np.genfromtxt('contours/amu_2sigma_low.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')

#
# Constraints from electron g-2
#
ae_3sigma = np.genfromtxt('contours/ae_3sigma.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')

#
# U70
#
u70_proj = np.genfromtxt('contours/u70_proj_2sigma.csv',
                     dtype=[('eps', 'f8'),
                            ('mass', 'f8')],
                     delimiter=',')
current_results.append(u70_proj)

u70 = np.genfromtxt('contours/u70_serpuhov.csv',
                     dtype=[('eps', 'f8'),
                            ('mass', 'f8')],
                     delimiter=',')
current_results.append(u70)


#
# e774
#
e774 = np.genfromtxt('contours/e774_andreas_log.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',',)
current_results.append(e774)

#
# e137
#
e137 = np.genfromtxt('contours/e137_andreas_log.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')
current_results.append(e137)

#
# e141
#
e141 = np.genfromtxt('contours/e141_andreas_log.csv',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')
current_results.append(e141)

#
# Orsay
#
orsay = np.genfromtxt('contours/orsay_andreas_95pct.dat',
                     dtype=[('mass', 'f8'),
                            ('eps', 'f8')],
                     delimiter=',')
current_results.append(orsay)

#
# DarkLight
#
dark_light_proj = np.genfromtxt('contours/dark_light.csv',
                                dtype=[('mass', 'f8'),
                                ('eps', 'f8')],
                                delimiter=',')


#
# NA64
#

#--- 2018
na64_2018 = np.genfromtxt('contours/na64_2018.csv',
                                dtype=[('mass', 'f8'),
                                       ('eps', 'f8')],
                                delimiter=',')
current_results.append(na64_2018)

#--- 2019
na64_2019 = np.genfromtxt('contours/na64_2019.csv',
                                dtype=[('mass', 'f8'),
                                       ('eps', 'f8')],
                                delimiter=',')
current_results.append(na64_2019)

#
# KEK
#
kek_andreas = np.genfromtxt('contours/kek.csv',
                                dtype=[('mass', 'f8'),
                                       ('eps', 'f8')],
                                delimiter=',')
current_results.append(kek_andreas)

#
# LHCb
#

# 2017 LHCb
lhcb_prompt = np.genfromtxt('contours/lhcb_2017_results_prompt_data.csv',
                            dtype=[('mass', 'f8'), # MeV
                                    ('eps', 'f8')], # epsilon^2
                            delimiter=',')
current_results.append(lhcb_prompt)

# 2019 LHCb
lhcb_prompt_2019 = np.genfromtxt('contours/lhcb_2019_results_prompt_data.csv',
                            dtype=[('mass', 'f8'), # MeV
                                    ('eps', 'f8')], # epsilon^2
                            delimiter=',')
current_results.append(lhcb_prompt_2019)

# 2019 LHCb
lhcb_ll_00_2019 = np.genfromtxt('contours/lhcb_2019_results_ll_00.csv',
                            dtype=[('mass', 'f8'), # MeV
                                    ('eps', 'f8')], # epsilon^2
                            delimiter=',')
current_results.append(lhcb_ll_00_2019)

# 2019 LHCb
lhcb_ll_01_2019 = np.genfromtxt('contours/lhcb_2019_results_ll_01.csv',
                            dtype=[('mass', 'f8'), # MeV
                                    ('eps', 'f8')], # epsilon^2
                            delimiter=',')
current_results.append(lhcb_ll_01_2019)

#
# Thermal targets
#

# Thermal targets upper
t_target_upper = np.genfromtxt('contours/thermal_targets_upper.csv',
                               dtype=[('mass', 'f8'), # MeV
                                      ('eps',  'f8')],
                               delimiter=',')

# Thermal targets upper
t_target_lower = np.genfromtxt('contours/thermal_targets_lower.csv',
                               dtype=[('mass', 'f8'), # MeV
                                      ('eps',  'f8')],
                               delimiter=',')

def setup_fig_style(ax):
    plt.xticks(fontsize = 30)
    plt.yticks(fontsize = 30)

    ax.set_xlabel("$A'$ Mass (GeV)", fontsize=30)
    ax.set_ylabel('$\epsilon^2$', fontsize=35)
    ax.set_ylim(0.00000000002, 0.0001)
    ax.set_xlim(0.002, 1.5)
    ax.tick_params(axis = 'both', which = 'both', length = 15)
    ax.set_title('$\\bf{HPS}$ $\\bf{Simulation}$ $\\bf{Preliminary}$', x=.7, y=.01, fontsize=20)

    ax.set_yscale('log')
    ax.set_xscale('log')



def draw_existing_limits_color(ax):

    ax.grid(False)

    ax.fill_between(amu_2sigma_low['mass'], amu_2sigma_low['eps']*amu_2sigma_low['eps'],
                    amu_2sigma_high['eps']*amu_2sigma_high['eps'], alpha=0.1, color='green')
    ax.text(0.009, 0.000003, '$a_{\mu \pm 2 \sigma}$', fontsize=30, color='green', fontweight='bold')

    ax.fill_between(ae_3sigma['mass'], ae_3sigma['eps']*ae_3sigma['eps'], 0.001,
                    alpha=0.2, facecolor='deeppink', edgecolor='deeppink', linewidth=2)
    ax.text(0.004, 0.00005, '$a_{e}$', fontsize=30, color='deeppink', fontweight='bold')

    ##
    ## Collider
    ##

    #
    # BaBar
    #
    epsilon_squared = babar['eps']*babar['eps']*math.sqrt(1.64/1.96)*math.sqrt(1.64/1.96)
    ax.fill_between(babar['mass'], epsilon_squared, 0.001,
                    alpha=0.2, facecolor='brown', edgecolor="0.3", linewidth=2)
    ax.text(0.3, 0.000002, 'BaBar', fontsize=15, color='brown', fontweight='bold')

    #
    # LHCb
    #

    # Prompt
    ax.fill_between(lhcb_prompt['mass']/1000, lhcb_prompt['eps'], 0.001,
                    alpha=0.2, facecolor='green', edgecolor='green', linewidth=2)
    ax.text(0.27, 0.000001, 'LHCb', fontsize=15, color='green', fontweight='bold')

    ax.fill_between(lhcb_prompt_2019['mass'], lhcb_prompt_2019['eps']*math.sqrt(1.96/1.64), 0.001,
                    alpha=0.2, facecolor='steelblue', edgecolor='steelblue', linewidth=2)
    ax.text(0.27, 0.0000003, 'LHCb', fontsize=15, color='steelblue', fontweight='bold')

    # Long lived
    ax.fill(lhcb_ll_00_2019['mass']/1000, lhcb_ll_00_2019['eps']*math.sqrt(1.96/1.64),
                   alpha=0.2, facecolor='steelblue', edgecolor='steelblue', linewidth=2)
    ax.fill(lhcb_ll_01_2019['mass']/1000, lhcb_ll_01_2019['eps']*math.sqrt(1.96/1.64),
                   alpha=0.2, facecolor='steelblue', edgecolor='steelblue', linewidth=2)
    ax.text(0.27, 1e-9, 'LHCb', fontsize=15, color='steelblue', fontweight='bold')

    ##
    ## p+ fixed target
    ##

    #
    # NA48/2
    #
    epsilon_squared = na48['eps']*na48['eps']*math.sqrt(1.64/1.96)*math.sqrt(1.64/1.96)
    ax.fill_between(na48['mass'], epsilon_squared, 0.001,
                    alpha=0.2, facecolor='teal', edgecolor='teal', linewidth=2)
    ax.text(0.02, 0.000001, 'NA48/2', fontsize=15, color='teal', fontweight='bold')

    ##
    ## e- fixed target
    ##

    #
    # HPS
    #

    ## 2015
    ax.fill_between(engrun2015['mass'], engrun2015['epsilon'], 0.001,
                    alpha=0.2, facecolor='blue', edgecolor='blue', linewidth=2)
    ax.text(0.028, 0.00003, 'HPS 2015', fontsize=15, color='blue', fontweight='bold')

    #
    # APEX Test
    #
    ax.fill_between(apex_test['mass']/1000, apex_test['eps']*math.sqrt(1.64/1.96), 0.001,
                    alpha=0.2, facecolor='purple', edgecolor='purple', hatch=hatching, linewidth=2)
    ax.text(0.15, 0.000004, '  APEX\nTest Run', fontsize=15, color='purple', fontweight='bold')

    #
    # KLOE
    #

    #### 2014
    ax.fill_between(kloe2014['mass']/1000, kloe2014['eps'], 0.001,
                    alpha=0.2, facecolor='orange', edgecolor='orange', linewidth=2)
    ax.text(0.6, 0.00004, 'KLOE', fontsize=15, color='orange', fontweight='bold')

    ####
    ax.fill_between(kloe['mass']/1000, kloe['eps'], 0.001,
                    alpha=0.2, facecolor='yellow', edgecolor='yellow', linewidth=2)
    ax.text(0.012, 0.00005, 'KLOE', fontsize=15, color='yellow', fontweight='bold')

    #
    # HADES
    #
    ax.fill_between(hades['mass'], hades['eps'], 0.001,
                    alpha=0.2, facecolor='dodgerblue', edgecolor='dodgerblue', linewidth=2)
    ax.text(0.06, 0.000006, 'HADES', fontsize=15, color='dodgerblue', fontweight='bold')

    #
    # PHENIX
    #
    ax.fill_between(phenix['mass']/1000, phenix['eps'], 0.001,
                    alpha=0.2, facecolor='gold', edgecolor='gold', linewidth=2)
    ax.text(0.05, 0.000004, 'PHENIX', fontsize=15, color='gold', fontweight='bold')

    #
    # Mainz
    #
    ax.fill_between(mainz['mass'], mainz['eps'], 0.001,
                    alpha=0.2, facecolor='indigo', edgecolor='indigo', linewidth=2)
    ax.text(0.1, 0.000002, 'Mainz', fontsize=15, color='indigo', fontweight='bold')

    ##
    ## Beam Dump
    ##

    #
    # NA64
    #
    ax.fill_between(na64_2019['mass'], na64_2019['eps']*na64_2019['eps'], 0.001,
                    alpha=0.2, facecolor='royalblue', edgecolor="royalblue", linewidth=2)
    ax.text(0.015, 0.00000005, 'NA64', fontsize=15, color='royalblue', fontweight='bold')

    #
    # U70
    #
    ax.fill_between(u70_proj['mass'], u70_proj['eps']*u70_proj['eps'], 0.001,
                    alpha=0.2, facecolor='0.3', edgecolor="0.3", linewidth=2)

    #
    # E774
    #
    epsilon_squared = np.power(10, e774['eps'])*np.power(10, e774['eps'])
    ax.fill_between(np.power(10, e774['mass']), epsilon_squared, 0.001,
                    alpha=0.2, facecolor='0.3', edgecolor="0.3", linewidth=2)
    ax.text(0.0045, 0.000001, 'E774', fontsize=15, color='0.3', fontweight='bold')

    #
    # E137
    #
    epsilon_squared = np.power(10, e137['eps'])*np.power(10, e137['eps'])
    ax.fill_between(np.power(10, e137['mass']), epsilon_squared, 0.001,
                    alpha=0.2, facecolor='0.3', edgecolor="0.3", linewidth=2)

    #
    # E141
    #
    epsilon_squared = np.power(10, e141['eps'])*np.power(10, e141['eps'])
    ax.fill_between(np.power(10, e141['mass']), epsilon_squared, 0.001,
                    alpha=0.2, facecolor='0.3', edgecolor="0.3", linewidth=2)
    ax.text(2.5e-3, 1e-8, 'E141', fontsize=15, color='0.3', fontweight='bold')

    #
    # Orsay
    #
    epsilon_squared = np.power(10, orsay['eps'])*np.power(10, orsay['eps'])
    ax.fill_between(np.power(10, orsay['mass']), epsilon_squared, 0.001,
                alpha=0.2, facecolor='0.3', edgecolor="0.3", linewidth=2)

    #
    # KEK
    #
    ax.fill_between(kek_andreas['mass'], kek_andreas['eps']*kek_andreas['eps'], 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", linewidth=2)
    ax.text(3e-3, 4e-11, 'Orsay/E137/CHARM/U70', fontsize=15, color='0.3', fontweight='bold')

def draw_existing_limits_grayscale(ax):

    ax.fill_between(amu_2sigma_low['mass'], amu_2sigma_low['eps']*amu_2sigma_low['eps'],
                amu_2sigma_high['eps']*amu_2sigma_high['eps'], alpha=0.1, color='green')

    ax.fill_between(ae_3sigma['mass'], ae_3sigma['eps']*ae_3sigma['eps'], 0.001,
                alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)

    # BaBar
    epsilon_squared = babar['eps']*babar['eps']*math.sqrt(1.64/1.96)*math.sqrt(1.64/1.96)
    ax.fill_between(babar['mass'], epsilon_squared, 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)

    # NA48/2
    epsilon_squared = na48['eps']*na48['eps']*math.sqrt(1.64/1.96)*math.sqrt(1.64/1.96)
    ax.fill_between(na48['mass'], epsilon_squared, 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)

    # APEX Test
    ax.fill_between(apex_test['mass']/1000, apex_test['eps']*math.sqrt(1.64/1.96), 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)

    ax.fill_between(kloe2014['mass']/1000, kloe2014['eps'], 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)
    #ax.text(0.6, 0.00004, 'KLOE', fontsize=15, color='0.3', fontweight='bold')

    ax.fill_between(kloe['mass']/1000, kloe['eps'], 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)

    ax.fill_between(hades['mass'], hades['eps'], 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3",hatch=hatching, linewidth=2)

    ax.fill_between(phenix['mass']/1000, phenix['eps'], 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)

    ax.fill_between(mainz['mass'], mainz['eps'], 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)

    ax.fill_between(u70_proj['mass'], u70_proj['eps']*u70_proj['eps'], 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)

    epsilon_squared = np.power(10, e774['eps'])*np.power(10, e774['eps'])
    ax.fill_between(np.power(10, e774['mass']), epsilon_squared, 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)


    epsilon_squared = np.power(10, e137['eps'])*np.power(10, e137['eps'])
    ax.fill_between(np.power(10, e137['mass']), epsilon_squared, 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)

    epsilon_squared = np.power(10, e141['eps'])*np.power(10, e141['eps'])
    ax.fill_between(np.power(10, e141['mass']), epsilon_squared, 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)


    ax.fill_between(na64_2019['mass'], na64_2019['eps']*na64_2019['eps'], 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)

    epsilon_squared = np.power(10, orsay['eps'])*np.power(10, orsay['eps'])
    ax.fill_between(np.power(10, orsay['mass']), epsilon_squared, 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)


    ax.fill_between(kek_andreas['mass'], kek_andreas['eps']*kek_andreas['eps'], 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)

    ax.fill_between(lhcb_prompt['mass']/1000, lhcb_prompt['eps'], 0.001,
                    alpha=0.2, facecolor='none', edgecolor="0.3", hatch=hatching, linewidth=2)

    ax.fill_between(lhcb_prompt_2019['mass'], lhcb_prompt_2019['eps']*math.sqrt(1.96/1.64), 0.001,
                    alpha=0.2, facecolor='none', edgecolor='0.3', hatch=hatching, linewidth=2)
    ax.text(0.27, 0.0000003, 'LHCb', fontsize=15, color='0.3', fontweight='bold')

    # Long lived
    ax.fill(lhcb_ll_00_2019['mass']/1000, lhcb_ll_00_2019['eps']*math.sqrt(1.96/1.64),
                   alpha=0.2, facecolor='none', edgecolor='0.3', hatch=hatching, linewidth=2)
    ax.fill(lhcb_ll_01_2019['mass']/1000, lhcb_ll_01_2019['eps']*math.sqrt(1.96/1.64),
                   alpha=0.2, facecolor='none', edgecolor='0.3', hatch=hatching, linewidth=2)
    ax.text(0.27, 1e-9, 'LHCb', fontsize=15, color='0.3', fontweight='bold')

    ax.fill_between(engrun2015['mass'], engrun2015['epsilon'], 0.001,
                    alpha=0.2, facecolor='none', edgecolor='0.3', hatch=hatching, linewidth=2)


    ax.text(0.009, 0.000003, '$a_{\mu \pm 2 \sigma}$', fontsize=30, color='green', fontweight='bold')
    ax.text(0.004, 0.00005, '$a_{e}$', fontsize=30, color='0.3', fontweight='bold')
    ax.text(0.3, 0.000002, 'BaBar', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.02, 0.000001, 'NA48/2', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.1, 0.00004, 'KLOE', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.06, 0.000006, 'HADES', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.15, 0.000004, '  APEX\nTest Run', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.05, 0.000004, 'PHENIX', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.09, 0.000003, 'Mainz', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.003, 0.00000003, 'U70', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.0045, 0.000001, 'E774', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.0022, 0.000000015, 'E137', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.004, 0.0000001, 'E141', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.015, 0.00000005, 'NA64', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.0022, 0.0000001, 'Orsay', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.0022, 0.00000004, 'KEK', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.27, 0.000001, 'LHCb', fontsize=15, color='0.3', fontweight='bold')
    ax.text(0.028, 0.00003, 'HPS 2015', fontsize=15, color='0.3', fontweight='bold')


#fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 12))
#setup_fig_style(ax)

#ax.text(0.035, 0.00000002, 'LDMX Phase II', fontsize=20, color='#6d904f');

#draw_existing_limits_grayscale(ax);
#ax.set_title("");

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 12))
setup_fig_style(ax)

##
## Thermal targets
##
ax.fill_between(t_target_upper['mass'], t_target_upper['eps'], 1e-12,
                alpha=0.2, facecolor='red', edgecolor='red', linewidth=2)
ax.fill_between(t_target_lower['mass'], t_target_lower['eps'], 1e-12,
                alpha=0.9, facecolor='white', edgecolor='red', linewidth=2)
ax.plot(t_target_upper['mass'], t_target_upper['eps'], linewidth=2, color='red')
ax.text(2.1e-2, 2.5e-11, r"Thermal targets: $\alpha_D = 0.5, M_{A'}/M_{\chi} = 1.5$", color='red',
        rotation=40, fontsize=12)

ax.plot(ldmx_phase1['mass'], ldmx_phase1['eps2'],
        marker='None', linestyle='-', color='#e5ae38', lw=4)
ax.text(0.003, 0.0000000005, 'LDMX Phase I', fontsize=20, color='#e5ae38');

ax.plot(ldmx_phase2['mass'], ldmx_phase2['eps2'],
        marker='None', linestyle='-', color='#6d904f', lw=4)
ax.text(0.003, 0.0000000001, 'LDMX Phase II', fontsize=20, color='#6d904f');

draw_existing_limits_color(ax)
ax.set_title("");
#fig.savefig('final_coupling_upper_limits.pdf', facecolor='white')
fig.savefig('test.pdf', facecolor='white')

plt.show()
