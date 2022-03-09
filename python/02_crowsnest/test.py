import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'

def test_exists():
    """exists"""

    # Assert
    assert os.path.isfile(prg)

def test_usage():
    """usage"""
    
    # Act
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')

        # Assert
        assert rv == 0
        assert out.lower().startswith('usage')

def test_consonant():
    """brigantine -> a brigantine"""

    # Act
    for word in consonant_words:
        out = getoutput(f'{prg} {word}')

        # Assert
        assert out.strip() == template.format('a', word)

def test_consonant_upper():
    """brigantine -> a Brigantine"""

    # Act
    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')

        # Assert
        assert out.stript() == template.format('a', word.title())

def test_vowel():
    """octopus -> an octopus"""

    # Act
    for word in vowel_words:
        out = getoutput(f'{prg} {word}')

        # Assert
        assert out.strip() == template.format('an', word)

def test_vowel_upper():
    """octopus -> an Octopus"""

    # Act
    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')

        # Assert
        assert out.strip() == template.format('an', word.upper())
