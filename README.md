# Glassdoor--Predicting-Job-Slot-Product-Retention

EXHIBIT 1 - EXPLANATION OF DATA							
							
Note:  Data reflects Job Slot contracts starting in or after April 2016 and ending in or before April 2018.  Each line represents a new contract transaction.  Customers who renew may appear more than							
once in the data set.  In rare cases, customers may purchase multiple Slot contracts around the same time.							
							
-- Slot Performance Data							
Employer_ID:			Unique identifier for a Glassdoor customer.  Note that some customers appear twice as they purchased Job Slots and then renewed, or purchased multiple contracts				
							
City_ID:			Unique identifier for the city a given employer resides				
							
Contract_ID:			Unique identifier for a contract				
							
StartDate:			The beginning date of the Job Slot contract				
							
EndDate:			The end date of the Job Slot contract				
							
Renewal_Flag:			True/false metric indicating whether the contract was renewed at the end of the contract: 1 = renewed, 0 = not renewed				
							
Job_Slots:			The number of job slots included in the package				
							
Total_Contract_Value:			Sold price of the contract				
							
Applications:			Total number of applications delivered over the course of the contract				
							
Apply_Start_Clicks:			Total number of apply start clicks delivered to clients. An apply start is defined as the click on the 'Apply Now' button on a Glassdoor job posting that brings the user to a portal to fill out a job application				
							
Click_Market_Value:			Total dollar value of the apply start clicks delivered to clients				
							
Job_Listings:			Total number of job listings customer posted through Glassdoor during the contract				
							
							
-- Location Data							
City_ID:			Unique identifier for the city a given employer resides				
							
City_Name:			City name which maps to a City_ID. City names are not unique since the same city name can exist across multiple states				
							
State_ID:			2-character value which the designates state for each City_Name and City_ID				
							
State_Name:			Full state name for each City_Name and City_ID				
