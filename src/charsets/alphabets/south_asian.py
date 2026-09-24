# -*- coding: utf-8 -*-
"""South Asian scripts for 12+ languages."""

# ---------------------------------------------------------------------------
# Devanagari
# ---------------------------------------------------------------------------
DEVANAGARI_VOWELS = "अआइईउऊऋएऐओऔअंअः"
DEVANAGARI_CONSONANTS = "कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह"
DEVANAGARI_LETTERS = DEVANAGARI_VOWELS + DEVANAGARI_CONSONANTS + "क्षत्रज्ञश्र"
DEVANAGARI_LETTERS_LIST = list(DEVANAGARI_LETTERS)

# ---------------------------------------------------------------------------
# Bengali
# ---------------------------------------------------------------------------
BENGALI_VOWELS = "অআইঈউঊঋএঐওঔ"
BENGALI_CONSONANTS = "কখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়ৎ"
BENGALI_LETTERS = BENGALI_VOWELS + BENGALI_CONSONANTS
BENGALI_LETTERS_LIST = list(BENGALI_LETTERS)

# ---------------------------------------------------------------------------
# Gurmukhi (Punjabi)
# ---------------------------------------------------------------------------
GURMUKHI_VOWELS = "ਅਆਇਈਉਊਏਐਓਔ"
GURMUKHI_CONSONANTS = "ਕਖਗਘਙਚਛਜਝਞਟਠਡਢਣਤਥਦਧਨਪਫਬਭਮਯਰਲਵਸਹ"
GURMUKHI_LETTERS = GURMUKHI_VOWELS + GURMUKHI_CONSONANTS + "ੜਸ਼ਖ਼ਗ਼ਜ਼ਫ਼"

# ---------------------------------------------------------------------------
# Gujarati
# ---------------------------------------------------------------------------
GUJARATI_VOWELS = "અઆઇઈઉઊઋએઐઓઔ"
GUJARATI_CONSONANTS = "કખગઘઙચછજઝઞટઠડઢણતથદધનપફબભમયરલવશષસહ"
GUJARATI_LETTERS = GUJARATI_VOWELS + GUJARATI_CONSONANTS + "ળક્ષજ્ઞ"

# ---------------------------------------------------------------------------
# Odia
# ---------------------------------------------------------------------------
ODIA_VOWELS = "ଅଆଇଈଉଊଋଏଐଓଔ"
ODIA_CONSONANTS = "କଖଗଘଙଚଛଜଝଞଟଠଡଢଣତଥଦଧନପଫବଭମଯରଲଵଶଷସହ"
ODIA_LETTERS = ODIA_VOWELS + ODIA_CONSONANTS + "ଡ଼ଢ଼ୟୱ"

# ---------------------------------------------------------------------------
# Tamil
# ---------------------------------------------------------------------------
TAMIL_VOWELS = "அஆஇஈஉஊஎஏஐஒஓஔ"
TAMIL_CONSONANTS = "கஙசஞடணதநபமயரலவழளறன"
TAMIL_LETTERS = TAMIL_VOWELS + TAMIL_CONSONANTS + "ஜஷஸஹக்ஷஶ"

# ---------------------------------------------------------------------------
# Telugu
# ---------------------------------------------------------------------------
TELUGU_VOWELS = "అఆఇఈఉఊఋఎఏఐఒఓఔ"
TELUGU_CONSONANTS = "కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరఱలళవశషసహ"
TELUGU_LETTERS = TELUGU_VOWELS + TELUGU_CONSONANTS

# ---------------------------------------------------------------------------
# Kannada
# ---------------------------------------------------------------------------
KANNADA_VOWELS = "ಅಆಇಈಉಊಋಎಏಐಒಓಔ"
KANNADA_CONSONANTS = "ಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲಳವಶಷಸಹ"
KANNADA_LETTERS = KANNADA_VOWELS + KANNADA_CONSONANTS + "ಱೞ"

# ---------------------------------------------------------------------------
# Malayalam
# ---------------------------------------------------------------------------
MALAYALAM_VOWELS = "അആഇഈഉഊഋഎഏഐഒഓഔ"
MALAYALAM_CONSONANTS = "കഖഗഘങചഛജഝഞടഠഡഢണതഥദധനപഫബഭമയരലളവശഷസഹ"
MALAYALAM_LETTERS = MALAYALAM_VOWELS + MALAYALAM_CONSONANTS + "റ്റന്റ"

# ---------------------------------------------------------------------------
# Sinhala
# ---------------------------------------------------------------------------
SINHALA_VOWELS = "අආඇඈඉඊඋඌඍඎඏඐඑඒඓඔඕඖ"
SINHALA_CONSONANTS = "කඛගඝඞචඡජඣඤටඨඩඪණතථදධනපඵබභමයරලවශෂසහ"
SINHALA_LETTERS = SINHALA_VOWELS + SINHALA_CONSONANTS + "ළෆ"


ALL_SOUTH_ASIAN = "".join(dict.fromkeys(
    DEVANAGARI_LETTERS + BENGALI_LETTERS + GURMUKHI_LETTERS
    + GUJARATI_LETTERS + ODIA_LETTERS + TAMIL_LETTERS
    + TELUGU_LETTERS + KANNADA_LETTERS + MALAYALAM_LETTERS
    + SINHALA_LETTERS
))


__all__ = [name for name in dir() if name.isupper() and not name.startswith("_")]