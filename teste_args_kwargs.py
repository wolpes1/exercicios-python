def args_teste(*args):
    for arg in args:
        print(f'A posição {args.index(arg)} contem: {arg}')

lista = ['a','b','c','d']

print(args_teste(*lista))