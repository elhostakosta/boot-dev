def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception("not enough gold")
    else:
        gold_available -= price
        return gold_available
