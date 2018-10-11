import re,os, webbrowser
header = ''' <!doctype html>
<html>
    <head>
        <title>Meus filmes favoritos</title>
        <meta charset="utf-8">
        <script type="text/javascript" src='http://ajax.googleapis.com/ajax/libs/jquery/1.4/jquery.js'></script>
        <script>

            //CRIANDO UM NOVO ELEMENTO UTILIZANDO JQUERY
            $(document).ready(function()                                        //VERIFICAÇÃO SE O DOM JA ESTÁ PRONTO*/
            {
                $('.tocar_trailer').click(function()                            //CAPTURANDO O CLICK DE QUALQUER ELEMENTO QUE TENHA A CLASSE .tocar_trailer     
                {
                    $('.modal-body').empty();                                   //REMOVER TODOS OS ELEMENTOS DO LOCAL QUE IRÁ RECEBER O TRAILER
                    var youtube_id = $(this).attr('data-trailer-youtube-id');   //CAPTURANDO O VALOR DO ATRIBUTO DE VALOR                    
                    $('<iframe />',                                             //CRIANDO UM NOVO ELEMENTO iframe
                    {
                       //ATRIBUTOS DO NOVO ELEMENTO                                   
                        name: 'frame',
                        class: 'embed-responsive-item',
                        frameborder:'0',
                        width: '100%',
                        height:'500px',
                        src: 'http://www.youtube.com/embed/'+ youtube_id +'?autoplay=1&html5=1'  //O LINK RECEBERA O VALOR RECOLHIDO ANTERIORMENTE  
                    }).appendTo('.modal-body');                                 //ADICIONANDO O NOVO ELEMENTO NO DOCUMENTO HTML
                });              
            });

            //REMOVENDO O ELEMENTO LOGO APÓS FECHAR O MODAL-CAIXA DE DIALOGO
            $(document).ready(function()
            {

                $('.close').click(function()                                    //CAPTURANDO O CLICK DE QUALQUER ELEMENTO QUE TENHA A CLASSE .close
                {   
                    $('<iframe />').remove();                                   //REMOVENDO O IFRAME
                    $('.modal-body').empty();                                   //REMOVENDO TODOS OS ELEMENTOS FILHOS DO ELEMENTO QUE CONTEM .modal-body COMO CLASSE
                });  
            });

        </script>

<!--DEFININDO O ESTILO DO HTML -->
    <style type="text/css">
 
    
    body
    {
        background: url('https://image.ibb.co/jdCWOp/filmes.jpg') no-repeat;
        background-size: cover;
        color: #D3D3D3;
        text-align: center;
    }


    /*===========================MENU===========================*/
    #menu
    {
        background: rgba(0,0,0,0.6);
        color:#D3D3D3;
        padding: 10px;
        
        
    }


    /*===========================DIV 1 - C0NTENT=================*/
    #content
    {
        display: grid;                      /*TRANSFORMANDO-O EM GRID*/
        grid-template-columns: 100%;        /*TEREMOS 1 COLUNA POR LINHA OCUPANDO 100% DA LARGURA DO CONTENT*/
        max-width: 960px;
        margin: 0 auto;                     /*CENTRALIZAÇÃO DO CONTENT*/
    }
    #content div 
    {    
        padding: 30px;
    }
       

    /*================GRID 2 - GRID DE CONTEUDO================*/
     #conteudo 
    {
        display: grid;                        /*TAMBEM SERA UM GRID*/
        grid-template-columns:repeat(3, 1fr); /*3 COLUNAS OCUPANDO 1 FRAÇÃO DO TOTAL CADA UMA*/
        grid-column-gap: 10px;                /*ESPAÇAMENTO ENTRE AS COLUNAS*/
        grid-row-gap: 10px;                   /*ESPAÇAMENTO ENTRE AS LINHAS */
        text-align:center;                    /*ALINHAMENTO DO TEXTO NO CENTRO EM RELAÇÃO AO SEU ELEMENTO PAI*/
    }    
    #conteudo img
    {   
        border-radius: 50%;                   /*FORMATO DE CIRFUNFERENCIA*/
        width:200px;
        height:200px;
        opacity: 0.9;                         /*OPACIDADE INICIAL*/
        
    }
       
    #conteudo img:hover
    {
        transition:1s;
        opacity: 1;                           /*OPACIDADE FINAL - APÓS PASSAR O CURSOR POR CIMA*/
        
            
    }
  

    #conteudo a
    { 
        transition: 2s;
        opacity:0.5;
    }
    #conteudo a:hover
    { 
        transition: 1s;
        opacity:1;
    }
    /*=============RESPONSIVIDADE DO GRID 2 ===============*/
    @media screen and (max-width:768px)       /*CONFIGURAÇÕES PARA TELAS  DE ATÉ 768 pixels */
    {
        #conteudo a {margin-top: 120px;}             
        #conteudo 
        {           
            grid-template-columns:1fr;        /*QUANTIDADE DE COLUNAS E SEU TAMANHO EM LARGURA*/
            grid-row-gap: 10px;               /*ESPAÇAMENTO ENTRE AS LINHAS*/
            transition:2s;
        }
        #conteudo img
        {   
            border-radius: 10%;               
            width:100%;
            height:100%;
            transition:2s;
        }
     }
      
    </style>
    </head>
'''
    
conteudo_principal = ''' <body>
        <div id="menu"><span class="navbar-brand">MY FAFORITES FILMS AND TV SHOWS</span></div>
        <div id="content">
            
            <div id="conteudo">{links_filmes}</div>
           
            
        </div>
        
        <div id="meu-modal" class="modal fade" tabindex="1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal">X</button>
                    </div>

                    <div class="modal-body">

                    </div>
                </div>
            </div>
        </div>
    </body>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
</html>'''

links_filmes = '''<a style="text-decoration:none; color:white; " class="tocar_trailer" data-toggle="modal" data-target="#meu-modal" href="#" data-trailer-youtube-id="{id_trailer}"><h4 class="card-title">{titulo_filme}</h4><img src="{poster_filme}"></a>
                 '''

def criar_links_filmes(filmes):
    novo_conteudo= ''
    for filme in filmes:
        youtube_id = re.search(r'(?<=v=)[\w]*',filme.endereco_trailer)      #CAPTURAR O ID DO VIDEO A PARTIR DE UMA URL INFORMADA
        novo_conteudo+= links_filmes.format(id_trailer=youtube_id.group(0), #GUARDAR O NOVO FILME E SEUS DADOS INCLUINDO O ID DO TRAILER
        poster_filme=filme.endereco_poster, titulo_filme=filme.titulo)      
    return novo_conteudo                                                    #RETORNO DO CONTEUDO ATUALIZADO 

def abrir_pagina_filmes(filmes):
    arquivo = open('filmes.html', 'w')                                                          #ABERTURA DO ARQUIVO EM MODO DE ESCRITA
    conteudo_atualizado = conteudo_principal.format(links_filmes=criar_links_filmes(filmes))
    arquivo.write(header+conteudo_atualizado)                                                   #ESCREVENDO O NOVO CONTEUDO NO ARQUIVO
    arquivo.close()                                                                             #FECHAMENTO DO ARQUIVO    
    url = os.path.abspath(arquivo.name)                                                         #RETORNO DO PATHNAME - ENDEREÇO DO ARQUIVO
    webbrowser.open('file://'+url)                                                              #ABERTURA DO ARQUIVO NO BROWSER
