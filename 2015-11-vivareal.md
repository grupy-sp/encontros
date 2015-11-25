#[Palestras e slides do encontro do Grupy-SP em Novembro/2015](http://www.meetup.com/pt/Grupy-SP/events/226536272/)

### Agradecimento especial ao Arian, Camila, Brian e Robson, todos da [Vivareal](http://www.vivareal.com.br/) pelo espaço cedido e o coffee break.

###[20min] "MapEngine": Introspecção, Orientação a objetos radical e desenvolvimento rápido de jogos de alta jogabilidade com "meias dúzias" de linhas de código - João Bueno [JS]  

Aqui em Campinas estamos desenvolvendo o projeto JovemHacker, dição 2015 - http://jovemhacker.org/ - fiquei como instrutor do módulo de programação e orientador dos projetos finais. E de repetne, estava com 5 grupos de alunos, cada um querendo criar um jogo diferente como projeto final Há outros orientadores/monitores mas não são muito proeficientes em Python ou jogos. A solução? Criar um framework to handle then all!

Em desenvolvimento ativo neste momento, o "MapEngine" é um framework para desenvolvimento de jogos 2D complexos (tela com scroll, várias fazesm orientado a blocos) - cuja idéia é permitir a edição dos mapas das fases em editores de imagem normais, e um mínimo de codificação (de 1 a poucas dezenas de linhas) para cada tipode objeto com que há interação: o framework permite naturalmente jogos no estilo platformer (Mario, Alex Kid), side scrollers, mapas vistos de cima, tanto de ação quanto de RPG (adventure). 

A idéia da palestra é mostrar o mesmo em funcionamento,  o código minimo para jogos diferentes, e como as características de introspecção e O.O. do Python foram usadas para permitir isso,ter espaço para discutir algumas das idéias na mesa _e_ angariar novos colaboradores para o projeto :-)

Principal ponto fraco: o número de linhas para criar uma grande variedade de interação entre objetos é mínimo, mas exige um nível de programação e conhecimento de Python além do que pôde ser desenvolvido em 6 encontros do projeto - na verdade, exigem algum Python razoavlemente avançado. O que por outro lado, faz comq ue seja uma ferramenta bem legal para Pythonistas com algum jogo de cintura criarem seus próprios jogos. (ex.: 

(A propósito, eu mencionei que ele "está em desenvolvimento"?  Já é possível fazer bastante coisa, e espero que seja possível fazer ainda mais até o dia do encontro -

mas quem quiser olhar: http://github.com/jsbueno/mapengine

###[30min] [Palestra convidada Vivareal | Continuous Delivery - Giancarlo Rubio](https://github.com/gianrubio/grupy-CI)

###[20min] [Python-EVE - APIs REST profissionais em poucas linhas - Rudá Porto](http://pt.slideshare.net/rudaporto/python-eve-apis-restful-profissionais-em-poucas-linhas)

Desenvolvimento de APIs REST com framework EVE (http://python-eve.org/).

Esse framework utiliza o conceito de declaração de modelos de domínio que podem inclusive ser um Model SQLAlchemy (usando a extensão Eve-SQLAlchemy), para entregar automaticamente uma API REST CRUD completa e repleta de funcionalidades prontas com as melhores práticas.

Além disso é possível customizar a API globalmente ou por recursos a ser exposto, como por exemplo não ter autorização para as consultas GET ou ter uma classe de autorização por recursos, hooks de request, hooks de acesso a dados, etc.

A minha intenção é apresentar os recursos mais relevantes desse framework muito maduro para REST que possui uma abordagem muito interessante, incluindo integração nativa com MongoDB.

###[20min] Python para iniciantes focados para Web - Anderson Borges 

Nesta mini palestra mostrarei para os iniciantes  como podem utilizar  a linguagem python com foco na Web, a partir 

da abordagem de uso com Django, Wagtail , Debug de código utilizando PyCharm e Deployment.

Se você está iniciando em python e gostaria de entender mais o funcionamento , você está convidado a participar desta palestra.

###[20min] [Sobrecarga de Operadores em Python: um grande poder implica em grande responsabilidade. - Paulo Scardine](http://nbviewer.ipython.org/github/scardine/palestra-grupy-2015-11/blob/master/Sobrecarga-de-operadores-em-Python.ipynb)

Um usuário do [stackoverflow perguntou se era possível implementar a sintaxe "infix" da linguagem R em Python](http://stackoverflow.com/questions/33658355/piping-output-from-one-function-to-another-using-python-infix-syntax):


    df = df | select('one') | rename(one = 'new_one')

Em vez de:


    df = rename(select(df, 'one), one='new one')

Essa mini-palestra exibe uma possível solução, discute os métodos mágicos de um objeto Python que permitem sobrecarregar os operadores, e discute quando é idiomático faze-lo.

A apresentação foi feita usando-se um IPython Notebook que está publicado no github:

 * [https://github.com/scardine/palestra-grupy-2015-11](https://github.com/scardine/palestra-grupy-2015-11)
