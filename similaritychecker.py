import os
import re
from difflib import SequenceMatcher

from pypdf import PdfReader


# ==========================================================
# PDF TEXT EXTRACTION
# ==========================================================

def extract_text_from_pdf(pdf_path):

    if not os.path.exists(pdf_path):
        return ""

    try:

        reader = PdfReader(pdf_path)

        pages = []

        for page in reader.pages:

            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)

    except Exception:
        return ""


# ==========================================================
# TEXT CLEANING
# ==========================================================

def clean_text(text):

    text = text.lower()

    # Remove punctuation
    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ==========================================================
# WORD SET
# ==========================================================

def get_word_set(text):

    cleaned = clean_text(text)

    return set(
        cleaned.split()
    )


# ==========================================================
# JACCARD SIMILARITY
# ==========================================================

def jaccard_similarity(text1, text2):

    words1 = get_word_set(text1)
    words2 = get_word_set(text2)

    if not words1 or not words2:
        return 0

    intersection = words1.intersection(
        words2
    )

    union = words1.union(
        words2
    )

    if not union:
        return 0

    score = (
        len(intersection) /
        len(union)
    ) * 100

    return score


# ==========================================================
# SEQUENCE SIMILARITY
# ==========================================================

def sequence_similarity(text1, text2):

    text1 = clean_text(text1)
    text2 = clean_text(text2)

    if not text1 or not text2:
        return 0

    score = SequenceMatcher(
        None,
        text1,
        text2
    ).ratio() * 100

    return score


# ==========================================================
# COMBINED SIMILARITY
# ==========================================================

def calculate_similarity(text1, text2):

    jaccard = jaccard_similarity(
        text1,
        text2
    )

    sequence = sequence_similarity(
        text1,
        text2
    )

    # Combine both methods
    score = (
        jaccard * 0.5 +
        sequence * 0.5
    )

    return round(
        score,
        2
    )


# ==========================================================
# CLASSIFY RESULT
# ==========================================================

def classify_similarity(score):

    if score >= 70:

        return (
            "High",
            "Possible plagiarism detected."
        )

    elif score >= 40:

        return (
            "Moderate",
            "Some similarity detected."
        )

    else:

        return (
            "Low",
            "No significant similarity detected."
        )


# ==========================================================
# COMPARE TWO PDF FILES
# ==========================================================

def compare_pdf_files(
    pdf1_path,
    pdf2_path
):

    text1 = extract_text_from_pdf(
        pdf1_path
    )

    text2 = extract_text_from_pdf(
        pdf2_path
    )

    if not text1 or not text2:

        return {
            "similarity": 0,
            "level": "Unavailable",
            "message": (
                "Could not extract text "
                "from one or both PDFs."
            )
        }

    score = calculate_similarity(
        text1,
        text2
    )

    level, message = classify_similarity(
        score
    )

    return {
        "similarity": score,
        "level": level,
        "message": message
    }


# ==========================================================
# OLD TEXT-BASED FUNCTION
# ==========================================================

def check_submissions(
    text1,
    text2
):

    score = calculate_similarity(
        text1,
        text2
    )

    level, message = classify_similarity(
        score
    )

    return {
        "similarity": score,
        "level": level,
        "result": message
    }
