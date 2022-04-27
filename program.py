from num2words import num2words

print('=-'*15)
numero = int( input('Digite um número: ') )
print('=-'*15)
# --------- Portugues Brasileiro
print('\033[32mPortuguês:\033[m')
num_ptbr = num2words(numero, lang='pt-br')
print(f'número: \033[33m{num_ptbr}\033[m')

num_ptbr_ord = num2words(numero, lang='pt-br', to='ordinal')
print(f'número ordinal: \033[33m{num_ptbr_ord}\033[m\n')

# --------- English
print('\033[32mEnglish:\033[m')
num_en = num2words(numero, lang='en')
print(f'número: \033[33m{num_en}\033[m')

num_en_ord = num2words(numero, lang='en', to='ordinal')
print(f'número ordinal: \033[33m{num_en_ord}\033[m\n')

# --------- Francês
print('\033[32mFrancês:\033[m')
num_fr = num2words(numero, lang='fr')
print(f'número: \033[33m{num_fr}\033[m')

num_fr_ord = num2words(numero, lang='fr', to='ordinal')
print(f'número ordinal: \033[33m{num_fr_ord}\033[m\n')

# --------- Español
print('\033[32mEspañol:\033[m')
num_es = num2words(numero, lang='es')
print(f'número: \033[33m{num_es}\033[m')

num_es_ord = num2words(numero, lang='es', to='ordinal')
print(f'número ordinal: \033[33m{num_es_ord}\033[m\n')
