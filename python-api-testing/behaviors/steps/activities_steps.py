from behave import *
from tests.tests_activities import ApiActivities


test = ApiActivities()


@given(u'Estoy en la URL de la API de actividades')
def step_impl(context):
    pass


@when(u'Consulto todas las actividades')
def step_impl(context):
    test.test_get_all_activities()


@then(u'Retorna todas las actividades')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'consulto una actividad con codigo "{activity_id}"')
def step_impl(context, activity_id):
    context.activity_id = activity_id
    test.test_get_activity(context.activity_id)


@then(u'Trae la información de la actividad')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'consulto una actividad no existente con id "{activity_id}"')
def step_impl(context, activity_id):
    context.activity_id = activity_id
    test.test_notfound_activity(context.activity_id)


@then(u'Debe retornar vacio en la respuesta')
def step_impl(context):
    test.test_validate_response_text('')


@when(u'Creo una actividad con id "{activity_id}" y nombre "{activity_title}"')
def step_impl(context, activity_id, activity_title):
    context.activity_id = activity_id
    context.activity_title = activity_title
    test.test_create_activity(context.activity_id, context.activity_title)


@then(u'Debe crear una nueva actividad con el titulo y ID dado')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'Elimino una actividad con id "{activity_id}"')
def step_impl(context, activity_id):
    context.activity_id = activity_id
    test.test_delete_activity(context.activity_id)


@then(u'Elimina la actividad especificada')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'Actualizo la actividad con id "{activity_id}" y nombre "{activity_title}"')
def step_impl(context, activity_id, activity_title):
    context.activity_id = activity_id
    context.activity_title = activity_title
    test.test_update_activity(activity_id, activity_title)


@then(u'Hace cambios en la actividad indicada')
def step_impl(context):
    test.test_validate_status_code(200)
