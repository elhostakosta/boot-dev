def restore_documents(originals, backups):
    return set(filter(lambda x: not x.isdigit(), list(map(lambda x: x.upper(), (list(originals) + list(backups))))))
