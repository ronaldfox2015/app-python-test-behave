Feature: Search Announcement
	As a user
	I want search announcements
	So that I can see all your information

	Background: Access the resource
		Given I access the resource

	Scenario Outline: Search a announcement by id
		Given I put the information of the location
		When I search the q <q>
		Then The quantity of result should be <result_len>
		Then The status code should be 200

		Examples:
			| q         | result_len |
			| lima      | 20	      	 |

	Scenario: Search announcements
		Given I search announcements
		When I dont use filters
		Then The result should be a list of announcements
		Then The status code should be 200
