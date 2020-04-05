# Automatización de pruebas para UI Testing

http://newtours.demoaut.com/

En este ejercicio se realizó la automatización de UI para el proceso de compra de tiquetes aéreos. Esto comprende las actividades de "Inicio de sesión", "Búsqueda de vuelos", "Selección de vuelos", "Reserva de vuelo" y "Confirmar reserva"

En la carpeta `tests` se programaron los casos de prueba, utilizando el Webdriver de Chrome
En la carpeta `behaviors` se han definido archivos `.feature` donde se definen los escenarios
En la carpeta `behaviors\steps` se encuentra los pasos necesarios para la ejecución de los casos de prueba, dependiendo del archivo .feature
En la carpeta `behaviors\reports` se encuentra los informes de la automatización de pruebas


## Ejecución de las pruebas de automatización de UI

```bash
behave python_ui_testing/behaviours/buy_flights.feature
```
Debe entregar la siguiente salida

```bash
Feature: login en Mercury Tours # python_ui_testing/behaviours/buy_flights.feature:1

  Scenario:                                                                   # python_ui_testing/behaviours/buy_flights
.feature:4
    Given Estoy en la página de Mercury Tours: "http://newtours.demoaut.com/" # python_ui_testing/behaviours/steps/buy_f
lights_steps.py:8

DevTools listening on ws://127.0.0.1:62890/devtools/browser/1fecd7db-f64e-4564-a9a2-1f0e0876707c
    When Ingreso un usuario "camilo123" y un password "camilo123"             # python_ui_testing/behaviours/steps/buy_f
lights_steps.py:14
    Then El sistema me autentica como usuario legitimo                        # python_ui_testing/behaviours/steps/buy_f
lights_steps.py:19

  Scenario:                                                   # python_ui_testing/behaviours/buy_flights.feature:10
    Given Estoy en la página de Flight Finder                 # python_ui_testing/behaviours/steps/buy_flights_steps.py:
26
    When Selecciono el tipo de vuelo "oneway"                 # python_ui_testing/behaviours/steps/buy_flights_steps.py:
32
    And Ingreso el número de pasajeros "2"                    # python_ui_testing/behaviours/steps/buy_flights_steps.py:
37
    And Ingreso el origen "New York"                          # python_ui_testing/behaviours/steps/buy_flights_steps.py:
42
    And Ingreso la fecha de ida: mes "9" y el día "21"        # python_ui_testing/behaviours/steps/buy_flights_steps.py:
47
    And Ingreso el destino "Paris"                            # python_ui_testing/behaviours/steps/buy_flights_steps.py:
52
    And Ingreso la fecha de vuelta: el mes "10" y el día "27" # python_ui_testing/behaviours/steps/buy_flights_steps.py:
57
    And Selecciono la clase "First Class"                     # python_ui_testing/behaviours/steps/buy_flights_steps.py:
62
    And Selecciono la aerolínea "Pangea Airlines"             # python_ui_testing/behaviours/steps/buy_flights_steps.py:
67
    And Doy click en Continuar (buscar vuelo)                 # python_ui_testing/behaviours/steps/buy_flights_steps.py:
72
    Then El sistema busca los vuelos                          # python_ui_testing/behaviours/steps/buy_flights_steps.py:
77

  Scenario:                                                                                     # python_ui_testing/beha
viours/buy_flights.feature:24
    Given Estoy en la página de Select Flight                                                   # python_ui_testing/beha
viours/steps/buy_flights_steps.py:84
    When Selecciono la aerolínea de ida "Pangea Airlines" y la aerolínea de vuelta "Blue Skies" # python_ui_testing/beha
viours/steps/buy_flights_steps.py:90
    And Doy click en Continuar (seleccionar vuelo)                                              # python_ui_testing/beha
viours/steps/buy_flights_steps.py:95
    Then El sistema selecciona los vuelos                                                       # python_ui_testing/beha
viours/steps/buy_flights_steps.py:100

  Scenario:

                                                                            # python_ui_testing/behaviours/buy_flights.f
eature:31
    Given Estoy en la página de Book a Flight

                                                                            # python_ui_testing/behaviours/steps/buy_fli
ghts_steps.py:107
    When Ingreso el nombre "Camilo" y el apellido "Manrique". Selecciono la comida "Low Calorie". Ingreso el nombre y ap
ellido del pasajero 2 "Ruben" y "Blades"
                                                                            # python_ui_testing/behaviours/steps/buy_fli
ghts_steps.py:113
    And Selecciono la tarjeta de crédito "Visa". Ingreso el número de tarjeta de crédito "123456789". Selecciono el mes
de vencimiento "01". Selecciono el año de vencimiento "2000". Ingreso el nombre del pasajero "Camilo". Ingreso el segund
o nombre del pasajero "Andres". Ingreso el apellido del pasajero "Manrique" # python_ui_testing/behaviours/steps/buy_fli
ghts_steps.py:120
    And Ingreso la dirección de facturación "Carrera". Ingreso la dirección 2 de facturación "Calle". Ingreso la ciudad
de facturación "Medellín". Ingreso el estado de facturación "ANT". Ingreso el código postal de facturación "0000". Selec
ciono el país de facturación "Colombia"                                     # python_ui_testing/behaviours/steps/buy_fli
ghts_steps.py:131
    And Ingreso la dirección de entrega "Carrera". Ingreso la dirección 2 de entrega "Calle". Ingreso la ciudad de entre
ga "Medellín". Ingreso el estado de entrega "ANT". Ingreso el código postal de entrega "0000". Selecciono el país de ent
rega "Colombia"                                                             # python_ui_testing/behaviours/steps/buy_fli
ghts_steps.py:141
    And Doy click en Asegurar Compra

                                                                            # python_ui_testing/behaviours/steps/buy_fli
ghts_steps.py:151
    Then El sistema reserva el vuelo

                                                                            # python_ui_testing/behaviours/steps/buy_fli
ghts_steps.py:156

  Scenario:                                           # python_ui_testing/behaviours/buy_flights.feature:41
    Given Estoy en la página de Confirmación de vuelo # python_ui_testing/behaviours/steps/buy_flights_steps.py:163
    When Doy click en Volver al home                  # python_ui_testing/behaviours/steps/buy_flights_steps.py:169
    Then el sistema vuleve a la página de inicio      # python_ui_testing/behaviours/steps/buy_flights_steps.py:174

1 feature passed, 0 failed, 0 skipped
5 scenarios passed, 0 failed, 0 skipped
28 steps passed, 0 failed, 0 skipped, 0 undefined
```