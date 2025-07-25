Feature: Order Transaction
  Tests related to Order Transaction

  Scenario Outline: Verify Order Success Message shown in details page
    Given Place the item order with <username> and <password>
    And the user is on the landing page
    When I login to portal with <username> and <password>
    And Navigate to orders page
    And Select the orderId
    Then Order message is successfully displayed

    Examples:
      | username               | password    |
      | diwakar12345@gmail.com | Diwakar@123 |
