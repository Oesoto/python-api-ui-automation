from behave import *
from tests.tests_authors import ApiAuthors

test = ApiAuthors()


@given(u'Estoy en la URL de la API de autores')
def step_impl(context):
    pass


@when(u'Consulto los autores para el libro con id "{book_id}"')
def step_impl(context, book_id):
    context.book_id = book_id
    test.test_get_authors_for_book(context.book_id)


@then(u'Retorna el listado de autores para el libro')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'Consulto todos los autores')
def step_impl(context):
    test.test_get_all_authors()


@then(u'Retorna todos los autores')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'Creo un autor con id "{author_id}" para el libro con id "{book_id}" de nombre "{first_name}" y apellido "{'
      u'last_name}"')
def step_impl(context, author_id, book_id, first_name, last_name):
    context.author_id = author_id
    context.book_id = book_id
    context.first_name = first_name
    context.last_name = last_name
    test.test_create_author(context.author_id, context.book_id, context.first_name, context.last_name)


@then(u'Crea el nuevo autor con los datos proporcionados')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'Elimino un autor con id "{author_id}"')
def step_impl(context, author_id):
    context.author_id = author_id
    test.test_delete_author(context.author_id)


@then(u'El autor es eliminado')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'Consulto un autor con id "{author_id}"')
def step_impl(context, author_id):
    context.author_id = author_id
    test.test_get_author(context.author_id)


@then(u'Retorna la informacion del autor')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'Actualizado el autor con id "{author_id}" para el libro con id "{book_id}" con nombre "{first_name}" y '
      u'apellido "{last_name}"')
def step_impl(context, author_id, book_id, first_name, last_name):
    context.author_id = author_id
    context.book_id = book_id
    context.first_name = first_name
    context.last_name = last_name
    test.test_update_author(context.author_id, context.book_id, context.first_name, context.last_name)


@then(u'Hace los cambios en el autor indicado')
def step_impl(context):
    test.test_validate_status_code(200)
