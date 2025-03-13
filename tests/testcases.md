## API-calls

1. Both API-calls return correct data with correct call (mock, or check that temp is found from response)
2. The countries in the responses are the same (?, this can be problem, for example Cairo gives Egypt and Kenya)

## Errors

1. If neither of the API-keys is found, error (NameError) is shown and the program doesn't crash. HTTP Response is correct (404).
2. If either of API-keys is wrong, error (ValueError) is shown and the program doesn't crash. HTTP Response is correct (404).
3. If either of API-calls returns error (city name is invalid), error (ValueError) is shown and the program doesn't crash. The weather information field is not visible. HTTP Response is correct (404 or 400?).

## UI
  
1. After successful API-call, the data is updated on the page (Data from API:s is found from html). This needs to be mocked (because the temperature changes all the time)
2. Error messages are shown in error cases (Found in the rendered html)
3. Internal Server Error doesn't occur (check this in every error case)
4. The text entered in the form is still visible in the input field after error (found in the html)

## User input
1. HTML code as input is not interpret as html but as string
2. Incorrect input returns and shows error
3. Correct city name returns the weather for given city
4. 