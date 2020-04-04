Feature: gestionar actividades

    Background:
        Given Estoy en la URL de la API de actividades

    Scenario: Consultar todas las actividades
        When Consulto todas las actividades
        Then Retorna todas las actividades

    Scenario: Consultar una actividad
        When consulto una actividad con codigo "2"
        Then Trae la información de la actividad

    Scenario: Consultar una actividad que no existe
        When consulto una actividad no existente con id "100"
        Then Debe retornar vacio en la respuesta

    Scenario: Crear una actividad
        When Creo una actividad con id "20" y nombre "Mi nueva actividad"
        Then Debe crear una nueva actividad con el titulo y ID dado

    Scenario: Eliminar una actividad
        When Elimino una actividad con id "20"
        Then Elimina la actividad especificada

    Scenario: Actualizar una actividad
        When Actualizo la actividad con id "20" y nombre "Titulo actualizado"
        Then Hace cambios en la actividad indicada