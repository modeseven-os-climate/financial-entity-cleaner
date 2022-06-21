cleaning_rules_dict = {
    "remove_email": [" ", "\S*@\S*\s?"],
    "remove_url": [" ", "https*\S+"],
    "remove_word_the_from_the_end": [" ", "the$"],
    "place_word_the_at_the_beginning": [" ", "the$"],
    "remove_www_address": [" ", "https?://[.\w]{3,}|www.[.\w]{3,}"],
    "enforce_single_space_between_words": [" ", "\s+"],
    "replace_amperstand_by_AND": [" and ", "&"],
    "replace_amperstand_between_space_by_AND": [" and ", "\s+&\s+"],
    "replace_hyphen_by_space": [" ", "-"],
    "replace_hyphen_between_spaces_by_single_space": [" ", "\s+-\s+"],
    "replace_underscore_by_space": [" ", "_"],
    "replace_underscore_between_spaces_by_single_space": [" ", "\s+_\s+"],
    "remove_all_punctuation": [" ", "([^\w\s])"],
    "remove_punctuation_except_dot": [" ", "([^\w\s.])"],
    "remove_mentions": [" ", "@\S+"],
    "remove_hashtags": [" ", "#\S+"],
    "remove_numbers": [" ", "\w*\d+\w*"],
    "remove_text_puctuation": [" ", "\;|\:|\,|\.|\?|\!|\""],
    "remove_text_puctuation_except_dot": [" ", "\;|\:|\,|\?|\!|\""],
    "remove_math_symbols": [" ", "\+|\-|\*|\>|\<|\=|\%"],
    "remove_math_symbols_except_dash": [" ", "\+|\*|\>|\<|\=|\%"],
    "remove_parentheses": ["", "\(|\)"],
    "remove_brackets": ["", "\[|\]"],
    "remove_curly_brackets": ["", "\{|\}"],
    "remove_single_quote_next_character": [" ", "'\w+"],
    "remove_words_in_parentheses": [" ", "\([^()]*\)"],
    "repeat_remove_words_in_parentheses": [" ", "remove_words_in_parentheses"]
}

default_company_cleaning_rules = [
    "replace_amperstand_between_space_by_AND",
    "replace_hyphen_between_spaces_by_single_space",
    "replace_underscore_between_spaces_by_single_space",
    "remove_text_puctuation_except_dot",
    "remove_math_symbols",
    "remove_words_in_parentheses",
    "remove_parentheses",
    "remove_brackets",
    "remove_curly_brackets",
    "enforce_single_space_between_words"
]