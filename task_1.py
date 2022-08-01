def hash_string(s, alg_type):
    """Hash string"""

    s_encoded = alg_type(s.encode('utf-8')).hexdigest()
    return s_encoded
