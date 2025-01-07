import random


o_botequim_da_francisca = {
    "Restaurante":"O botequim da francisca",
    "Bairro": "Vila Independencia",
    "R.":"Francisca de Queiroz",
    "numero":"125",
}

oca_burguer_mangal = {
    "Restaurante":"Oca Burguer Mangal",
    "Bairro":"Vila Leão",
    "R.":"Gustavo Teixeira",
    "numero":"325",
}

tammy_pastelaria = {
    "Restaurante":"Tammy Pastelaria",
    "Bairro":"Jardim Simus",
    "Av.":"Afonso Vergueiro",
    "numero":"76",
}

mc_donald_campolim = {
    "Restaurante":"McDonald's (Sor)Campolim",
    "Bairro": "Campolim",
    "Av.":"Antonio Carlos Comitre",
    "numero":"1055",
}

pana = {
    "Restaurante":"Panacita Empanadas",
    "Bairro": "Vila Independencia",
    "R.":" Francisca de Queiroz",
    "numero":"97",
}

edson_lanches = {
    "Restaurante":"Edson Lanches",
    "Bairro":"Vila Jardine",
    "R.":"Visc. do Rio Branco",
    "numero":"1014",
}

cucina_del_capo = {
    "Restaurante":"Cucina Del Capo",
    "Bairro":"Vila Jardine",
    "R.":"Francisca de Queiroz",
    "numero":"43",
}

mansour = {
    "Restaurante":"Mansour Arabe",
    "Bairro":"Vila Florinda",
    "R.":"Dr. Francisco Preste Maia",
    "numero":"486",
}

dr_pastel = {
    "Restaurante":"Dr. Pastel",
    "Bairro":"Centro",
    "R.":"da Penha",
    "numero":"1376",
}

dicionario = [dr_pastel, mansour, cucina_del_capo, edson_lanches, o_botequim_da_francisca, oca_burguer_mangal, tammy_pastelaria, mc_donald_campolim, pana]
restaurante = random.choice(dicionario)
for i in restaurante.items():
    print(i)


