import celue
import inspect


def best_promo2(order):
    promos = [func for name, func in inspect.getmembers(celue, inspect.isfunction) if name.endswith('promo')]
    return max(promo(order) for promo in promos)

if __name__ == '__main__':
    joe = celue.Customer('John Doe', 0)
    ann = celue.Customer('Ann Smith', 1100)
    cart = [celue.LineItem('banana', 4, .5),
            celue.LineItem('apple', 10, 1.5),
            celue.LineItem('watermellon', 5, 5.0)
            ]
    print celue.Order(joe, cart, celue.FidelityPromo())
    print celue.Order2(joe, cart, celue.fidelity_promo)
    print
    long_order = [celue.LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    print celue.Order2(joe, long_order,celue.fidelity_promo)
    print celue.Order2(joe, long_order,celue.bulk_item_promo)
    print celue.Order2(joe, long_order,celue.large_order_promo)
    print celue.Order2(joe,long_order,best_promo2)
    print
    promos = [name for name, func in inspect.getmembers(celue, inspect.isclass) if name.endswith('Promo')]
    count = []
    for promo in promos:
        count.append(celue.Order(joe, long_order, getattr(celue, promos[2])()))
    print max(count)