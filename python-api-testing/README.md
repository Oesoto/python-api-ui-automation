# Automatización de pruebas para API Testing

https://fakerestapi.azurewebsites.net/swagger/ui/index

En este ejercicio se han creado pruebas para las API de actividades, autores y libros

En la carpeta `behaviors` se han definido archivos `.feature` por cada una de las API definiendo los escenarios de pruebas


## Ejecución de las pruebas de actividades

```bash
behave behaviors/activities.feature
```
Debe entregar la siguiente salida

```bash
Feature: gestionar actividades # behaviors/activities.feature:1

  Background:   # behaviors/activities.feature:3

  Scenario: Consultar todas las actividades # behaviors/activities.feature:6
    Given Estoy en la URL de la API de actividades 
    When Consulto todas las actividades            
    Then Retorna todas las actividades             

  Scenario: Consultar una actividad # behaviors/activities.feature:10
    Given Estoy en la URL de la API de actividades 
    When consulto una actividad con codigo "2"     
    Then Trae la información de la actividad       

  Scenario: Consultar una actividad que no existe # behaviors/activities.feature:14
    Given Estoy en la URL de la API de actividades        
    When consulto una actividad no existente con id "100" 
    Then Debe retornar vacio en la respuesta              

  Scenario: Crear una actividad  # behaviors/activities.feature:18
    Given Estoy en la URL de la API de actividades                    
    When Creo una actividad con id "20" y nombre "Mi nueva actividad" 
    Then Debe crear una nueva actividad con el titulo y ID dado       

  Scenario: Eliminar una actividad # behaviors/activities.feature:22
    Given Estoy en la URL de la API de actividades 
    When Elimino una actividad con id "20"         
    Then Elimina la actividad especificada         

  Scenario: Actualizar una actividad # behaviors/activities.feature:26
    Given Estoy en la URL de la API de actividades                        
    When Actualizo la actividad con id "20" y nombre "Titulo actualizado" 
    Then Hace cambios en la actividad indicada                            

1 feature passed, 0 failed, 0 skipped
6 scenarios passed, 0 failed, 0 skipped
18 steps passed, 0 failed, 0 skipped, 0 undefined
```
## Ejecución de las pruebas de autores

```bash
behave behaviors/authors.feature
```
Debe entregar la siguiente salida

```bash
Feature: Gestionar Autores # behaviors/authors.feature:1

  Background:   # behaviors/authors.feature:3

  Scenario: Consultar los autores para un libro # behaviors/authors.feature:6
    Given Estoy en la URL de la API de autores          
    When Consulto los autores para el libro con id "16" 
    Then Retorna el listado de autores para el libro    

  Scenario: Consultar todos los autores # behaviors/authors.feature:10
    Given Estoy en la URL de la API de autores 
    When Consulto todos los autores           
    Then Retorna todos los autores             

  Scenario: Crear un autor # behaviors/authors.feature:14
    Given Estoy en la URL de la API de autores                                                      
    When Creo un autor con id "25" para el libro con id "42" de nombre "Andres" y apellido "Arango" 
    Then Crea el nuevo autor con los datos proporcionados                                          

  Scenario: Eliminar un autor                  # behaviors/authors.feature:18
    Given Estoy en la URL de la API de autores 
    When Elimino un autor con id "30"          
    Then El autor es eliminado                 

  Scenario: Consultar un autor                 # behaviors/authors.feature:22
    Given Estoy en la URL de la API de autores 
    When Consulto un autor con id "88"         
    Then Retorna la informacion del autor      

  Scenario: Actualizar la informacion de un autor # behaviors/authors.feature:26
    Given Estoy en la URL de la API de autores                                                                     
    When Actualizado el autor con id "25" para el libro con id "42" con nombre "Andres Felipe" y apellido "Arango" 
    Then Hace los cambios en el autor indicado                                                                     

1 feature passed, 0 failed, 0 skipped
6 scenarios passed, 0 failed, 0 skipped
18 steps passed, 0 failed, 0 skipped, 0 undefined

```

## Ejecución de las pruebas de libros

```bash
behave behaviors/books.feature
```

Debe entregar la siguiente salida

```bash
Feature: Gestionar Libros # behaviors/books.feature:1

  Background:   # behaviors/books.feature:3

  Scenario: Consultar todos los libros        # behaviors/books.feature:6
    Given Estoy en la URL de la API de libros 
    When Consulto todos los libros            
    Then Retorna todos los libros             

  Scenario: Crear un libro # behaviors/books.feature:10
    Given Estoy en la URL de la API de libros                            
    When Creo un libro con id "30" titulo "Fundamentos de fisica" descripcion "Explicacion fisica elemental" numero de paginas "428" y extracto "Fisica desde cero" 
    Then Crea el libro con la informacion especificada  

  Scenario: Eliminar un libro                    # behaviors/books.feature:14
    Given Estoy en la URL de la API de libros    
    When Elimino un libro con id "45"            
    Then Elimina el libro con el id especificado 

  Scenario: Consultar un libro especifico        # behaviors/books.feature:18
    Given Estoy en la URL de la API de libros    
    When Consulto un libro con id "16"           
    Then Retorna el libro con el id especificado 

  Scenario: Consultar una actividad que no existe    # behaviors/books.feature:22
    Given Estoy en la URL de la API de libros        
    When Consulto un libro no existente con id "250" 
    Then La consulta del libro debe retornar vacio   

  Scenario: Actualizar un libro # behaviors/books.feature:26
    Given Estoy en la URL de la API de libros
    When Actualizo un libro con id "30" titulo "Fundamentos de fisica" descripcion "Fisica fundamental" numero de paginas "450" y extracto "Fisica basica desde cero" 
    Then Se actualiza el libro con la nueva informacion proporcionada 

1 feature passed, 0 failed, 0 skipped
6 scenarios passed, 0 failed, 0 skipped
18 steps passed, 0 failed, 0 skipped, 0 undefined

```