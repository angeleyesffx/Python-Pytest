Feature: Search
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  Background:
    Given I navigate to the Google Home page
<<<<<<< HEAD
  @wip
=======

>>>>>>> 4cae239e836e11bde80325c4f762c83f7b66419f
  Scenario Outline: Search the terms on Google
    When I search for <data>
    Then I should see the results

    Examples:
<<<<<<< HEAD
        | data        |
        | python      |
        | ruby        |

=======
        | data          |
        | python        |
        | apples        |

  Scenario Outline: Search the terms on Google1
    When I search for <data>
    Then I should see the results

    Examples:
        | data          |
        | python        |
        | apples        |
>>>>>>> 4cae239e836e11bde80325c4f762c83f7b66419f
