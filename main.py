import itertools
from funix import funix
from funix.hint import HTML

lastWords = ""

ReactorType = {
    "Batch (non-baffled flask)": 1, "Batch (baffled flask)": 2,
    "Batch (closed bottle)": 3, "Batch (bioreactor)": 4,
    "Chemostat, CSTR": 5
}

Species = {
    "Actinobacillus succinogenes": 8, "Agrobacterium tumefaciens": 14,
    "Arthrobacter sp.": 15, "Azotobacter vinelandii": 16,
    "Bacillus megaterium": 20, "Bacillus subtilis": 3,
    "Basfia succiniciproducens": 18, "Chlorobaculum tepidum": 202,
    "Clostridium acetobutylicum": 22, "Corynebacterium glutamicum": 2,
    "Cyanothece 51142": 201, "Desulfovibrio vulgaris Hildenborough": 24,
    "Dinoroseobacter shibae": 205, "Escherichia coli": 1,
    "Geobacillus thermoglucosidasius": 25, "Geobacter metallireducens": 26,
    "Gluconobacter oxydans": 27, "Mycobacterium bovis BCG": 29,
    "Mycobacterium tuberculosis": 30, "Nonomuraea sp.": 31,
    "Paracoccus versutus": 32, "Phaeobacter gallaeciensis": 207,
    "Pseudomonas aeruginosa": 13, "Pseudomonas denitrificans": 12,
    "Pseudomonas fluorescens": 11, "Pseudomonas putida": 4,
    "Rhodobacter sphaeroides": 206, "Rhodopseudomonas palustris": 204,
    "Shewanella oneidensis": 6, "Sinorhizobium meliloti": 33,
    "Sorangium cellulosum": 34, "Streptomyces": 38,
    "Synechocystis 6803": 203, "Thermoanaerobacter sp": 35,
    "Thermus thermophilus": 36, "Xanthomonas campestris": 37,
    "Zymomonas mobilis": 10
}

NutrientType = {
    "Sufficient": 1, "Carbon source limited": 2,
    "Nitrogen source limited": 3, "Phosphate source limited": 4,
    "Under stress/toxic condition": 5
}

OxygenCondition={
    "Aerobic": 1, "Anaerobic": 2, "Microaerophilic": 3
}

GeneticBackground = {
    "Wild type": 1, "With plasmid (low overexpression burden)": 2,
    "Protein overexpression": 3, "Gene Knockout(KO)": 4,
    "KO + plasmid (low overexpression burden)": 5, "KO + protein overexpression": 6
}

Substrate = {
    "Glucose": 1, "Fructose": 2, "Galactose": 3,
    "Gluconate": 4, "Glutamate": 5, "Citrate": 6,
    "Xylose": 7, "Succinate": 8, "Malate": 9,
    "Lactate": 10, "Pyruvate": 11, "Glycerol": 12,
    "Acetate": 13, "NaHCO₃": 14
}

@funix(disable=True)
def getArgumentValue(argument: str, value: str) -> float:
    if argument == "Reactor":
        return ReactorType[value]
    if argument == "Species":
        return Species[value]
    if argument == "Nutrient":
        return NutrientType[value]
    if argument == "Oxygen":
        return OxygenCondition[value]
    if argument == "Method":
        return GeneticBackground[value]
    if argument == "Substrate_first":
        return Substrate[value]
    if argument == "Substrate_sec":
        return Substrate[value]
    return 0.0

intro= """# Bacterial flux prediction

by [Forrest Bao](https://github.com/forrestbao), [Yazawazi](https://github.com/Yazawazi/), [Stephen Wu](https://www.linkedin.com/in/gangwustl), and [Yinjie Tang](https://tang.eece.wustl.edu/)

Funded by NSF grants 1356669 and 1821828

Cite:  Wu et al., Rapid prediction of bacterial heterotrophic fluxomics using machine learning and constraint programming, PLoS Computational Biology, 2016, DOI: 10.1371/journal.pcbi.1004838

Source code: https://github.com/Yazawazi/MFlux

Please report issues via our Github page.
"""

