from behave import *
from python_ui_testing.tests.buy_flights import BuyFlightsTest

test = BuyFlightsTest()


# LOGIN
@given(u'Estoy en la página de Mercury Tours: "{url}"')
def step_impl(context, url):
    test.setUpClass()
    test.test_go_url(url)


@when(u'Ingreso un usuario "{user}" y un password "{password}"')
def step_impl(context, user, password):
    test.test_login(user, password)


@then(u'El sistema me autentica como usuario legitimo')
def step_impl(context):
    test.test_image_flight_finder()



# BUSCAR VUELOS
@given(u'Estoy en la página de Flight Finder')
def step_impl(context):
    print("Estoy en la página de Flight Finder")
    pass


@when(u'Selecciono el tipo de vuelo "{type}"')
def step_impl(context, type):
    test.test_select_flight_type(type)


@when(u'Ingreso el número de pasajeros "{number}"')
def step_impl(context, number):
    test.test_select_passanger_number(number)


@when(u'Ingreso el origen "{city}"')
def step_impl(context, city):
    test.test_select_origin(city)


@when(u'Ingreso la fecha de ida: mes "{month}" y el día "{day}"')
def step_impl(context, month, day):
    test.test_select_departure_date(month, day)


@when(u'Ingreso el destino "{city}"')
def step_impl(context, city):
    test.test_select_destiny(city)


@when(u'Ingreso la fecha de vuelta: el mes "{month}" y el día "{day}"')
def step_impl(context, month, day):
    test.test_select_returning_date(month, day)


@when(u'Selecciono la clase "{serv_class}"')
def step_impl(context, serv_class):
    test.test_select_service_class(serv_class)


@when(u'Selecciono la aerolínea "{air}"')
def step_impl(context, air):
    test.test_select_airline("Pangea Airlines")


@when(u'Doy click en Continuar (buscar vuelo)')
def step_impl(context):
    test.test_search_flight()


@then(u'El sistema busca los vuelos')
def step_impl(context):
    test.test_image_select_flight()



# Seleccionar vuelo
@given(u'Estoy en la página de Select Flight')
def step_impl(context):
    print("Given Estoy en la página de Select Flight")
    pass


@when(u'Selecciono la aerolínea de ida "{departure}" y la aerolínea de vuelta "{returnn}"')
def step_impl(context, departure, returnn):
    test.test_select_departure_return_flights(departure, returnn)


@when(u'Doy click en Continuar (seleccionar vuelo)')
def step_impl(context):
    test.test_select_flights()


@then(u'El sistema selecciona los vuelos')
def step_impl(context):
    test.test_image_book_a_flight()



# Reservar vuelo
@given(u'Estoy en la página de Book a Flight')
def step_impl(context):
    print("Given Estoy en la página de Book a Flight")
    pass


@when(u'Ingreso el nombre "{name}" y el apellido "{lastname}". '
      u'Selecciono la comida "{meal}". '
      u'Ingreso el nombre y apellido del pasajero 2 "{name2}" y "{lastname2}"')
def step_impl(context, name, lastname, meal, name2, lastname2):
    test.test_enter_personal_data(name, lastname, meal, name2, lastname2)


@when(u'Selecciono la tarjeta de crédito "{credit_card}". '
      u'Ingreso el número de tarjeta de crédito "{card_number}". '
      u'Selecciono el mes de vencimiento "{expiration_month}". '
      u'Selecciono el año de vencimiento "{expiration_year}". '
      u'Ingreso el nombre del pasajero "{name}". '
      u'Ingreso el segundo nombre del pasajero "{lastname}". '
      u'Ingreso el apellido del pasajero "{midname}"')
def step_impl(context, credit_card, card_number, expiration_month, expiration_year, name, lastname, midname):
    test.test_enter_credit_card_data(credit_card, card_number, expiration_month, expiration_year, name, lastname, midname)


@when(u'Ingreso la dirección de facturación "{bill_address1}". '
      u'Ingreso la dirección 2 de facturación "{bill_address2}". '
      u'Ingreso la ciudad de facturación "{bill_city}". '
      u'Ingreso el estado de facturación "{bill_state}". '
      u'Ingreso el código postal de facturación "{bill_zip}". '
      u'Selecciono el país de facturación "{country}"')
def step_impl(context, bill_address1, bill_address2, bill_city, bill_state, bill_zip, country):
    test.test_enter_billing_address(bill_address1, bill_address2, bill_city, bill_state, bill_zip, country)


@when(u'Ingreso la dirección de entrega "{del_address1}". '
      u'Ingreso la dirección 2 de entrega "{del_address2}". '
      u'Ingreso la ciudad de entrega "{del_city}". '
      u'Ingreso el estado de entrega "{del_state}". '
      u'Ingreso el código postal de entrega "{del_zip}". '
      u'Selecciono el país de entrega "{country}"')
def step_impl(context, del_address1, del_address2, del_city, del_state, del_zip, country):
    test.test_enter_delivery_address(del_address1, del_address2, del_city, del_state, del_zip, country)


@when(u'Doy click en Asegurar Compra')
def step_impl(context):
    test.test_book_flight()


@then(u'El sistema reserva el vuelo')
def step_impl(context):
    test.test_image_flight_confirmation()



# Confirmar reseva
@given(u'Estoy en la página de Confirmación de vuelo')
def step_impl(context):
    print("Given Estoy en la página de Confirmación de vuelo")
    pass


@when(u'Doy click en Volver al home')
def step_impl(context):
    test.test_flight_confirmation()


@then(u'el sistema vuleve a la página de inicio')
def step_impl(context):
    test.test_image_home()
    test.tearDownClass()


