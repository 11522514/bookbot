def number_words(string):
    return len(string.split())

def character_count(string):
    counts = {}
    for character in string:
        if character.lower() in counts:
            counts[character.lower()] += 1
        else:
            counts[character.lower()] = 1
    return counts

def sort_by(dict):
    return dict["count"]

def sort_dictionary(dict):
    sorted_character_counts = []
    for character, count in dict.items():
        if character.isalpha():
            sorted_character_counts.append({"character": character, "count": count})
    sorted_character_counts.sort(reverse=True, key=sort_by)
    return sorted_character_counts
    