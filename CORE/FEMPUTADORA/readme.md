# Femputadora

sistema de procesamiento de lenguaje natural (PLN).

# componenetes

- Tokenizer.
- Vocabulario.
- Sinónimos.
- Vectorizer.

# Tokenizer

Es una clase que se encarga de tomar un texto y dividirlo en palabras... solamente usando espacio.
"divide el texto en palabras (tokens) y separa caracteres especiales."

# Vocabulario

Es un diccionario que representa las dimensiones que puede soportar nuestro lenguaje. Cada dimension puede tomar un valor entre 0 y 1. Los valores son según "vocabulary_tokenizer_ids.py" y esta clase no es más que un dicionario del tipo:

key: value

Donde la "key" es una palabra la cual genera una dimensión en el arreglo.
Donde el "value" es un arreglo de números [0-1] los cuales van en un arreglo de tamaño según cuantas palabras tenga el vocabulario.

Los vectores de todos los tokens se suman (con saturación en 1) para obtener un vector final que representa la presencia de conceptos en el texto.

# Sinonimos

Es un diccionario que representa las palabras con igual significado que se encuentran en el "vocabulario".

Es un diccionario del tipo key, value en donde la "key" es una palabra que es exactamente la misma key del vocabulario y el value es un arreglo de string de todos los posibles sinonimos de una palabra... incluyendo concidencias comunes por mala ortografia.
