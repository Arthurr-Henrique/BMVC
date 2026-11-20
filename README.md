# Bmvc

## Trabalhando com o BMVC no BASH:

1. Executar o arquivo 'route.py', na raiz do projeto.

## Trabalhando com o BMVC no DOCKER:

1. $ docker build -t bmvci .
1. $ docker run -d -p 8080:8080 -v $(pwd):/bmeta bmvci

## Níveis do Projeto BMVC

* Nível 1 — Catálogo (`/catalogo`):** vitrine estática de hardware com CSS e JS (`catalogo.html`, `catalogo.css`, `catalogo.js`), filtro por categoria e troca de tema.

* Nível 2 — Hardware (`/hardware`):** CRUD completo de hardware com modelo (`app/models/hardware.py`), repositório (`app/models/hardware_repository.py`), persistência em `db/hardware.json` e view/estética/script próprios (`hardware.html`, `hardware.css`, `hardware.js`).