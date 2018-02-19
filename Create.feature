Feature: Add New Student
  In Order to Add a new student detail
  As a Students Admin user
  I want FirstName, LastName, Academic Year


  Scenario: Add New Student link
    Given Students Admin user is on Student Account Page
    When user wants to add new student
    Then there must be a link as "Add New Student"
    And clicking the link should navigate to Add Students Page

  Scenario: Mandatory Details for Add New Student
    Given Students Admin user is on Add Student Page
    When user provides FirstName,LastName, Academic Year as mandatory details
    Then clicking Insert button should add the Student detail
    And the user should navigate to Students page

  Scenario: Canceling in the process of Add New Student
    Given Students Admin user is again on Add Student Page
    When user decides to cancel the addition of new Student
    Then clicking cancel button should cancel the addition
    And the user should navigate to Students page





