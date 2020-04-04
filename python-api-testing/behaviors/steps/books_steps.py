from behave import *
from tests.tests_books import ApiBooks

test = ApiBooks()


@given(u'Estoy en la URL de la API de libros')
def step_impl(context):
    pass


@when(u'Consulto todos los libros')
def step_impl(context):
    test.test_get_all_books()


@then(u'Retorna todos los libros')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'Creo un libro con id "{book_id}" titulo "{book_title}" descripcion "{description}" numero de paginas "{'
      u'page_count}" y extracto "{excerpt}"')
def step_impl(context, book_id, book_title, description, page_count, excerpt):
    context.book_id = book_id
    context.book_title = book_title
    context.description = description
    context.page_count = page_count
    context.excerpt = excerpt
    test.test_create_book(context.book_id, context.book_title, context.description, context.page_count, context.excerpt)


@then(u'Crea el libro con la informacion especificada')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'Elimino un libro con id "{book_id}"')
def step_impl(context, book_id):
    context.book_id = book_id
    test.test_delete_book(context.book_id)


@then(u'Elimina el libro con el id especificado')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'Consulto un libro con id "{book_id}"')
def step_impl(context, book_id):
    context.book_id = book_id
    test.test_get_book(context.book_id)


@then(u'Retorna el libro con el id especificado')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'Consulto un libro no existente con id "{book_id}"')
def step_impl(context, book_id):
    context.book_id = book_id
    test.test_notfound_book(context.book_id)


@then(u'La consulta del libro debe retornar vacio')
def step_impl(context):
    test.test_validate_response_text('')


@when(u'Actualizo un libro con id "{book_id}" titulo "{book_title}" descripcion "{description}" numero de '
      u'paginas "{page_count}" y extracto "{excerpt}"')
def step_impl(context, book_id, book_title, description, page_count, excerpt):
    context.book_id = book_id
    context.book_title = book_title
    context.description = description
    context.page_count = page_count
    context.excerpt = excerpt
    test.test_update_book(context.book_id, context.book_title, context.description, context.page_count, context.excerpt)


@then(u'Se actualiza el libro con la nueva informacion proporcionada')
def step_impl(context):
    test.test_validate_status_code(200)

