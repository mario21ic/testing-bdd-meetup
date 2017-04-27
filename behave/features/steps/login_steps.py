from behave import given, when, then, step
#from hamcrest import assert_that, equal_to, is_not


@given(u'load path {path}')
def step_impl_carga(context, path):
    context.driver.get(context.base_url + path)

@when(u'I click on Ingresa link')
def step_impl(context):
    login_lnk = context.driver.find_element_by_xpath("html/body/header/section[2]/div[1]/div/ul/li[4]/a")
    login_lnk.click()

@when(u'I put {email} and {password}')
def step_impl(context, email, password):
    txt_user = context.driver.find_element_by_id("txtUser")
    txt_user.send_keys("mario21ic@gmail.com")

    txt_pass = context.driver.find_element_by_id("txtPasswordLogin")
    txt_pass.send_keys("miclave1234")

@when(u'I clic on Ingresar buton')
def step_impl(context):
    login_btn = context.driver.find_element_by_xpath(".//*[@id='frmUserLogIn']/button")
    login_btn.click()

@when(u'I wait {seconds} seconds')
def step_impl(context, seconds):
    #sleep(seconds)
    pass

@when(u'I wait {seconds} seconds until see link Mis Ofertas Educativas')
def step_impl(context, seconds):
    context.page.wait_until_link_text(seconds)

@when("I wait {seconds} seconds until see ico {element}")
def step_impl(context, seconds, element):
    context.page.wait_until_ico_login(seconds, element)

@then("I see the url")
def step_impl(context):
    print("xD")
    #assert_that(u"Bienvenido Luis", equal_to(context.page.get_username()))


