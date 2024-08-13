from fastapi import FastAPI

app = FastAPI(
    title = 'Practicado FastApi', #Titulo que aparecera en /docs
    description = 'Api basica',
    version = '0.0.1'
    
)

@app.get('/' , tags =['Inicio'])

def read_root():
    return {'Hello': 'World'}