def count_nested_levels(nested_documents, target_document_id, level=1):
    for doc in nested_documents:
        if doc == target_document_id:
            return level
        elif nested_documents[doc]:
            found_level = count_nested_levels(nested_documents[doc], target_document_id, level + 1)  
            if found_level != -1:
                return found_level
    return -1
