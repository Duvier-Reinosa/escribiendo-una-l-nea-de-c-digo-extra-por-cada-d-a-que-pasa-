import random
versos = [ "La luna brilla sobre el mar sereno",
        "Las estrellas cantan en el cielo pleno.", "Un susurro del viento trae un secreto,",
        "El alma danza al ritmo del soneto.", "Cada hoja cae con su propia historia,",
        "El río fluye, llevando su memoria.", "En la noche oscura, un sueño despierta,",
        "La vida es un viaje de puerta en puerta.", "En cada rincón, la magia es sembrada."
    ]
poema = "\n".join(random.sample(versos,4))
print("Aquí tienes tu poema: \n")
print(poema)