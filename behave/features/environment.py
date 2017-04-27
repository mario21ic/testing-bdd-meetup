import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


# Runs before each Given, When and Then step.
def before_step(context, step):
    pass


# Runs after each step
def after_step(context, step):
    #session.clear_cookies_if_required(session.Stage.step, context)
    if step.status == "failed":
        print("step failed")
    #if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
    #    import ipdb
    #    ipdb.post_mortem(step.exc_traceback)


# Runs before each full scenario (complete Given, When, Then definition)
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.base_url = "http://aptitus.com"
    pass

# Runs after each scenario
def after_scenario(context, scenario):
    #session.clear_cookies_if_required(session.Stage.scenario, context)
    #if scenario.status == "failed":
    #    screenshot.capture_failure(context, scenario)
    pass

# Runs before each feature file
def before_feature(context, feature):
    pass

# Runs after each feature
def after_feature(context, feature):
    #session.clear_cookies_if_required(session.Stage.feature, context)
    pass

def before_all(context):
    setup_debug_on_error(context.config.userdata)
    #context.base_url = base_url
    #context.base_dir = os.getcwd()

def after_all(context):
    #session.clear_cookies_if_required(session.Stage.lifetime, context)
    # Very last thing to run.
    #context.display.stop()
    pass
