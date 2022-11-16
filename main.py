import itertools
from pydatafront.decorator import funix_export

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

@funix_export(
    description="@[Forrest Bao](https://github.com/forrestbao), [MFlux](https://github.com/forrestbao/mflux)",
    whitelist={
        "Reactor": list(ReactorType.keys()), "Species": list(Species.keys()),
        "Nutrient": list(NutrientType.keys()), "Oxygen": list(OxygenCondition.keys()),
        "Method": list(GeneticBackground.keys()), "Substrate_first": list(Substrate.keys()),
        "Substrate_sec": list(Substrate.keys())
    },
    returnHTML=True,
    labels={
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
    layout=[
        [
            {"type": "argument", "argument": "Reactor"},
            {"type": "argument", "argument": "Species"}
        ],
        [
            {"type": "argument", "argument": "Nutrient"},
            {"type": "argument", "argument": "Oxygen"}
        ],
        [{"type": "argument", "argument": "Method"}],
        [
            {"type": "argument", "argument": "Growth_rate"},
            {"type": "markdown", "content": "Normally in the range of [0, 2] h<sup>-1</sup>"}
        ],
        [{"type": "argument", "argument": "Substrate_uptake_rate"}],
        [{"type": "argument", "argument": "Substrate_first"}],
        [
            {"type": "argument", "argument": "Ratio_first", "width": 8},
            {"type": "markdown", "content": "In the range of [0, 1]"}
        ],
        [{"type": "argument", "argument": "Substrate_sec"}],
        [{"type": "markdown", "content": "Note: The Molar ratio of the 2nd substrate is calulated as (1 - that of primary substrate) automatically"}],
        [{"type": "dividing"}],
        [{"type": "markdown", "content": "**For genetically modified strain, you can manually set boundaries for fluxes below. Leave intact to use default values. Do NOT enter 0 unless you really want to.**"}],
        [{"type": "markdown", "content": "Glucose ⇒ G6P (glk/ptsG)"}],
        [
            {"type": "argument", "argument": "lb1"},
            {"type": "argument", "argument": "ub1"}
        ],
        [{"type": "markdown", "content": "G6P ⇒ F6P (pgi)"}],
        [
            {"type": "argument", "argument": "lb2"},
            {"type": "argument", "argument": "ub2"}
        ],
        [{"type": "markdown", "content": "FBP(F6P) ⇒ GAP + DHAP (pfk/fba)"}],
        [
            {"type": "argument", "argument": "lb3"},
            {"type": "argument", "argument": "ub3"}
        ],
        [{"type": "markdown", "content": "DHAP ⇒ GAP (tpiA)"}],
        [
            {"type": "argument", "argument": "lb4"},
            {"type": "argument", "argument": "ub4"}
        ],
        [{"type": "markdown", "content": "GAP ⇒ 3PG (gapA/gapC)"}],
        [
            {"type": "argument", "argument": "lb5"},
            {"type": "argument", "argument": "ub5"}
        ],
        [{"type": "markdown", "content": "3PG ⇒ PEP (gpm/eno)"}],
        [
            {"type": "argument", "argument": "lb6"},
            {"type": "argument", "argument": "ub6"}
        ],
        [{"type": "markdown", "content": "PEP ⇒ PYR (pyk/ptsG/ppsA)"}],
        [
            {"type": "argument", "argument": "lb7"},
            {"type": "argument", "argument": "ub7"}
        ],
        [{"type": "markdown", "content": "PYR ⇒ AceCoA (lpd/pfl/tdcE/aceE/aceF)"}],
        [
            {"type": "argument", "argument": "lb8"},
            {"type": "argument", "argument": "ub8"}
        ],
        [{"type": "markdown", "content": "AceCoA ⇒ Acetate (pta/ackA)"}],
        [
            {"type": "argument", "argument": "lb9"},
            {"type": "argument", "argument": "ub9"}
        ],
        [{"type": "markdown", "content": "G6P ⇒ 6PG (zwf/pgl)"}],
        [
            {"type": "argument", "argument": "lb10"},
            {"type": "argument", "argument": "ub10"}
        ],
        [{"type": "markdown", "content": "6PG ⇒ Ru5P + CO₂ (gnd)"}],
        [
            {"type": "argument", "argument": "lb11"},
            {"type": "argument", "argument": "ub11"}
        ],
        [{"type": "markdown", "content": "Ru5P ⇒ X5P (rpe)"}],
        [
            {"type": "argument", "argument": "lb12"},
            {"type": "argument", "argument": "ub12"}
        ],
        [{"type": "markdown", "content": "Ru5P ⇔ R5P (rpi)"}],
        [
            {"type": "argument", "argument": "lb13"},
            {"type": "argument", "argument": "ub13"}
        ],
        [{"type": "markdown", "content": "X5P + R5P ⇔ S7P + GAP (tkt)"}],
        [
            {"type": "argument", "argument": "lb14"},
            {"type": "argument", "argument": "ub14"}
        ],
        [{"type": "markdown", "content": "X5P + E4P ⇔ F6P + GAP (tal)"}],
        [
            {"type": "argument", "argument": "lb15"},
            {"type": "argument", "argument": "ub15"}
        ],
        [{"type": "markdown", "content": "S7P + GAP ⇒ F6P + E4P (tkt)"}],
        [
            {"type": "argument", "argument": "lb16"},
            {"type": "argument", "argument": "ub16"}
        ],
        [{"type": "markdown", "content": "AceCoA ⇒ CIT (gltA/prpC)"}],
        [
            {"type": "argument", "argument": "lb17"},
            {"type": "argument", "argument": "ub17"}
        ],
        [{"type": "markdown", "content": "CIT ⇒ ICIT (acn)"}],
        [
            {"type": "argument", "argument": "lb18"},
            {"type": "argument", "argument": "ub18"}
        ],
        [{"type": "markdown", "content": "ICIT ⇒ AKG + CO₂ (icd)"}],
        [
            {"type": "argument", "argument": "lb19"},
            {"type": "argument", "argument": "ub19"}
        ],
        [{"type": "markdown", "content": "AKG ⇒ SUC + CO₂ (suc)"}],
        [
            {"type": "argument", "argument": "lb20"},
            {"type": "argument", "argument": "ub20"}
        ],
        [{"type": "markdown", "content": "SUC ⇒ FUM (sdhABCD/frdABCD)"}],
        [
            {"type": "argument", "argument": "lb21"},
            {"type": "argument", "argument": "ub21"}
        ],
        [{"type": "markdown", "content": "FUM ⇔ MAL (fumABC)"}],
        [
            {"type": "argument", "argument": "lb22"},
            {"type": "argument", "argument": "ub22"}
        ],
        [{"type": "markdown", "content": "MAL ⇔ OAA (mdh/mqo)"}],
        [
            {"type": "argument", "argument": "lb23"},
            {"type": "argument", "argument": "ub23"}
        ],
        [{"type": "markdown", "content": "ICIT ⇒ GLX + SUC & GLX + AceCoA --> MAL (aceA/aceB)"}],
        [
            {"type": "argument", "argument": "lb24"},
            {"type": "argument", "argument": "ub24"}
        ],
        [{"type": "markdown", "content": "6PG ⇒ PYR + GAP (edd/eda)"}],
        [
            {"type": "argument", "argument": "lb25"},
            {"type": "argument", "argument": "ub25"}
        ],
        [{"type": "markdown", "content": "AceCoA ⇒ Ethanol (adh)"}],
        [
            {"type": "argument", "argument": "lb26"},
            {"type": "argument", "argument": "ub26"}
        ],
        [{"type": "markdown", "content": "PYR ⇒ Lactate (ldh)"}],
        [
            {"type": "argument", "argument": "lb27"},
            {"type": "argument", "argument": "ub27"}
        ],
        [{"type": "markdown", "content": "PEP + CO₂ ⇔ OAA (ppc/ppk)"}],
        [
            {"type": "argument", "argument": "lb28"},
            {"type": "argument", "argument": "ub28"}
        ],
        [{"type": "markdown", "content": "MAL ⇒ PYR + CO₂ (maeA/maeB)"}],
        [
            {"type": "argument", "argument": "lb29"},
            {"type": "argument", "argument": "ub29"}
        ]
    ]
)
def mflux(
    Reactor: str, Species: str, Nutrient: str, Oxygen: str, Method: str,
    Growth_rate: float, Substrate_uptake_rate: float,
    Substrate_first: str, Ratio_first: float, Substrate_sec: str,
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
):
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

    pushLastWords("<hr> \
        <p> \
        This project is supported by National Science Foundation. <a href='http://www.nsf.gov/awardsearch/showAward?AWD_ID=1356669'>More info</a> <br> \
        Information on this website only relects the perspectives of the individuals.<br> \
        Built by Forrest Sheng Bao <a href='http://fsbao.net'>http://fsbao.net </a> \
        </p>")
    return lastWords
