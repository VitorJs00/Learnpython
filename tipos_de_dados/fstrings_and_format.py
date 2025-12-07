text = 'Texto teste'
numero = 2.4444
print(f"olha como {text} fica bem demais e {numero:.2f}")
string = 'texto={} num=numero={:.1f}'
print(" {text}  {numero:.4f}".format(text=text,numero=numero))
print(string.format(text,numero))