# Word Frequency Counter

Este código es parte de la prueba de cart.com, elaborada por **Guillermo Steve Albo Muñíz**. Fue probado en **Python 3.9.0**. El script `word_frequency.py` cuenta la frecuencia de cada palabra en un archivo de texto. Ignora puntuación, números y normaliza mayúsculas/minúsculas. Las palabras y sus frecuencias se imprimen en orden descendente de frecuencia así mismo de manera alfabética. Para ejecutar el script, usa el comando `python word_frequency.py <file_path>`, donde `<file_path>` es la ruta al archivo de texto que deseas analizar.

El script fue probado con los siguientes archivos de texto: `sample.txt` con el contenido "This is a test. This test is only a test." y el resultado esperado es "test: 3, a: 2, is: 2, This: 2, only: 1". Y `sample_2.txt` con el contenido "Apple apple banana 123 BANANA orange ORANGE apple. 35424 Apple! ORANGE, banana." y el resultado esperado es "Apple: 4, banana: 3, ORANGE: 3".

El script produce los siguientes resultados: para `sample.txt` - "test: 3, a: 2, is: 2, This: 2, only: 1", y para `sample_2.txt` - "Apple: 4, banana: 3, ORANGE: 3".

El script ignora los números y la puntuación y mayúsculas/minúsculas. Para clonar el repositorio, usa `git clone https://github.com/memosteve/cart.com_test.git`, navega al directorio del proyecto con `cd cart.com_test` y ejecuta el script con uno de los archivos de muestra. Este proyecto fue elaborado por Guillermo Steve Albo Muñíz.
