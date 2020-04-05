Feature: login en Mercury Tours

  #Login
  Scenario:
    Given Estoy en la página de Mercury Tours: "http://newtours.demoaut.com/"
    When Ingreso un usuario "camilo123" y un password "camilo123"
    Then El sistema me autentica como usuario legitimo

  #Buscar vuelo
  Scenario:
    Given Estoy en la página de Flight Finder
    When Selecciono el tipo de vuelo "oneway"
    And Ingreso el número de pasajeros "2"
    And Ingreso el origen "New York"
    And Ingreso la fecha de ida: mes "9" y el día "21"
    And Ingreso el destino "Paris"
    And Ingreso la fecha de vuelta: el mes "10" y el día "27"
    And Selecciono la clase "First Class"
    And Selecciono la aerolínea "Pangea Airlines"
    And Doy click en Continuar (buscar vuelo)
    Then El sistema busca los vuelos

  #Seleccionar vuelo
  Scenario:
    Given Estoy en la página de Select Flight
    When Selecciono la aerolínea de ida "Pangea Airlines" y la aerolínea de vuelta "Blue Skies"
    And Doy click en Continuar (seleccionar vuelo)
    Then El sistema selecciona los vuelos

  #Reservar vuelo
  Scenario:
    Given Estoy en la página de Book a Flight
    When Ingreso el nombre "Camilo" y el apellido "Manrique". Selecciono la comida "Low Calorie". Ingreso el nombre y apellido del pasajero 2 "Ruben" y "Blades"
    And Selecciono la tarjeta de crédito "Visa". Ingreso el número de tarjeta de crédito "123456789". Selecciono el mes de vencimiento "01". Selecciono el año de vencimiento "2000". Ingreso el nombre del pasajero "Camilo". Ingreso el segundo nombre del pasajero "Andres". Ingreso el apellido del pasajero "Manrique"
    And Ingreso la dirección de facturación "Carrera". Ingreso la dirección 2 de facturación "Calle". Ingreso la ciudad de facturación "Medellín". Ingreso el estado de facturación "ANT". Ingreso el código postal de facturación "0000". Selecciono el país de facturación "Colombia"
    And Ingreso la dirección de entrega "Carrera". Ingreso la dirección 2 de entrega "Calle". Ingreso la ciudad de entrega "Medellín". Ingreso el estado de entrega "ANT". Ingreso el código postal de entrega "0000". Selecciono el país de entrega "Colombia"
    And Doy click en Asegurar Compra
    Then El sistema reserva el vuelo

  #Confirmar reseva
  Scenario:
    Given Estoy en la página de Confirmación de vuelo
    When Doy click en Volver al home
    Then el sistema vuleve a la página de inicio