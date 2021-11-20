def as_source_file(attribute_info: dict) -> dict:
    result = attribute_info.copy()
    result['name_index'] = int.from_bytes(attribute_info['info'], "big")
    return result
