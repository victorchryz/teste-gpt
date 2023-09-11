#!/usr/bin/env python
"""Utilitário de linha de comando do Django para tarefas administrativas."""
import os
import sys


def main():
    """Execute tarefas administrativas."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            """
            Não foi possível importar o Django. 
            Tem certeza de que está instalado e disponível na sua variável de ambiente PYTHONPATH? 
            Você não esqueceu de ativar o ambiente virtual?
            """
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
