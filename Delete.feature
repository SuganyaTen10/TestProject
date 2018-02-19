# Created by Suganya.Jagadeesan at 19/02/2018
Feature: Delete Student
  In Order to Delete a student detail
  As a Students Admin user
  I want a Delete link in Student page


  Scenario: Delete Student link
    Given Students Admin user is on Student Account Page
    When user wants to delete a student detail
    Then there must be a link as "Delete"
    And clicking the link should delete a student from list
    And user should be in the same Students page