@funix(
    description=intro,
    whitelist={
        "Reactor": list(ReactorType.keys()), "Species": list(Species.keys()),
        "Nutrient": list(NutrientType.keys()), "Oxygen": list(OxygenCondition.keys()),
        "Method": list(GeneticBackground.keys()), "Substrate_first": list(Substrate.keys()),
        "Substrate_sec": list(Substrate.keys())
    },
    argument_labels={
        "Reactor": "Reactor Type", "Species": "Species",
        "Nutrient": "Nutrient Type", "Oxygen": "Oxygen Condition",
        "Method": "Genetic Background", "Growth_rate": "Growth Rate (h⁻¹)",
        "Substrate_uptake_rate": "Total Substrate Uptake Rate (mmol * g⁻¹ * h⁻¹)",
        "Substrate_first": "Primary Substrate",
        "Ratio_first": "Molar Ratio of Primary Substrate",
        "Substrate_sec": "Secondary Substrate",
        "lb1": "Min", "ub1": "Max", "lb2": "Min", "ub2": "Max",
        "lb3": "Min", "ub3": "Max", "lb4": "Min", "ub4": "Max",
        "lb5": "Min", "ub5": "Max", "lb6": "Min", "ub6": "Max",
        "lb7": "Min", "ub7": "Max", "lb8": "Min", "ub8": "Max",
        "lb9": "Min", "ub9": "Max", "lb10": "Min", "ub10": "Max",
        "lb11": "Min", "ub11": "Max", "lb12": "Min", "ub12": "Max",
        "lb13": "Min", "ub13": "Max", "lb14": "Min", "ub14": "Max",
        "lb15": "Min", "ub15": "Max", "lb16": "Min", "ub16": "Max",
        "lb17": "Min", "ub17": "Max", "lb18": "Min", "ub18": "Max",
        "lb19": "Min", "ub19": "Max", "lb20": "Min", "ub20": "Max",
        "lb21": "Min", "ub21": "Max", "lb22": "Min", "ub22": "Max",
        "lb23": "Min", "ub23": "Max", "lb24": "Min", "ub24": "Max",
        "lb25": "Min", "ub25": "Max", "lb26": "Min", "ub26": "Max",
        "lb27": "Min", "ub27": "Max", "lb28": "Min", "ub28": "Max",
        "lb29": "Min", "ub29": "Max"
    },
    input_layout=[
        [{'dividing':""}],
        [{"markdown":"Select or enter the values for your experiment and we will compute the flux values for you."}],
        [
            {"argument": "Reactor"},
            {"argument": "Species"}
        ],
        [
            {"argument": "Nutrient"},
            {"argument": "Oxygen"}
        ],
        [{"argument": "Method"}],
        [
            {"argument": "Growth_rate"},
            {"markdown": "Normally in the range of [0, 2] h<sup>-1</sup>"}
        ],
        [{"argument": "Substrate_uptake_rate"}],
        [{"argument": "Substrate_first"}],
        [
            {"argument": "Ratio_first", "width": 8},
            {"markdown": "In the range of [0, 1]"}
        ],
        [{"argument": "Substrate_sec"}],
        [{"markdown": "Note: The Molar ratio of the 2nd substrate is calulated as (1 - that of primary substrate) automatically"}],
        [{"dividing": True}],
        [{"markdown": "**For genetically modified strain, you can manually set boundaries for fluxes below. Leave intact to use default values. Do NOT enter 0 unless you really want to.**"}],
        [{"markdown": "Glucose ⇒ G6P (glk/ptsG)"}],
        [
            {"argument": "lb1"},
            {"argument": "ub1"}
        ],
        [{"markdown": "G6P ⇒ F6P (pgi)"}],
        [
            {"argument": "lb2"},
            {"argument": "ub2"}
        ],
        [{"markdown": "FBP(F6P) ⇒ GAP + DHAP (pfk/fba)"}],
        [
            {"argument": "lb3"},
            {"argument": "ub3"}
        ],
        [{"markdown": "DHAP ⇒ GAP (tpiA)"}],
        [
            {"argument": "lb4"},
            {"argument": "ub4"}
        ],
        [{"markdown": "GAP ⇒ 3PG (gapA/gapC)"}],
        [
            {"argument": "lb5"},
            {"argument": "ub5"}
        ],
        [{"markdown": "3PG ⇒ PEP (gpm/eno)"}],
        [
            {"argument": "lb6"},
            {"argument": "ub6"}
        ],
        [{"markdown": "PEP ⇒ PYR (pyk/ptsG/ppsA)"}],
        [
            {"argument": "lb7"},
            {"argument": "ub7"}
        ],
        [{"markdown": "PYR ⇒ AceCoA (lpd/pfl/tdcE/aceE/aceF)"}],
        [
            {"argument": "lb8"},
            {"argument": "ub8"}
        ],
        [{"markdown": "AceCoA ⇒ Acetate (pta/ackA)"}],
        [
            {"argument": "lb9"},
            {"argument": "ub9"}
        ],
        [{"markdown": "G6P ⇒ 6PG (zwf/pgl)"}],
        [
            {"argument": "lb10"},
            {"argument": "ub10"}
        ],
        [{"markdown": "6PG ⇒ Ru5P + CO₂ (gnd)"}],
        [
            {"argument": "lb11"},
            {"argument": "ub11"}
        ],
        [{"markdown": "Ru5P ⇒ X5P (rpe)"}],
        [
            {"argument": "lb12"},
            {"argument": "ub12"}
        ],
        [{"markdown": "Ru5P ⇔ R5P (rpi)"}],
        [
            {"argument": "lb13"},
            {"argument": "ub13"}
        ],
        [{"markdown": "X5P + R5P ⇔ S7P + GAP (tkt)"}],
        [
            {"argument": "lb14"},
            {"argument": "ub14"}
        ],
        [{"markdown": "X5P + E4P ⇔ F6P + GAP (tal)"}],
        [
            {"argument": "lb15"},
            {"argument": "ub15"}
        ],
        [{"markdown": "S7P + GAP ⇒ F6P + E4P (tkt)"}],
        [
            {"argument": "lb16"},
            {"argument": "ub16"}
        ],
        [{"markdown": "AceCoA ⇒ CIT (gltA/prpC)"}],
        [
            {"argument": "lb17"},
            {"argument": "ub17"}
        ],
        [{"markdown": "CIT ⇒ ICIT (acn)"}],
        [
            {"argument": "lb18"},
            {"argument": "ub18"}
        ],
        [{"markdown": "ICIT ⇒ AKG + CO₂ (icd)"}],
        [
            {"argument": "lb19"},
            {"argument": "ub19"}
        ],
        [{"markdown": "AKG ⇒ SUC + CO₂ (suc)"}],
        [
            {"argument": "lb20"},
            {"argument": "ub20"}
        ],
        [{"markdown": "SUC ⇒ FUM (sdhABCD/frdABCD)"}],
        [
            {"argument": "lb21"},
            {"argument": "ub21"}
        ],
        [{"markdown": "FUM ⇔ MAL (fumABC)"}],
        [
            {"argument": "lb22"},
            {"argument": "ub22"}
        ],
        [{"markdown": "MAL ⇔ OAA (mdh/mqo)"}],
        [
            {"argument": "lb23"},
            {"argument": "ub23"}
        ],
        [{"markdown": "ICIT ⇒ GLX + SUC & GLX + AceCoA --> MAL (aceA/aceB)"}],
        [
            {"argument": "lb24"},
            {"argument": "ub24"}
        ],
        [{"markdown": "6PG ⇒ PYR + GAP (edd/eda)"}],
        [
            {"argument": "lb25"},
            {"argument": "ub25"}
        ],
        [{"markdown": "AceCoA ⇒ Ethanol (adh)"}],
        [
            {"argument": "lb26"},
            {"argument": "ub26"}
        ],
        [{"markdown": "PYR ⇒ Lactate (ldh)"}],
        [
            {"argument": "lb27"},
            {"argument": "ub27"}
        ],
        [{"markdown": "PEP + CO₂ ⇔ OAA (ppc/ppk)"}],
        [
            {"argument": "lb28"},
            {"argument": "ub28"}
        ],
        [{"markdown": "MAL ⇒ PYR + CO₂ (maeA/maeB)"}],
        [
            {"argument": "lb29"},
            {"argument": "ub29"}
        ]
    ]
)
def mflux(
    Reactor: str = "Batch (closed bottle)",
    Species: str = "Escherichia coli",
    Nutrient: str = "Phosphate source limited",
    Oxygen: str = "Anaerobic",
    Method: str = "Gene Knockout(KO)",
    Growth_rate: float = 1.45,
    Substrate_uptake_rate: float = 2,
    Substrate_first: str = "Glucose",
    Ratio_first: float = 0.7, Substrate_sec: str = "NaHCO₃",
    lb1: float = 0, ub1: float = 100, lb2: float = -99.9, ub2: float = 99.5,
    lb3: float = -51.5, ub3: float = 99.3, lb4: float = -51.5, ub4: float = 99.3,
    lb5: float = -13.5, ub5: float = 216.6, lb6: float = -23.3, ub6: float = 196.2,
    lb7: float = -36, ub7: float = 232, lb8: float = -7.9, ub8: float = 213.1,
    lb9: float = 0, ub9: float = 135, lb10: float = 0, ub10: float = 151.4,
    lb11: float = 0, ub11: float = 113.7, lb12: float = -33, ub12: float = 94.1,
    lb13: float = -94.4, ub13: float = 41.2, lb14: float = -2, ub14: float = 47.5,
    lb15: float = -6.6, ub15: float = 71, lb16: float = -2, ub16: float = 47.5,
    lb17: float = 0, ub17: float = 189, lb18: float = 0, ub18: float = 189,
    lb19: float = 0, ub19: float = 189, lb20: float = 0, ub20: float = 194,
    lb21: float = -105, ub21: float = 194, lb22: float = -106, ub22: float = 194,
    lb23: float = -144.3, ub23: float = 181.5, lb24: float = 0, ub24: float = 55,
    lb25: float = 0, ub25: float = 148, lb26: float = 0, ub26: float = 193.2,
    lb27: float = 0, ub27: float = 151, lb28: float = -67.6, ub28: float = 149.8,
    lb29: float = -13.5, ub29: float = 104.2
) -> HTML:
    global lastWords
    lastWords = ""
    def pushLastWords(something: str) -> None:
        global lastWords
        lastWords += something + "\n"

    Feature_names =  [
        "Species",
        "Reactor",
        "Nutrient",
        "Oxygen",
        "Method",
        "Growth_rate",
        "Substrate_uptake_rate",
        "Substrate_first",
        "Ratio_first",
        "Substrate_sec"
    ]
    Specielist = ["Growth_rate", "Substrate_uptake_rate", "Ratio_first"]
    Features = {
        "Energy": 1.0,
        "MFA": 1.0,
        "Substrate_other": 0.0,
        "Ratio_sec": 0.0
    }
    for Feature_name in Feature_names:
        if Feature_name in Specielist:
            # I am sorry, but eval is so good here, lazy haha
            Features[Feature_name] = eval(Feature_name)
        else:
            Features[Feature_name] = getArgumentValue(Feature_name, eval(Feature_name))
        pushLastWords(f"{Feature_name}: {Features[Feature_name]}")

    import libflux
    Vector, Substrates = libflux.process_input(Features, pushLastWords)
    # Boundary_dict = libflux.process_boundaries(request, Substrates)
    # No bro
    Substrate2Index = {
        "glucose": 1,
        "galactose": 3,
        "fructose": 2,
        "gluconate": 4,
        "glutamate": 5,
        "citrate": 6,
        "xylose": 7,
        "succinate": 8,
        "malate": 9,
        "lactate": 10,
        "pyruvate": 11,
        "glycerol": 12,
        "acetate": 13
    }
    Feature_names = ["".join([Bound, ID]) for (Bound, ID) in itertools.product(["lb", "ub"], list(map(str, list(range(1, 29+1)))))]
    Features = {}
    for Feature_name in Feature_names:
        Feature_value = eval(Feature_name)
        if Feature_value:
            Features[Feature_name] = float(Feature_value)

    if Substrates[Substrate2Index["acetate"]] == 0:
        Features["lb9"] = 0
    if Substrates[Substrate2Index["lactate"]] == 0:
        Features["lb27"] = 0

    Boundary_dict = Features
    libflux.predict(Vector, Substrates, Boundary_dict, pushLastWords)

    #pushLastWords("<hr> \
    #    <p> \
    #    This project is supported by National Science Foundation. <a href='http://www.nsf.gov/awardsearch/showAward?AWD_ID=1356669'>More info</a> <br> \
    #    Information on this website only relects the perspectives of the individuals.<br> \
    #    Built by Forrest Sheng Bao <a href='http://fsbao.net'>http://fsbao.net </a> \
    #    </p>")
    return lastWords
