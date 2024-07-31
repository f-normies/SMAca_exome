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
 "avg_cov_EMC1|"  \
 "avg_cov_STK16|"  \
 "avg_cov_APEX1|"  \
 "avg_cov_ZFYVE19|"  \
 "avg_cov_USP7|"  \
 "avg_cov_SIRT2|"  

POSITIONS = {
    REF_HG19: {
        "SMN": {
            "SMN1": [5, 70220767, 70249769],
            "SMN2": [5, 69345349, 69374349]
        },
        # NOT IMPLEMENTED, PLACEHOLDER
        "GENES": {
            'GNB1': ['1', 1890819, 1891117],
            'THAP3': ['1', 6634019, 6635700],
            'IRF2BP2': ['1', 234608446, 234610178],
            'SLF2': ['10', 100912962, 100913886],
            'MAPKAPK5': ['12', 111892966, 111902222],
            'PAGR1': ['16', 29819416, 29822489],
            'RPS2P44': ['16', 48577523, 48578369],
            'MBTPS1': ['16', 84116734, 84116942],
            'BRK1': ['3', 10126268, 10127190],
            'DIPK2A': ['3', 143989509, 143992368],
            'SAR1B': ['5', 134648115, 134649271],
            'GTF2H4': ['6', 30913810, 30915037],
            'GPANK1': ['6', 31665860, 31666283],
            'RARS2': ['6', 87589700, 87590028],
            'ASH2L': ['8', 38138963, 38140080]
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
                'EMC1': ['1', 19239230, 19239985],
                'STK16': ['2', 219247414, 219248191],
                'APEX1': ['14', 20455190, 20456101],
                'ZFYVE19': ['15', 40807085, 40807868],
                'USP7': ['16', 8899306, 8900131],
                'SIRT2': ['19', 38893413, 38894410]
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
