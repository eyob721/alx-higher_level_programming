#!/usr/bin/python3
def multiple_returns(sentence):
    """A function that returns a tuple with the length of a sentence and its
    first character

    Args:
        sentence: a given sentence

    Returns:
        - A tuple with the length of the sentence and its first character
        - If the sentence is empty, the first character will be None

    """
    if sentence is not None:
        stc_len = len(sentence)
        stc_fst_chr = None if stc_len == 0 else sentence[0]
        return stc_len, stc_fst_chr
    return None, None
