:orphan:

Scott Calvin's XAFS Divination Set
==================================

Abstract
--------

This is a set of actual XAFS data gathered especially as a "test set"
for analysis. Why do that? Several reasons are suggested below, under
"Uses."

Details
-------

The set is focused primarily on iron oxides, but also includes metallic
iron and a few iron salts with organic anions. The data was collected on
beamline X-11B of the NSLS, and is of moderate to good quality,
depending on the sample. Multiple scans of each sample are included, and
they are cut off before the cobalt edge. An iron foil was used in the
reference channel.

**Important:** To keep this from being easily solved by linear
combination methods alone, and to simulate the common situation
encountered in XAFS analysis of having a sample that is "almost" like a
mixture of bulk materials, every sample was collected at a random
temperature between 303 and 403 K. That temperature is not reported in
the data set below, in order to simulate the kind of differences between
samples and standards that are not known *a priori*.

Standards
^^^^^^^^^

Standards collected on the same beamline, but not necessarily at the
same temperatures.

`Divination standards (zip file)
<https://docs.xrayabsorption.org/EXAFSAnalysis/EXAFS_Divination_Set/DivStandards.zip>`__

Known Constituents
^^^^^^^^^^^^^^^^^^

In this set, the identity of the constituents are known, but the
fraction of each that is present in the sample is not known (to you,
that is). This is the easiest set to analyze (after the standards), and
is good for beginners to use to test their proficiency and get practice
at the technique.

`Known constituents (zip file)
<https://docs.xrayabsorption.org/EXAFSAnalysis/EXAFS_Divination_Set/DivKnown.zip>`__

Unknown Constituents from a Known List
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this set, 2-3 constituents from the list of standards were mixed in
an unknown (to you) ratio. This is a somewhat more difficult set, but
should be analyzable by any seasoned XAFS researcher.

`Unknown constituents (zip file)
<https://docs.xrayabsorption.org/EXAFSAnalysis/EXAFS_Divination_Set/DivUnknown.zip>`__

Known Constituents and one Mystery Constituent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here the identity of all but one of the constituents are given to
you...but the last constituent is an unknown simple organic compound (a
salt?) involving iron. If I'm a little vague, it's because I haven't
attempted the analysis yet, so only the colleague who ordered the
material and the undergraduate who made the random assignments and
prepared the samples knows what it is. I expect this to be an
interesting challenge for seasoned XAFS researchers. The task is
comparable to that often faced in published analyses.


`Known Constituents and one Mystery Constituent
<https://docs.xrayabsorption.org/EXAFSAnalysis/EXAFS_Divination_Set/DivKnownMyst.zip>`__

Unknown Constituents
^^^^^^^^^^^^^^^^^^^^

This is the tough one. One or two of the constituents is from the list
of standards (but you don't know which ones), and the other is the
mystery constituent from the above set.

`Unknown Constituents
<https://docs.xrayabsorption.org/EXAFSAnalysis/EXAFS_Divination_Set/DivUnknownMyst.zip>`__

Uses
----

I can think of a number of uses for this set.

-  As practice exercises for those learning XAFS analysis
-  As a proficiency test: new research assistants could be asked to
   achieve a certain accuracy with some of these sets before being
   trusted with important analyses
-  For fun. Just once, wouldn't you like a XAFS analysis problem where
   you could check yourself afterward?
-  To compare the accuracy of different techniques, approaches,
   software...
-  For My Nefarious Plan (see below)

My Nefarious Plan
-----------------

My primary purpose for creating this set is to get some baseline figures
on the accuracy of real-life XAFS analysis. There have been attempts in
the literature to estimate this from the bottom up, that is, by
estimating the uncertainty in each step of the analysis. My project is
to try to estimate this from the top down: I'll get actual practitioners
to do an analysis on part (or all) of this set and then report to me
their results. This is then a double-blind study of the accuracy of XAFS
analysis as it is practiced. I plan to then publish the results on
accuracy, creating a publication we can all point to ("In similar
systems, XAFS analysis has been shown to be able to identify the
proportion of phases present with an uncertainty of ##%"). The
publication will contain no identifying information as to who performed
which fits. Participants will be included in the acknowledgments if they
choose.

Getting the Answers
-------------------

To find out the correct answers, and incidentally participate in my
nefarious plan, send an email to "SCalvin at mailaps dot org." Include
the results you have gotten, as much detail as you'd like on how you got
them, what you think your level of expertise is, and about how long you
worked on the problem. I (or my undergraduate, if I have not completed
the analysis myself) will then email back the correct percentages and
phases for the set(s) you've specified. Although the minimum requirement
is phase identification and fraction of each phase, nearest-neighbor
bond lengths and would also be useful, since these samples and standards
were collected at various temperatures.

Example: You could send "I am a graduate student learning EXAFS
analysis. I've found that sample B5 consists of 37 +/- 4 % Fe, 41 +/- 8%
!Fe2O3, and 22 +/-8% alpha FeOOH. The nearest neighbor bond distances in
the , Fe, !Fe2O3, and FeOOH is 2.53 +/- 0.02 angstroms. The
nearest-neighbor distances in the oxidized compounds appeared reasonably
consistent with the crystallographic values, but I could not determine
them individually due to the complications of multiple phases. I used
linear combination of XANES to get the phase percentages and phase
identifications, and then fitted to feff calculations to get the bond
lengths and confirm the XANES results. The software used was Athena and
Artemis. This took about six hours of my life, which I'd like back, but
my Ph. D. adviser says it's good for my soul." I'd then send back the
actual percentages and temperatures.

