# Flask API - Estrutura Base para Projetos 🧱

Repositório dedicado a exemplificar e facilitar o início de projetos Flask para APIs 💫. Clone e inicie seus próprios desenvolvimentos com facilidade 🚀.

##### Estrutura Organizada e Escalavel. 😎📱

### Estrutura
<img width="221" alt="2024-03-09_17h53_25" src="https://github.com/piedro404/flask-api-structure/assets/88720549/a824cb03-38d1-4173-b7c9-5eab764e333a">

#### Detalhes
- Controllers: Contém os controladores que gerenciam a lógica da aplicação, conectando as rotas às operações específicas.
- Drivers: Armazena os drivers e bibliotecas necessários para conectar e operar com outros serviços ou hardware.
- Errors: Define tipos específicos de erros e exceções personalizadas que podem ser acionadas durante a execução do código.
- Main: É o ponto de entrada principal do aplicativo. Dentro desta pasta, “Routes” gerencia as rotas da API e “Server” é responsável por iniciar e gerenciar o servidor web.
- Models: Contém os modelos de dados, geralmente classes que representam as tabelas no banco de dados.
- Static: Armazena arquivos estáticos como CSS, JS, imagens, etc., que são necessários para renderizar páginas web front-end.
- Templates: Mantém templates HTML e documentação relacionada à estrutura ou uso da API.
- Validators: Inclui scripts ou módulos para validar dados de entrada ou requisições à API.
- Views: Define diferentes tipos de respostas HTTP e views associadas à lógica da apresentação.

# Recursos da Estrutura da API 🔨
- Home: Dá as suas Boas-Vindas e traz informações relevantes sobre a API e Contatos.
- Docs: Local para aprender sobre a API e como utilizar de forma interativa e dinâmica.
- Favicon.icon: Icone para ser apresentado e visualizado na janela do Web Site.

# Principais Tecnologias Utilizadas 🌐
- Flask: Framework utilizado para o desenvolvimento de aplicações web, proporcionando uma estrutura flexível e eficiente para a criação de APIs e interfaces de usuário.
- Python: Linguagem de programação principal, escolhida pela sua versatilidade, simplicidade e vasta comunidade de desenvolvedores.
- Cerberus: Biblioteca de validação de dados em Python, empregada para garantir a integridade e consistência dos dados manipulados pela aplicação.
- Outras Bibliotecas: O resto das bibliotecas pode ser encontradas no requirements.txt, incluindo diversas ferramentas e utilitários que complementam e aprimoram as funcionalidades da aplicação.

# Documentação 📃

### API:
Uma API (Interface de Programação de Aplicações) é um conjunto de regras e definições que permite a comunicação entre diferentes softwares. Ela possibilita que aplicações e serviços troquem informações e funcionalidades de forma eficiente e padronizada.

### Principais Usos no Desenvolvimento:
1. Integração de Serviços:
As APIs facilitam a integração entre diferentes serviços e plataformas, permitindo que aplicativos compartilhem dados e funcionalidades.
2. Desenvolvimento de Aplicações Móveis:
APIs são fundamentais para o desenvolvimento de aplicativos móveis, permitindo acesso a recursos como localização, câmera, notificações, entre outros.
3. Acesso a Dados Externos:
Utilizadas para obter dados de fontes externas, como redes sociais, bancos de dados, serviços de terceiros, proporcionando informações atualizadas.
4. Integração com Plataformas Web:
APIs são cruciais para a integração de aplicações web, possibilitando a comunicação eficiente entre o front-end e o back-end.
5. Desenvolvimento de Microsserviços:
Em arquiteturas de microsserviços, as APIs são essenciais para a comunicação entre os diversos componentes distribuídos de uma aplicação.
6. Automatização de Tarefas:
APIs permitem a automatização de tarefas rotineiras, otimizando processos e melhorando a eficiência operacional.
7. Desenvolvimento de Plugins e Extensões:
São utilizadas para criar plugins e extensões em diversas plataformas, ampliando as funcionalidades de softwares existentes.
8. Economia de Recursos:
Facilitam o desenvolvimento ao permitir o reuso de funcionalidades já implementadas, economizando tempo e recursos.

## Como usar 💁‍♀️
1. Rota Principal ("/"): Retorna um Template que renderiza a Documentação Swagger. <br>(http://127.0.0.1:3000)
<img width="930" alt="2024-03-09_18h21_55" src="https://github.com/piedro404/flask-api-structure/assets/88720549/e7f8d813-f624-48d7-8cb8-fcf0be04e89f">
   
2. Rota Informações da API ("/info"): Retorna um JSON com informações sobre a API. <br>(http://127.0.0.1:3000/info)

```bash
{
    "status": True,
    "message": "Welcome to the Structure Flask API!",
    "version": "1.0v",
    "endpoints": {
        "docs": "/",
        "info": "/info",
    },
    "documentation": "/",
    "contact": {
        "email_personal": "pedro.henrique.martins404@gmail.com",
        "email_academic": "pedro.borges@alu.unibalsas.edu.br",
        "github": "piedro404",
        "linkedin": "pedrohenrique404"
    }
}
```

# Como Executar o Projeto Localmente 🛠️
1. Clone este repositório:
   
```bash
   git clone https://github.com/piedro404/flask-api-structure.git
```

2. Ambiente Virtualizado (Opcional)
Para organização e facilitar em rodar o projeto, sugiro criar um ambiente virtualizado. Para isso, basta usar o comando abaixo:
```Bash
  python -m venv .venv
```
```Bash
  .venv\Scripts\activate
```

3. Instale as dependências: 

```bash
   pip install -r requirements.txt
```
   
4. Execute a aplicação: 

```bash
   python run.py
```

# Sobre 📒
Obrigado a todos, desejo ótimos estudos, caso queira, entre em contato em pedro.henrique.martins404@gmail.com;
