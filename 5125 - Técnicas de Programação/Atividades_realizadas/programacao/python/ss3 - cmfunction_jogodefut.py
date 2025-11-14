def jogo(equipe_casa, equipe_fora, golos_casa, golos_fora):
    print("\n","*" * 20, "Jogo","*" * 20)
    print(f"Nome da Equipa da Casa: {equipe_casa}")
    print(f"Nome da Equipa de Fora: {equipe_fora}")
    print(f"Golos equipe casa: {golos_casa}")
    print(f"Golos equipe fora: {golos_fora}")
    print("\n","-" * 20, "Resultado","-" * 20)

    if (golos_casa > golos_fora):
        return(f"A equipe da casa venceu por: \n{equipe_casa} | {golos_casa} x {golos_fora} | {equipe_fora}")
    elif (golos_casa < golos_fora):
        return(f"A equipe de fora venceu por: \n{equipe_fora} | {golos_fora} x {golos_casa} | {equipe_casa}")
    else:
        return(f"O jogo empatou em: \n{equipe_casa}| {golos_casa} x {golos_fora} |{equipe_fora}")
    

print(jogo("Benfica", "Porto", 2, 1))
print("\n","*" * 20, "Jogo","*" * 20)