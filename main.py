from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI(
    title = 'Practicado FastApi', #Titulo que aparecera en /docs
    description = 'Api basica',
    version = '0.0.1'
    
)

#TODO: Array de peliculas
movies = [
    {
     'id': 1,
     'title': 'La La Land',
     'overview': "La La Land es una pelicula un poco aburrida",
     'year': '2020',
     'rating': 9.2,
     'category': "drama"
     }
]

@app.get('/' , tags =['Inicio'])
def read_root():
    return HTMLResponse('<h2>Hola Mundo </h2>')

# Metodo GET
@app.get('/movies', tags=["Movies"])
def get_movies():
    return  movies 

# Parametros de Ruta
@app.get('/movies/{id}', tags=["Movies"])
def get_movie(id: int):
    for item in movies:
        if item['id'] == id:
            return item
    return []

# Parametros de Query (Conjunto de parametros opcionales)
@app.get('/movies/', tags=["Movies"])
def get_movies_by_category(category: str):
    return category 

# Metodo POST
@app.post('/movies', tags=["Movies"])
def create_movie(
    id: int = Body(), 
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body(),
):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
})
    print(movies)
    return title 

# Metodo PUT - DELETE
@app.put('/movies/{id}', tags=["Movies"])
def update_movie(
    id: int = Body(), 
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body(),
):
    for item in movies:
        if item['id'] == id:
            item['title'] = title
            item['overview'] = overview
            item['year'] = year
            item['rating'] = rating
            item['category'] = category
    return item
          
