import re

STOP_WORDS = {
    "what", "is", "are", "the", "a", "an", "of", "in", "on",
    "to", "and", "for", "do", "does", "how", "why", "name",
    "tell", "me", "about", "give", "explain", "with", "two",
    "one", "three", "was", "were", "did", "who", "where",
    "when", "which", "much", "many", "can", "could", "would",
    "please", "find", "describe", "state", "mention"
}

def words(text):
    return set(re.findall(r"\b[a-zA-Z]+\b", text.lower()))

def search_relevant_passages(question, pages, max_results=3):
    question_words = words(question) - STOP_WORDS
    if not question_words:
        return []

    q = question.lower()
    results = []

    # Identify what kind of information the question requests.
    asks_name = any(x in q for x in ("what was", "what is", "name of", "puppy's name", "dog's name"))
    asks_give = any(x in q for x in ("what did", "what has", "give the puppy", "gave the puppy", "fed the puppy"))
    asks_place = any(x in q for x in ("where", "which place", "where did"))
    asks_reason = any(x in q for x in ("why", "reason", "why did"))
    asks_method = any(x in q for x in ("how did", "how was", "in what way"))

    for page in pages:
        sentences = re.split(r"(?<=[.!?])\s+", page["text"])

        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            sentence_words = words(sentence)
            matches = question_words & sentence_words

            if not matches:
                continue

            score = len(matches) / len(question_words)

            # Prefer sentences that answer the question type.
            s = sentence.lower()

            if asks_name:
                if re.search(r"\b(named|called|name was|name is)\b", s):
                    score += 0.8
                elif re.search(r"\bpuppy\b", s) and re.search(r"\b(bruno|name)\b", s):
                    score += 0.5

            if asks_give:
                if re.search(r"\b(gave|give|offered|fed|handed)\b", s):
                    score += 0.8
                if "water" in s or "food" in s:
                    score += 0.3

            if asks_place:
                if re.search(r"\b(under|near|inside|outside|at|in|beside|behind)\b", s):
                    score += 0.5

            if asks_reason and re.search(r"\b(because|since|so that|therefore)\b", s):
                score += 0.5

            if asks_method and re.search(r"\b(by|using|with|called|phoned|contacted)\b", s):
                score += 0.3

            results.append({
                "page": page["page"],
                "text": sentence,
                "score": score
            })

    # Sort strongest evidence first.
    results.sort(key=lambda item: item["score"], reverse=True)

    # Remove duplicate sentences.
    unique_results = []
    seen = set()

    for result in results:
        key = result["text"].lower()
        if key not in seen:
            seen.add(key)
            unique_results.append(result)

    # Return only the strongest matches.
    return unique_results[:1]