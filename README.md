# MOVIE TRAILER WEBSITE
This repository contains Scripts that was created in Python to generate a WebSite with the iformation that was provided in one of the Scripts.
The information that you'll need to provide are: Title of the movie, URL of the poster and Youtube trailer URL . All that information will be redenred as a Web page.

## REQUIREMENTS
### Requirements to run the Scripts 

First thing first, you'll need to have Python 3 installed in your computer.

## Requirements to see the website
Network connection.
 - Why? 
 - Inside the HTML and CSS code some elements like images are provided throught outher websites whch this images are hosted.

## INSTALL
### ON LINUX 
1.  Open your terminal;
1.  Clone this repository (or download it in the **GREEN BUTTON** above)  
    ``` 
    git clone https://github.com/HiroTatsuo/Movie-trailer-WEBSITE.git    
    ```
1.  Store your movie
    1.  Open the centro_de_informacoes.py is file with your prefred text editor
    1.  Store your movie in there
    ```
    [name of your movie] = filmes.Filme({title}, {poster URL}, {Youtube trailer URL})
    ```
    ###### EXAMPLE
    > interstellar = filmes.Filme("Interstellar",
                            "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg",
                            'https://www.youtube.com/watch?v=zSWdZVtXT7E')
    
1.  Run the centro_de_informacoes.py is file
    ```
    python3 centro_de_informacoes.py
    
1.  A new file called "filmes.html" will be created, open it and apreciate
> REMEMBER, YOU NEED INTERNET CONNECTION TO SEE IMAGES AND TRAILERS OF THE MOVIES STORED 
