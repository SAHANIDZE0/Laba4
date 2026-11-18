def count_words(sentence):
    """Принимает строку, возвращает количество слов"""
    if not sentence or not sentence.strip():
        return 0
    return len(sentence.split())