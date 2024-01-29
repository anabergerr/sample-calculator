def sample_calculator():
    population_size = int(input("Digite o número total de pessoas: "))
    confidence_level = input("nivel de confiança? ")
    margin_error = (
        float(input("Qual margem de erro? ")) / 100
    )  # Convertido para decimal
    z_score = 0
    z_scores_dict = {"80": 1.28, "85": 1.44, "90": 1.65, "95": 1.96, "99": 2.58}

    for score in z_scores_dict:
        if score == confidence_level:
            z_score = z_scores_dict[score]

    result = (z_score**2 * 0.25) / (margin_error**2)

    # Ajuste para população finita
    result = (result * population_size) / (result + population_size - 1)
    print(round(result))


sample_calculator()
