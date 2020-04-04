Feature: Gestionar Autores

    Background:
        Given Estoy en la URL de la API de autores

    Scenario: Consultar los autores para un libro
        When Consulto los autores para el libro con id "16"
        Then Retorna el listado de autores para el libro

    Scenario: Consultar todos los autores
        When Consulto todos los autores
        Then Retorna todos los autores

    Scenario: Crear un autor
        When Creo un autor con id "25" para el libro con id "42" de nombre "Andres" y apellido "Arango"
        Then Crea el nuevo autor con los datos proporcionados

    Scenario: Eliminar un autor
        When Elimino un autor con id "30"
        Then El autor es eliminado

    Scenario: Consultar un autor
        When Consulto un autor con id "88"
        Then Retorna la informacion del autor

    Scenario: Actualizar la informacion de un autor
        When Actualizado el autor con id "25" para el libro con id "42" con nombre "Andres Felipe" y apellido "Arango"
        Then Hace los cambios en el autor indicado