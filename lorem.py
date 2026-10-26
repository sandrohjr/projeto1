import random

def gerar_lorem_ipsum(paragraphs_count=1):
    words = [
        "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
        "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
        "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam", "quis", "nostrud",
        "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea",
        "commodo", "consequat", "duis", "aute", "irure", "dolor", "in", "reprehenderit",
        "in", "voluptate", "velit", "esse", "cillum", "dolore", "eu", "fugiat", "nulla",
        "pariatur", "excepteur", "sint", "occaecat", "cupidatat", "non", "proident",
        "sunt", "in", "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id", "est", "laborum"
    ]
    
    paragraphs = []
    
    for _ in range(paragraphs_count):
        # Cria frases com tamanho aleatório entre 8 e 15 palavras
        sentences = []
        for _ in range(random.randint(3, 5)):
            sentence_words = random.choices(words, k=random.randint(8, 15))
            sentence = " ".join(sentence_words).capitalize() + "."
            sentences.append(sentence)
            
        paragraphs.append(" ".join(sentences))
        
    return "\n\n".join(paragraphs)

# Exemplo de uso gerando 2 parágrafos
print(gerar_lorem_ipsum(2))

