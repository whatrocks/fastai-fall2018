import random
facts = {
    'charlie': [
        'ask him about the fast.ai course',
        'he loves pizza',
        'he is writing a book right now'
    ],
    'jack': [
        'loves reading books',
        "his fiancee's name is Ali",
        'studying law right now'
    ],
    'brian': [
        'just got married!',
    ],
    'peter': [
        'lives in san francisco',
        'just bought a new fishing pole from a pawn shop',
    ],
    'michael': [
        'his band name is dark city strings',
        'works in new york city',
        'needs a haircut',
    ],
    'luke': [
        'lives in chicago',
        'working in the entertainment industry',
    ],
    'jimmy': [
        'just got his PhD!',
        'works and lives in kansas now',
        'loves garfield comics',
    ]
}

def fact_finder(label: str) -> str:
    return random.choice(facts[label])