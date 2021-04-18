def format_float_str_moeda(valor: float) -> str:  # formatacao para apresentacao do numero com a virgula
    return f'R$ {valor: ,.2f}'                    # ao inves do ponto