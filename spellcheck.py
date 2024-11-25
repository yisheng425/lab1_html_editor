from spellchecker import SpellChecker

def spell_check(element):
    """Performs spell check on text content of the HTML element."""
    spell = SpellChecker()
    errors = []
    
    def check_text(text):
        words = text.split()
        misspelled = spell.unknown(words)
        return {word: spell.candidates(word) for word in misspelled}

    def recursive_check(el):
        if el.text_content:
            text_errors = check_text(el.text_content)
            if text_errors:
                errors.append((el.id, text_errors))
        for child in el.children:
            recursive_check(child)

    recursive_check(element)
    return errors
