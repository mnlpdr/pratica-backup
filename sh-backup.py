# -*- coding: utf-8 -*-
import os
import shutil
import datetime



# Definindo as configurações do backup
# Capturando input do usuário para definir os caminhos de backup e origem
while True:
    backup_path = input("Digite o caminho completo para o diretório de backup: ")
    if not os.path.isdir(backup_path):
        print("O diretório de backup não existe. Tente novamente.")
    else:
        break

while True:
    source_path = input("Digite o caminho completo para o diretório de origem: ")
    if not os.path.isdir(source_path):
        print("O diretório de origem não existe. Tente novamente.")
    else:
        break

now = datetime.datetime.now()

# Criando diretório de backup se não existir
if not os.path.exists(backup_path):
    os.makedirs(backup_path)

# Função para fazer backup completo
def full_backup():
    # Criando nome do arquivo de backup com timestamp
    backup_file = "full_backup_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".zip"
    # Criando arquivo de backup
    shutil.make_archive(os.path.join(backup_path, backup_file), "zip", source_path)

# Função para fazer backup diário
def daily_backup():
    # Criando nome do arquivo de backup com timestamp
    backup_file = "daily_backup_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".zip"
    # Criando arquivo de backup
    shutil.make_archive(os.path.join(backup_path, backup_file), "zip", source_path)

# Função para fazer backup semanal
def weekly_backup():
    # Verificando se é domingo (0 é domingo na função weekday())
    if now.weekday() == 0:
        # Criando nome do arquivo de backup com timestamp
        backup_file = "weekly_backup_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".zip"
        # Criando arquivo de backup
        shutil.make_archive(os.path.join(backup_path, backup_file), "zip", source_path)

# Função para fazer backup mensal
def monthly_backup():
    # Verificando se é o primeiro dia do mês
    if now.day == 1:
        # Criando nome do arquivo de backup com timestamp
        backup_file = "monthly_backup_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".zip"
        # Criando arquivo de backup
        shutil.make_archive(os.path.join(backup_path, backup_file), "zip", source_path)

# Função para fazer backup incremental
def incremental_backup():
    # Verificando se existe backup completo
    full_backups = [f for f in os.listdir(backup_path) if f.startswith("full_backup")]
    if len(full_backups) > 0:
        # Obtendo nome do último backup completo
        last_full_backup = max(full_backups)
        # Criando nome do arquivo de backup incremental com timestamp
        backup_file = "incremental_backup_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".zip"
        # Criando arquivo de backup
        shutil.make_archive(os.path.join(backup_path, backup_file), "zip", source_path, os.path.join(backup_path, last_full_backup))
    else:
        print("Não há backup completo para fazer backup incremental.")

# Função para fazer backup diferencial
def differential_backup():
    # Verificando se existe backup completo
    full_backups = [f for f in os.listdir(backup_path) if f.startswith("full_backup")]
    if len(full_backups) > 0:
        # Obtendo nome do último backup completo
        last_full_backup = max(full_backups)
        # Verificando se já foi feito backup diferencial antes
        diff_backups = [f for f in os.listdir(backup_path) if f.startswith("differential_backup")]
        if len(diff_backups) > 0:
                # Obtendo nome do último backup diferencial
                last_diff_backup = max(diff_backups)
                # Criando nome do arquivo de backup diferencial com timestamp
                backup_file = "differential_backup_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".zip"
                # Criando arquivo de backup
                shutil.make_archive(os.path.join(backup_path, backup_file), "zip", source_path, os.path.join(backup_path, last_diff_backup))
        else:
                # Criando nome do arquivo de backup diferencial com timestamp
                backup_file = "differential_backup_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".zip"
                # Criando arquivo de backup
                shutil.make_archive(os.path.join(backup_path, backup_file), "zip", source_path, os.path.join(backup_path, last_full_backup))
    else:
        print("Não há backup completo para fazer backup diferencial.")

# Função para mostrar as opções e executar backup escolhido
def menu():
    print("Escolha uma opção de backup:")
    print("1. Backup completo")
    print("2. Backup diário")
    print("3. Backup semanal")
    print("4. Backup mensal")
    print("5. Backup incremental")
    print("6. Backup diferencial")
    option = input("Opção: ")
    if option == "1":
        full_backup()
    elif option == "2":
        daily_backup()
    elif option == "3":
        weekly_backup()
    elif option == "4":
        monthly_backup()
    elif option == "5":
        incremental_backup()
    elif option == "6":
        differential_backup()
    else:
        print("Opção inválida.")
        menu()

# Executando o menu
menu()
