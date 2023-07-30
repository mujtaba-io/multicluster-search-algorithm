
# author: mujtaba
# date: july 30, 2023

# quickly test this search algorithm based on in-memory dataset before applying it to huge words-dataset

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans

def cluster_strings(strings, k):
    # Step 1: Calculate the cosine similarity matrix
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(strings)
    cosine_sim_matrix = cosine_similarity(tfidf_matrix)

    # Step 2: Perform K-Means clustering on the cosine similarity matrix
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(cosine_sim_matrix)

    # Step 3: Create k smaller sets
    clusters = {}
    for i, label in enumerate(kmeans.labels_):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(strings[i])

    return list(clusters.values())

# Example usage
huge_set_of_strings = [
    'anter', 'lifebelt', 'rounding', 'tumour', 'maistre', 'testimonial', 'blended', 'harder', 'kidney', 'spirals',
    'wedged', 'unpaid', 'scandalous', 'butta', 'inguinal', 'ewe', 'slanderous', 'subjunctive', 'placer', 'meritocracy',
    'pamphlet', 'occupational', 'mightn', 'omen', 'berry', 'kettle', 'coexistence', 'outbreak', 'virtuoso', 'histos',
    'sockets', 'electrotype', 'buyer', 'supportiveness', 'y3', 'receptionist', 'midden', 'sheaths', 'appellation',
    'concise', 'information', 'initiated', 'exterior', 'unpleasant', 'j2', 'percent', 'rockfall', 'carousel', 'biphenyl',
    'gloxinia', 'miraculous', 'donkey', 'potting', 'conservationist', 'redecorate', 'gogue', 'stentor', 'obliviousness',
    'nepos', 'promises', 'electing', 'kalendae', 'judgment', 'pert', 'alloyed', 'plated', 'cuff', 'architectonic',
    'equivocally', 'gibbus', 'inadmissibly', 'gchq', 'crueller', 'conifer', 'neos', 'strido', 'referee', 'blanc',
    'disconnected', 'salvageable', 'rulers', 'albinism', 'postulo', 'attributively', 'projector', 'slat', 'mercuric',
    'airbus', 'disgraceful', 'mover', 'flurried', 'oniony', 'predic', 'herbivorous', 'embalmment', 'preambles', 'roped',
    'pawn', 'discompose', 'contradictions', 'doubt', 'seedless', 'borders', 'heats', 'smiled', 'pivotal', 'uncomplimentary',
    'tumours', 'invisible', 'eventide', 'strident', 'telly', 'substantively', 'examining', 'nome', 'expressionism',
    'choc', 'incoherent', 'pug', 'escapement', 'concentrated', 'forewarn', 'intelligently', 'obviousness', 'plasticizer',
    'autumnal', 'clangour', 'errata', 'oversexed', 'omissions', 'sightings', 'menstruus', 'croaky', 'hotness', 'unmerited',
    'sloppy', 'comedienne', 'habitability', 'confundo', 'vespers', 'prodigious', 'militate', 'husky1', 'rudder', 'filo',
    'supervisory', 'denouncement', 'floundering', 'misfortunes', 'appendix', 'callisthenic', 'kelson', 'designer',
    'ersatz', 'hunger', 'furbish', 'macchia', 'lighter2', 'overwhelm', 'satchel', 'sandwiched', 'toot', 'palindromic',
    'wishers', 'retrodden', 'numerable', 'bane', 'propagator', 'castellated', 'emergencies', 'cwm', 'larix', 'purgatory',
    'psychedelia', 'iconic', 'mausolos', 'walkway', 'situ', 'ashcan', 'copartnership', 'offshoots', 'skua', 'counterpart',
    'mob', 'hooked', 'busk', 'summit', 'closest', 'triennial', 'vigil', 'awesome', 'yum', 'wooden', 'punt2', 'choppiness',
    'wriggled', 'jeebies', 'pentagonon', 'areola', 'redeemer', 'embargo', 'overprint', 'butterscotch', 'theion', 'refills',
    'satires', 'reanimate', 'sprinkling', 'multiplier', 'numbering', 'syllabus', 'rubellus', 'dactylic', 'admixture',
    'steal', 'hydropsy', 'modesty', 'borough', 'cackle', 'nominees', 'sopping', 'spermatozoon', 'stonking', 'girlhood',
    'quaere', 'accordionist', 'electrolyze', 'gaff', 'man', 'commitment', 'overheat', 'mudflap', 'live', 'alumni',
    'seafaring', 'mausoleum', 'shapeless', 'synthesizer', 'ler', 'wrathfully', 'indict', 'syrupy', 'hither', 'curs',
    'functioning', 'twinge', 'leaders', 'ntgen', 'engorged', 'gem', 'immeasurably', 'concordat', 'vortical', 'runabout',
    'maximization', 'enfeeble', 'reticulum', 'render', 'lag1', 'scrump', 'grossly', 'harlot', 'shoals', 'trap', 'foreground',
    'c4h9', 'approachable', 'windiness', 'fredum', 'bongo', 'knitter', 'unknowing', 'hierarchy', 'playfellow', 'khaite',
    'quad3', 'oillet', 'gambit', 'matrimonial', 'tire', 'puke', 'moonless', 'campaigning', 'duple', 'halftone', 'ultraviolet',
    'undermanned', 'observer', 'hustings', 'acer', 'inventing', 'obsequiousness', 'sulfite', 'kerosine', 'vicar', 'maxillary',
    'parturition', 'raspe', 'biker', 'trumped', 'sardonios', 'phrenology', 'unblushing', 'semite', 'saltiness', 'postal',
    'reactions', 'skin', 'rationalistic', 'somerset', 'treasures', 'outstandingly', 'slide', 'loaves', 'thrifty', 'diversify',
    'gentil', 'overeager', 'troubadour', 'phenomena', 'uv', 'tomber', 'arboretum', 'matt', 'vocabulary', 'goujon', 'elvish',
    'faster', 'queen', 'grenades', 'dentifrice', 'undertakes', 'conn', 'ette', 'unforgettable', 'unicyclist', 'grease',
    'unpardonably', 'cubism', 'curator', 'lateo', 'molding', 'spearmint', 'impishness', 'stagey', 'commanded', 'abridgement',
    'vendor', 'songlike', 'pythagoras', 'limelight', 'bushels', 'jehad', 'aperio', 'suppressing', 'intuition', 'curral',
    'dilution', 'lacks', 'absurd', 'holography', 'ungodly', 'underwriter', 'steps', 'simmering', 'prolongation', 'stasis',
    'squeak', 'sycophant', 'vindictiveness', 'homosexual', 'karyo', 'cbe', 'moans', 'dioikesis', 'sedatives', 'supervene',
    'pallium', 'venerator', 'unalloyed', 'quack2', 'auctioneer', 'ancilla', 'morbidity', 'sexton', 'ail', 'hum', 'diakonos',
    'electroencephalograph', 'unheeded', 'socialism', 'mantissa', 'exude', 'patty', 'whereabouts', 'contented', 'softwood',
    'mouldings', 'sanctity', 'habeas', 'osus', 'chemical', 'demotic', 'tonight', 'exhaustively', 'undecided', 'sedulously',
    'reunited', 'despotic', 'obsession', 'tunes', 'aid', 'vagina', 'keelson', 'jogtrot', 'tribesman', 'wesleyan', 'uncommonness',
    'chestnut', 'craftswoman', 'liquorice', 'standardizing', 'attentions', 'exquisite', 'hapless', 'biscuit', 'obedient',
    'kuparissos', 'crossbreed', 'tumble', '16th', 'snuff', 'gob', 'inductively', 'journalists', 'medicat', 'garage', 'gm',
    'fusils', 'zizuphon', 'symbolism', 'felspar', 'negatively', 'dumpiness', 'iniquitous', 'avoiding', 'fraud', 'assagai',
    'pouter', 'scotsman', 'meander', 'imperiousness', 'wittingly', 'repeal', 'kroner', 'muskiness', 'tasted', 'jim',
    'preserver', 'hurtful', 'clubbable', 'scopic', 'freebooter', 'commentator', 'stimulated', 'congenitally', 'paeony', 'ia',
    'jelly', 'walrus', 'heck', 'conquest', 'intercourse', 'masted', 'fixus', 'elation', 'midshipman', 'barm', 'temporary',
    'spores', 'tuner', 'roundabout', 'minder', 'precipitate', 'gum', 'fermi', 'fordable', 'dispersion', 'firry', 'collie',
    'liner2', 'sarzin', 'paracetamol', 'demerge', 'satis', 'apologies', 'veterinarian', 'simulating', 'verb', 'overweight',
    'straws', 'genteel', 'alcorque', 'paneling', 'fists', 'barrel', 'seepage', 'indicatory', 'bridged', 'arachnid', 'wars',
    'moveable', 'empower', 'marmot', 'wanderer', 'importunus', 'nifty', 'craters', 'siute', 'booing', 'imprisonment',
    'regional', 'risk', 'stronger', 'patrol', 'audax', 'sprats', 'commandeer', 'mesos', 'abstain', 'supposes', 'snuggest',
    'furtively', 'servitude', 'espaundre', 'promineo', 'horoscope', 'victims', 'commissioner', 'resonance', 'entirely',
    'barr', 'charismatic', 'maraca', 'synchronically', 'quark1', 'frisky', 'headband', 'risqu', 'react', 'slavish', 'differo',
    'notation', 'sulfon', 'leisure', 'pentagonal', 'talmud', 'wrick', 'heartbreaking', 'holier', 'skilful', 'computing',
    'wickerwork', 'daw', 'comfort', 'unlocking', 'does', 'rod', 'spool', 'kingpin', 'defendo', 'baritone', 'persuasive',
    'surplus', 'proletariat', 'gloves', 'stimuli', 'cuing', 'phileo', 'baaed', 'idem', 'congaed'
]


# Call the clustering function again with the updated set of strings
k = 3  # Number of resulting sets
resulting_sets = cluster_strings(huge_set_of_strings, k)

# Print the resulting sets
for i, smaller_set in enumerate(resulting_sets):
    print(f"Set {i + 1}: {smaller_set}")

