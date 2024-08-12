# coding: utf-8
"""
author: Daniel López
email: daniel.lopez.lopez@juntadeandalucia.es

author: Carlos Loucera
email: carlos.loucera@juntadeandalucia.es

SMA carrier Test samtools constants file. Genomic ranges are 0-based, stop-excluded
"""

REF_HG19 = "hg19"
REF_HG38 = "hg38"

HEADER_FILE = \
 "id|" \
 "Pi_a|" \
 "Pi_b_exon7|" \
 "Pi_c|" \
 "cov_SMN1_a|" \
 "cov_SMN1_b|" \
 "cov_SMN1_c|" \
 "cov_SMN2_a|" \
 "cov_SMN2_b|" \
 "cov_SMN2_c|" \
 "avg_cov_SMN1|" \
 "avg_cov_SMN2|" \
 "scale_factor|" \
 "std_control|" \
 "g.27134T>G|" \
 "g.27706_27707delAT|" \
 "avg_cov_ENSE00001753715|"  \
 "avg_cov_ENSE00003475744_ENSE00003668148|"  \
 "avg_cov_ENSE00000772493_ENSE00001941691|"  \
 "avg_cov_ENSE00002439297_ENSE00002496679_ENSE00003480889_ENSE00003539428|"  \
 "avg_cov_ENSE00000876091|"  \
 "avg_cov_ENSE00003519976_ENSE00003611519|"  \
 "avg_cov_ENSE00001131925|"  \
 "avg_cov_ENSE00003472458_ENSE00003679784|"  \
 "avg_cov_ENSE00003714360_ENSE00004030467|"  \
 "avg_cov_ENSE00003550230_ENSE00003565984|"  \
 "avg_cov_ENSE00002163457_ENSE00003599335_ENSE00003611132|"  \
 "avg_cov_ENSE00003523331_ENSE00003683955|"  \
 "avg_cov_ENSE00000656821|"  \
 "avg_cov_ENSE00001147300|"  \
 "avg_cov_ENSE00000675982_ENSE00000675985_ENSE00002624378|"  \
 "avg_cov_ENSE00002626237_ENSE00003537347_ENSE00003632529|"  \
 "avg_cov_ENSE00003751713"

POSITIONS = {
    REF_HG19: {
        "SMN": {
            "SMN1": [5, 70220767, 70249769],
            "SMN2": [5, 69345349, 69374349]
        },
        # NOT IMPLEMENTED, PLACEHOLDER
        "GENES": {
            'ENSE00001753715': [1, 147042951, 147043064],
            'ENSE00003475744,ENSE00003668148': [2, 24673365, 24673463],
            'ENSE00000772493,ENSE00001941691': [2, 102702405, 102702502],
            'ENSE00002439297,ENSE00002496679,ENSE00003480889,ENSE00003539428': [2, 110567963, 110568075],
            'ENSE00000876091': [2, 218488303, 218488421],
            'ENSE00003519976,ENSE00003611519': [5, 80728850, 80728965],
            'ENSE00001131925': [5, 118928536, 118928729],
            'ENSE00003472458,ENSE00003679784': [7, 27785398, 27785489],
            'ENSE00003714360,ENSE00004030467': [7, 75202541, 75202613],
            'ENSE00003550230,ENSE00003565984': [7, 92031511, 92031604],
            'ENSE00002163457,ENSE00003599335,ENSE00003611132': [11, 46669403, 46669532],
            'ENSE00003523331,ENSE00003683955': [12, 110205594, 110205680],
            'ENSE00000656821': [14, 50153069, 50153173],
            'ENSE00001147300': [15, 43347015, 43347096],
            'ENSE00000675982,ENSE00000675985,ENSE00002624378': [16, 19545816, 19546534],
            'ENSE00002626237,ENSE00003537347,ENSE00003632529': [16, 84762988, 84763088],
            'ENSE00003751713': [17, 38306532, 38306631]
        },
        "SMN1_POS": {
            "SMN1_a": [5, 70247723, 70247724],
            "SMN1_b_e7": [5, 70247772, 70247773],
            "SMN1_c": [5, 70247920, 70247921]
        },
        "SMN2_POS": {
            "SMN2_a": [5, 69372303, 69372304],
            "SMN2_b_e7": [5, 69372352, 69372353],
            "SMN2_c": [5, 69372500, 69372501]
        },
        "DUP_MARK": {
            "g.27134T>G": [5, 70247900, 70247901],
            "g.27706_27707delAT": [5, 70248472, 70248474]
        }
    },
    REF_HG38: {
        "SMN": {
            "SMN1": [5, 70924940, 70953942],
            "SMN2": [5, 70049523, 70078522]
        },
        "GENES": {
            'ENSE00001753715': [1, 147042951, 147043064],
            'ENSE00003475744,ENSE00003668148': [2, 24673365, 24673463],
            'ENSE00000772493,ENSE00001941691': [2, 102702405, 102702502],
            'ENSE00002439297,ENSE00002496679,ENSE00003480889,ENSE00003539428': [2, 110567963, 110568075],
            'ENSE00000876091': [2, 218488303, 218488421],
            'ENSE00003519976,ENSE00003611519': [5, 80728850, 80728965],
            'ENSE00001131925': [5, 118928536, 118928729],
            'ENSE00003472458,ENSE00003679784': [7, 27785398, 27785489],
            'ENSE00003714360,ENSE00004030467': [7, 75202541, 75202613],
            'ENSE00003550230,ENSE00003565984': [7, 92031511, 92031604],
            'ENSE00002163457,ENSE00003599335,ENSE00003611132': [11, 46669403, 46669532],
            'ENSE00003523331,ENSE00003683955': [12, 110205594, 110205680],
            'ENSE00000656821': [14, 50153069, 50153173],
            'ENSE00001147300': [15, 43347015, 43347096],
            'ENSE00000675982,ENSE00000675985,ENSE00002624378': [16, 19545816, 19546534],
            'ENSE00002626237,ENSE00003537347,ENSE00003632529': [16, 84762988, 84763088],
            'ENSE00003751713': [17, 38306532, 38306631]
        },
        "SMN1_POS": {
            "SMN1_a": [5, 70951895, 70951897],
            "SMN1_b_e7": [5, 70951944, 70951946],
            "SMN1_c": [5, 70952092, 70952094]
        },
        "SMN2_POS": {
            "SMN2_a": [5, 70076475, 70076477],
            "SMN2_b_e7": [5, 70076524, 70076526],
            "SMN2_c": [5, 70076672, 70076674]
        },
        "DUP_MARK": {
            "g.27134T>G": [5, 70952072, 70952074],
            "g.27706_27707delAT": [5, 70952644, 70952647]
        }
    }
}
