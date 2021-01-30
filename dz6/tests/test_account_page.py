import pytest


@pytest.mark.parametrize('path', ['login'])
def test_login_page_elements(account_page):
    account_page.should_be_login_elements()


# TODO: Для данного теста необходимо реализовать фикстуру предварительного удаления учетной записи с данными параметрами
@pytest.mark.parametrize('path', ['register'])
def test_register_form(account_page):
    account_page.input_reg_first_name()
    account_page.input_reg_last_name()
    account_page.input_reg_email()
    account_page.input_reg_telephone()
    account_page.input_reg_pass()
    account_page.input_reg_pass_confirm()
    account_page.accept_reg_policy()
    account_page.accept_reg_form()
    account_page.new_account_created()
