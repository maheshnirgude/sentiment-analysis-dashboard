"""Lexicon-based sentiment scorer — transparent and dependency-light."""

POSITIVE = {"great", "good", "love", "excellent", "amazing", "fast", "helpful", "easy", "best", "happy"}
NEGATIVE = {"bad", "slow", "hate", "terrible", "awful", "broken", "worst", "bug", "difficult", "poor"}
NEGATORS = {"not", "never", "no"}


def analyze(text: str) -> dict:
    tokens = text.lower().replace(".", " ").replace(",", " ").split()
    score = 0
    for i, tok in enumerate(tokens):
        value = 1 if tok in POSITIVE else -1 if tok in NEGATIVE else 0
        if value and i > 0 and tokens[i - 1] in NEGATORS:
            value = -value
        score += value
    label = "positive" if score > 0 else "negative" if score < 0 else "neutral"
    return {"score": score, "label": label}
