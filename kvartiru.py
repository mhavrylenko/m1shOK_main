target_flat = 144
flats_per_floor = 6
floors = 9


def poisk(target_flat, flats_per_floor, floors):
    target_floor = floors * flats_per_floor // target_flat + 1
    a = target_flat // flats_per_floor + 1
    target_porch = a // floors + 1
    return print('Kvartira #', target_flat, 'nahoditsya v podezde #', target_porch, 'na', target_floor, 'etazhe')

print(poisk(16, 3, 5))