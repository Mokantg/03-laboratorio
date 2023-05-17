habitantes1 = 1556805
habitantes2 = 828708
superficie1 = 23890
superficie2 = 48583


censo2017 = {
    'ID': {8, 10},
    'Nombre': {'BioBío', 'Los Lagos'},
    'Superficie (km2)': {superficie1, superficie2},
    'Habitantes (2017)': {habitantes1, habitantes2}
}


print('Censo del 2017:\n',censo2017)

densidad1 = habitantes1/superficie1
densidad2 = habitantes2/superficie2


censo2017 = {
    'ID': {8, 10},
    'Nombre': {'BioBío', 'Los Lagos'},
    'Superficie (km2)': {23890, 48583},
    'Habitantes (2017)': {1556805, 828708},
    'Densidad Region de BioBío': densidad1,
    'Densidad Region de Los Lagos': densidad2
}

print(censo2017)


