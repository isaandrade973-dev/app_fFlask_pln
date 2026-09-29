import spacy

# Carrega o modelo de linguagem em português do spaCy
nlp = spacy.load("pt_core_news_sm")

# Dicionário léxico simplificado para classificação de sentimento
# Em produção, este componente pode ser substituído por um modelo de ML (TextCategorizer do spaCy)
POSITIVE_WORDS = {
    "excelente", "ótimo", "otimo", "bom", "boa", "maravilhoso", "incrível", 
    "incrivel", "adoré", "adorei", "gostei", "recomendo", "parabéns", "parabens", 
    "satisfeito", "sensacional", "perfeito", "top", "satisfeita"
}

NEGATIVE_WORDS = {
    "péssimo", "pessimo", "ruim", "horrível", "horrivel", "odiei", "demorado", 
    "decepcionante", "decepção", "decepcao", "insatisfeito", "insatisfeita", 
    "problema", "defeito", "pior", "lento", "terrivel", "terrível"
}

def analyze_sentiment(text: str) -> tuple[str, float]:
    """
    Processa o texto usando spaCy e calcula o sentimento com base
    na lemmatização e na presença de palavras com polaridade.
    
    Retorna:
        tuple: (classificacao, pontuacao)
    """
    doc = nlp(text.lower())
    
    pos_count = 0
    neg_count = 0
    total_tokens = 0

    for token in doc:
        # Descarta pontuação e stop words
        if not token.is_punct and not token.is_stop:
            lemma = token.lemma_
            total_tokens += 1
            
            if lemma in POSITIVE_WORDS or token.text in POSITIVE_WORDS:
                pos_count += 1
            elif lemma in NEGATIVE_WORDS or token.text in NEGATIVE_WORDS:
                neg_count += 1

    score = pos_count - neg_count

    if score > 0:
        sentiment = "Positivo"
    elif score < 0:
        sentiment = "Negativo"
    else:
        sentiment = "Neutro"

    return sentiment, score