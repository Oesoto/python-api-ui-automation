Feature: Gestionar Libros

    Background:
        Given Estoy en la URL de la API de libros

    Scenario: Consultar todos los libros
        When Consulto todos los libros
        Then Retorna todos los libros

    Scenario: Crear un libro
        When Creo un libro con id "30" titulo "Fundamentos de fisica" descripcion "Explicacion fisica elemental" numero de paginas "428" y extracto "Fisica desde cero"
        Then Crea el libro con la informacion especificada

    Scenario: Eliminar un libro
        When Elimino un libro con id "45"
        Then Elimina el libro con el id especificado

    Scenario: Consultar un libro especifico
        When Consulto un libro con id "16"
        Then Retorna el libro con el id especificado

    Scenario: Consultar una actividad que no existe
        When Consulto un libro no existente con id "250"
        Then La consulta del libro debe retornar vacio

    Scenario: Actualizar un libro
        When Actualizo un libro con id "30" titulo "Fundamentos de fisica" descripcion "Fisica fundamental" numero de paginas "450" y extracto "Fisica basica desde cero"
        Then Se actualiza el libro con la nueva informacion proporcionada