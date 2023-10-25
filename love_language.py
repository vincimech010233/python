from preloaded import LOVE_LANGUAGES

def love_language(partner, weeks):
    # Inicializa un diccionario para contar las respuestas positivas de cada lenguaje de amor
    positive_responses = {language: 0 for language in LOVE_LANGUAGES}
    # Calcula el total de días
    total_days = weeks * 7
    for day in range(total_days):
        # Circula a través de los lenguajes de amor en orden
        language = LOVE_LANGUAGES[day % len(LOVE_LANGUAGES)]
        # Prueba el lenguaje de amor en tu pareja
        response = partner.response(language)
        # Si la respuesta es positiva, incrementa el contador para ese lenguaje de amor
        if response == "positive":
            positive_responses[language] += 1
    # Encuentra el lenguaje de amor con el mayor número de respuestas positivas
    main_love_language = max(positive_responses, key=positive_responses.get)
    return main_love_language
