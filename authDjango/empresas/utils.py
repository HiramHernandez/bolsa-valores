def validate_post_empresa(values):
    message: str = ''
    message += "-Falta el campo name." if not 'name' in values else ''
    message +=  "-Falta el campo description." if not 'description' in values else ''
    message +=  "-Falta el campo simbolo." if not 'simbolo' in values else ''
    message +=  "-Falta el campo valores_mercado." if not 'valores_mercado' in values else ''
    return message


def simbol_is_accepted(simbol: str) -> bool:
    # Esta funcion devuel un boolena dependiendo si el simbo
    # es aceptado o no por la bolsa de Nueva York
    # Referecia: https://coachingconsortium.org/que-es-simbolo-bursatil/
    if not simbol.isalpha():
        return False
    return True if len(simbol) <= 4 else False