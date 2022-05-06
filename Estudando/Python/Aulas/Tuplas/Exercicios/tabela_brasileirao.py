times = ('Corinthians', 'Bragantino', 'Atletico-MG',
         'Coritiba', 'Sao Paulo', 'Santos',
         'Cuiaba', 'Internacional', 'Avai',
         'America-MG', 'Palmeiras', 'Flamengo',
         'Botafogo', 'Fluminense', 'Ceara SC',
         'Athletico-PR', 'Atletico-GO', 'Goias',
         'Juventude', 'Fortaleza')
print(times[:5])
print('-='*15)
print(times[-4:])
print('-='*15)
print(sorted(times))
print('-='*15)
print(f' O Santos esta na {times.index("Santos") + 1} posicao')
