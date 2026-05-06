import shelve

inventario_actual = {'espada': 1, 'pociones': 5, 'oro': 150}

partida = shelve.open('partida_guardada')
partida['inventario_jugador'] = inventario_actual
partida.close()

partida_flechas = shelve.open('partida_guardada')
mi_inventario = partida_flechas['inventario_jugador']
# flechas = mi_inventario.get['flechas']
# flechas = get(mi_inventario['flechas'], 0)
flechas = mi_inventario.get('flechas', 0)