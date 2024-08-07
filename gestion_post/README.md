"# -Microservicio-de-Gesti-n-de-Posts-G4" 



docker-compose up -d    #Para contruir la imagen y crear el contenedor en base a esta

Despues se puede hacer las peticiones al localhost:8000

Get: localhost:8000/posts  #obtener todos los posts
Post localhost:8000/posts  (En thunder client establecer un body {
    "title": "Test Post Thunder",
    "content": "This is a test post from thunderClient."
})

Get: localhost:8000/posts/{id}    #obtner un post
 
