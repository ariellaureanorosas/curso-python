"""
================================================================================
TUDO SOBRE IMPORTAÇÃO EM PYTHON – GUIA COMPLETO E BOAS PRÁTICAS
================================================================================
Este arquivo é um "guia vivo" sobre módulos, pacotes, __init__, __main__,
imports relativos/absolutos, circular imports, boas práticas e más práticas.
Copie e cole no VS Code, leia com calma e use como referência diária.

O código é didático: muitos trechos estão comentados porque simulam arquivos
que não existem em disco. O objetivo é você entender os mecanismos, não executar
tudo de uma vez.
"""

# ==============================================================================
# 1. MÓDULOS
# ==============================================================================
# Módulo é qualquer arquivo .py. O nome do módulo é o nome do arquivo sem .py.
# Exemplo: arquivo "calculadora.py" → módulo "calculadora"

# --- import simples ---
# import calculadora          # importa o módulo inteiro
# calculadora.soma(2, 3)      # usa função prefixada

# --- import com alias (apelido) ---
# import calculadora as calc
# calc.subtrai(5, 2)

# --- from ... import ... (importa nomes específicos para o namespace atual) ---
# from calculadora import soma, PI
# print(soma(1, 2))            # não precisa de prefixo
# print(PI)

# --- from ... import * (importa TUDO que está no namespace do módulo) ---
# from calculadora import *    # EVITE! (ver más práticas)
# print(multiplica(3, 4))

# ==============================================================================
# 2. PACOTES (packages)
# ==============================================================================
# Pacote é um diretório que contém um arquivo especial __init__.py.
# Ele pode conter outros módulos e subpacotes.
#
# Estrutura de exemplo:
# meu_pacote/
# ├── __init__.py
# ├── modulo_a.py
# ├── modulo_b.py
# └── sub_pacote/
#     ├── __init__.py
#     └── modulo_c.py
#
# Para usar:
# import meu_pacote.modulo_a
# from meu_pacote import modulo_b
# from meu_pacote.sub_pacote import modulo_c

# ==============================================================================
# 3. O ARQUIVO __init__.py
# ==============================================================================
# - Torna o diretório um pacote Python.
# - Pode estar vazio.
# - É executado na primeira vez que o pacote (ou algo dentro dele) é importado.
# - Pode definir a variável especial __all__ (lista de strings) para controlar
#   o que é exportado quando alguém faz "from pacote import *".
# - Pode expor nomes do submódulos para facilitar o acesso:
#   Exemplo: no __init__.py de 'meu_pacote':
#       from .modulo_a import funcao_principal
#   Agora o usuário faz: from meu_pacote import funcao_principal

# Demonstração (comentada, pois não temos o diretório real):
# Suponha que meu_pacote/__init__.py contenha:
#   __all__ = ['modulo_a', 'funcao_principal']
#   from .modulo_a import funcao_principal
#
# Agora:
# from meu_pacote import *     # importa apenas modulo_a e funcao_principal

# ==============================================================================
# 4. __main__ – O PONTO DE ENTRADA
# ==============================================================================
# Quando um arquivo .py é executado diretamente (python arquivo.py),
# a variável especial __name__ recebe o valor "__main__".
# Quando é importado como módulo, __name__ recebe o nome do módulo.
# Isso permite separar código que só deve rodar na execução direta.

print(f"Nome deste módulo quando executado ou importado: {__name__}")

# --- Exemplo clássico ---
if __name__ == "__main__":
    # Este bloco só roda se este arquivo for o script principal.
    print("Rodando como script principal!")
else:
    # Este bloco roda quando o arquivo é importado como módulo.
    print("Importado como módulo.")

# ==============================================================================
# 5. IMPORTS ABSOLUTOS vs RELATIVOS
# ==============================================================================
# Absoluto: caminho completo a partir da raiz do projeto (sys.path).
#   from meu_pacote.modulo_a import funcao
# Relativo: usa . (diretório atual), .. (diretório pai), etc.
#   from . import modulo_a          # importa modulo_a do mesmo pacote
#   from .modulo_a import funcao
#   from .. import pacote_irmao     # sobe um nível

# IMPORTANTE: imports relativos só funcionam DENTRO de pacotes (arquivos que
# estão em um diretório com __init__.py). Fora de um pacote, você deve usar
# imports absolutos.

# Quando usar relativo vs absoluto?
# - Relativos: para referências internas ao próprio pacote, tornando o pacote
#   independente do nome da pasta raiz.
# - Absolutos: recomendado para scripts fora do pacote e para maior clareza.
# Ambos são aceitáveis, mas a comunidade tende a preferir imports absolutos.

# Exemplo (suponha que você esteja dentro de meu_pacote/sub_pacote/modulo_c.py):
# from ..modulo_a import funcao   # sobe um nível (sub_pacote -> meu_pacote)
#                                  # e importa funcao de modulo_a

# ==============================================================================
# 6. CIRCULAR IMPORTS (importação circular) – PROBLEMA E SOLUÇÃO
# ==============================================================================
# Ocorre quando dois módulos tentam importar um ao outro.
# Exemplo:
#   arquivo a.py:
#       from b import algo
#   arquivo b.py:
#       from a import outra_coisa
#
# Isso pode causar AttributeError ou ImportError porque um dos módulos ainda
# não foi completamente carregado.
#
# Soluções:
# a) Refatorar para evitar a dependência circular (quase sempre o ideal).
# b) Mover o import para dentro da função (import local) – só resolve se a
#    função não for chamada durante a importação.
# c) Importar o módulo inteiro em vez de nomes específicos:
#       import b   (e depois b.algo)
#    Isso quebra a necessidade de ter os nomes no momento da importação.

