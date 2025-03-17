from pytest_bdd import scenario, given, when, then
from splinter import Browser
import pytest
import time


@pytest.fixture
def browser():
  with Browser("chrome", headless=True) as browser:
      yield browser


@pytest.fixture
def visit_page(browser):
  browser.visit("http://localhost:5000/")
  heading = browser.find_by_css("h1").first
  assert "Weather API comparator" == heading.text


# Test for correct user input
@scenario("user_input_city.feature", "User gives correct city name as input")
def test_user_input_correct_city():
  pass


@given("User enters the website")
def test_user_enters_website(visit_page):
  pass


@when("User types 'London' as city name")
def user_inputs_correct_city(browser):
  browser.find_by_name("location").fill("London")


@when("User clicks on the search button")
def user_clicks_search_button(browser):
  browser.find_by_css("button[type='submit']").click()  


@then("User should see the weather details of London")
def user_sees_weather_details(browser):
  weather_info = browser.find_by_css(".weather-info")
  assert "London, United Kingdom" in weather_info.text
  assert "Average temperature" in weather_info.text
  assert "Temperature difference" in weather_info.text
  assert "OpenWeatherMap" in weather_info.text
  assert "WeatherAPI" in weather_info.text


# Test for incorrect user input
@scenario("user_input_city.feature", "User gives incorrect city name as input")
def test_user_inputs_incorrect_city():
  pass


@given("User enters the website")
def test_user_enters_website(visit_page):
  pass

@when("User types 'FakeCityName' as city name")
def user_inputs_incorrect_city(browser):
  browser.find_by_name("location").fill("FakeCityName")


@when("User clicks on the search button")
def user_clicks_search_button(browser):
  browser.find_by_css("button[type='submit']").click()


@then("User should see the error message 'Enter a valid city name'")
def user_should_see_error_message(browser):
  time.sleep(2)
  error_message = browser.find_by_css(".error-message").first
  assert "Enter a valid city name" in error_message.text


# Test for empty input
@scenario("user_input_city.feature", "User gives empty city name as input")
def test_user_leaves_input_field_empty():
  pass


@given("User enters the website")
def test_user_enters_website(visit_page):
  pass


@when("User types '' as city name")
def user_inputs_incorrect_city(browser):
  browser.find_by_name("location").fill("")


@when("User clicks on the search button")
def user_clicks_search_button(browser):
  browser.find_by_css("button[type='submit']").click()


@then("User should see the error message 'Enter a valid city name'")
def user_should_see_error_message(browser):
  time.sleep(2)
  error_message = browser.find_by_css(".error-message").first
  assert "Enter a valid city name" in error_message.text


# Test for differently interpreted city names
@scenario("user_input_city.feature", "User gives a city name that is interpreted differently by APIs")
def test_user_puts_city_name_that_is_interpreted_differently():
    pass


@given("User enters the website")
def test_user_enters_website(visit_page):
  pass


@when("User types 'Kairo' as city name")
def user_inputs_city_name(browser):
  browser.find_by_name("location").fill("Kairo")


@when("User clicks on the search button")
def user_clicks_search_button(browser):
  browser.find_by_css("button[type='submit']").click()


@then("User should see the note about the different interpretation of the city name by APIs")
def user_should_see_error_message(browser):
  time.sleep(2)
  note = browser.find_by_css(".note").first
  assert "Note, the APIs requested the weather data from different countries that have the same city name." in note.text