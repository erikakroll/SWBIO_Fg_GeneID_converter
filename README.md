*Fusarium graminearum* PH-1 gene ID converter 
==============

This is a python script which can convert gene IDs from and between the *F. graminearium* PH-1 assemblies v. 3.2 (Wong et al., 2011; Güldener et al., 2006), v. 4 (King et al., 2015) and v 5 (King et al., 2017). In the output and script these assemblies are referred to as MIPS v. 3.2, RRES v. 4 and RRES v. 4 repectively. This is in reference to the institutes that created/developed the assemblies ie. the Munich Information Services for Protein Sequences (MIPS) and Rothamsted Research (RRES).

To run:

1. Download Fg_geneID_converter.py
2. Run in terminal as python Fg_geneID converter.py
3. Enter one or multiple gene IDs from assemblies v. 3.2, v. 4 and v. 5 
4. Multiple gene IDs should be comma seperated

**NOTE - IDs need to be entered in the following formats:**

- v 3.2 IDs as FGSG_xxxxx
- v 4.0 IDs as FFGRES_xxxxx
- v 5.0 IDs as FgramPH1_xxtxxxx

5. The gene IDs from the two other assemblies should then be printed adjacent to the initial entry
6. The assembly to which the ID belongs to is printed before both the input and output IDs


Additional Analysis
--------------

The dictionaries in this script were created using the python script assemblyIDs_to_dict.py

This script can be modified to read a CSV file containing IDs for the key in the top row (row 0)
and IDs for the value in the row below (row 1). For example view 'MIPS_to_RRESv4.csv'

References 
--------------

Güldener, U., Mannhaupt, G., Münsterkötter, M., Haase, D., Oesterheld, M., Stümpflen, V., Mewes, H.W. and Adam, G., 2006. FGDB: a comprehensive fungal genome resource on the plant pathogen Fusarium graminearum. Nucleic acids research, 34(suppl_1), pp.D456-D458.

King, R., Urban, M., Hammond-Kosack, M.C., Hassani-Pak, K. and Hammond-Kosack, K.E., 2015. The completed genome sequence of the pathogenic ascomycete fungus Fusarium graminearum. BMC genomics, 16(1), p.544.

King, R., Urban, M. and Hammond-Kosack, K.E., 2017. Annotation of Fusarium graminearum (PH-1) version 5.0. Genome announcements, 5(2).

Wong, P., Walter, M., Lee, W., Mannhaupt, G., Münsterkötter, M., Mewes, H.W., Adam, G. and Güldener, U., 2010. FGDB: revisiting the genome annotation of the plant pathogen Fusarium graminearum. Nucleic acids research, 39(suppl_1), pp.D637-D639.