# Exemplo de solução com import local:
# def funcao_que_precisa_de_b():
#     from b import algo   # 'b' só é importado quando a função é chamada
#     return algo()

# ==============================================================================
# 7. BOAS PRÁTICAS DE IMPORTAÇÃO
# ==============================================================================

# 7.1 ordene os imports
#    a) bibliotecas padrão (os, sys, json...)
#    b) bibliotecas de terceiros (requests, numpy, pandas...)
#    c) imports locais (do seu projeto)
import os
import sys

# import requests   # terceiro (exemplo)
# from meu_pacote import modulo_a  # local

# 7.2 use imports explícitos (nunca "from modulo import *")
# Bom:
# from math import sqrt, pi
# Ruim:
# from math import *   # polui o namespace, difícil de debugar

# 7.3 prefira importar o módulo ou nomes específicos, evite carregar tudo
# Bom:
import json

dados = json.loads("{}")
# Também bom:
from json import loads, dumps

# 7.4 não coloque código com efeitos colaterais no escopo do módulo (fora de funções)
# Isso inclui: print(), abertura de arquivos, conexões de rede, etc.
# A não ser que estejam protegidos por "if __name__ == '__main__':".

# 7.5 use alias com significado claro
import numpy as np
import pandas as pd

# Evite aliases obscuros ou sem contexto.

# 7.6 defina __all__ em seus pacotes/__init__.py para explicitar a API pública.
# Exemplo (dentro de __init__.py):
# __all__ = ['ClassePublica', 'funcao_util']

# 7.7 mantenha os imports no topo do arquivo (PEP 8)
# Só use imports dentro de funções se houver um motivo muito forte
# (ex.: evitar circular import, import condicional por plataforma, late binding).

# 7.8 evite manipular sys.path diretamente
# Em vez de sys.path.insert(0, '/caminho/qualquer'), prefira:
#   - Instalar o pacote em modo de desenvolvimento (pip install -e .)
#   - Definir a variável de ambiente PYTHONPATH
#   - Estruturar o projeto com um diretório src e setup.py/pyproject.toml

# 7.9 use if __name__ == "__main__" para código executável
# Isso permite que o módulo seja importado sem rodar scripts, testes ou demos.

# 7.10 não crie __init__.py gigantes
# O __init__.py pode expor uma API simplificada, mas a lógica deve ficar nos módulos.

# ==============================================================================
# 8. MÁS PRÁTICAS (EVITE!)
# ==============================================================================

# 8.1 Wildcard import (from modulo import *)
#    Polui o namespace, dificulta leitura, pode sobrescrever nomes sem aviso.
#    Além disso, ignora o __all__ se o módulo não o definir.

# 8.2 Circular imports (já explicado).

# 8.3 Modificar sys.path de forma descontrolada
# sys.path.append('..')  # frágil, dependente do diretório de execução

# 8.4 Executar lógica pesada ou com efeitos colaterais no escopo do módulo
# Exemplo: abrir um arquivo, baixar dados da internet, conectar a um banco,
#          tudo fora de funções e sem proteção do __main__.

# 8.5 Importar módulos que não são usados (polui o código, atrapalha linters)

# 8.6 Criar dependências cíclicas entre __init__.py e seus submódulos
#    Exemplo: __init__.py importa modulo_a, e modulo_a importa algo do __init__
#    Isso facilmente gera circular import.

# 8.7 Usar import * dentro de __init__.py para "exportar tudo"
#    Melhor: definir __all__ ou importar seletivamente.

# 8.8 Sombrear built-ins (não crie um módulo chamado "math.py" se você também
#    usa "import math", pois Python pode importar seu módulo local e não o built-in).

# 8.9 Importar dentro de funções sem necessidade real
#    Só faça se for resolver um problema comprovado de circular import ou
#    para evitar carregar módulos pesados desnecessariamente (lazy loading).

# 8.10 Nomes de módulos/pacotes com hífen ou começando com número.
#     Python não permite importar nomes com hífen, e nomes numéricos são inválidos.

# ==============================================================================
# 9. DICAS EXTRAS DO DIA A DIA
# ==============================================================================

# - Use "import this" no interpretador para ver o Zen do Python.
# - Para recarregar um módulo sem reiniciar o kernel (útil em desenvolvimento):
#   from importlib import reload
#   reload(meu_modulo)

# - Ferramentas como isort e black ajudam a organizar imports automaticamente.
#   Exemplo: pip install isort && isort meu_arquivo.py

# - Quando estiver debugando imports, verifique sys.path e o __file__ do módulo:
# import meu_modulo
# print(meu_modulo.__file__)  # mostra o caminho absoluto de onde foi carregado

# - Para criar um pacote instalável, estude setuptools e pyproject.toml.
#   Isso elimina a necessidade de manipular sys.path e torna o projeto portável.

# ==============================================================================
# EXEMPLO COMPLETO SIMULANDO UM MINI PROJETO (comentado)
# ==============================================================================
# Suponha esta estrutura de diretório:
# projeto/
# ├── main.py
# └── utils/
#     ├── __init__.py
#     ├── strings.py
#     └── numeros.py
#
# Conteúdo de utils/__init__.py:
#   __all__ = ['strings', 'numeros']
#   from .strings import inverter
#
# Conteúdo de utils/strings.py:
#   def inverter(texto):
#       return texto[::-1]
#
# Conteúdo de utils/numeros.py:
#   def dobro(n):
#       return n * 2
#
# Conteúdo de main.py:
#   from utils import inverter
#   from utils.numeros import dobro
#   print(inverter("python"))  # nohtyp
#   print(dobro(21))           # 42
#
# Para rodar: python main.py (estando na pasta projeto)

# FIM DO GUIA – Agora é com você! Revise, pratique e compartilhe.
