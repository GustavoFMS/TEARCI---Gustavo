print("\n","*" * 20, "Jogo","*" * 20)

equipe_casa = str(input("Nome da Equipa da Casa: \n→ "))
equipe_fora = str(input("Nome da Equipa de Fora: \n→ "))
golos_casa = int(input("Golos equipe casa: \n→ "))
golos_fora = int(input("Golos equipe fora: \n→ "))
print("\n","-" * 20, "Resultado","-" * 20)

if (golos_casa > golos_fora):
    print(f"A equipe da casa venceu por: \n{equipe_casa} | {golos_casa} x {golos_fora} | {equipe_fora}")
elif (golos_casa < golos_fora):
    print(f"A equipe de fora venceu por: \n{equipe_fora} | {golos_fora} x {golos_casa} | {equipe_casa}")
else:
    print(f"O jogo empatou em: \n{equipe_casa}| {golos_casa} x {golos_fora} |{equipe_fora}")

print("\n","*" * 20, "Jogo","*" * 20)